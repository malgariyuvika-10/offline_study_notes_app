import streamlit as st
import time
import json
from datetime import datetime
import io

from pypdf import PdfReader
from backend.pipeline import StudyNotesPipeline

# -----------------------------
# OCR SUPPORT
# -----------------------------
from PIL import Image
import pytesseract

# Set the path to the Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)
# -----------------------------
# AUDIO SUPPORT
# -----------------------------
import whisper
import tempfile
import os
# -----------------------------
# WHISPER MODEL
# -----------------------------
@st.cache_resource
def load_whisper_model():
    return whisper.load_model("base")   # tiny, base, small

whisper_model = load_whisper_model()

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Offline Study Notes AI",
    page_icon="📚",
    layout="wide"
)

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("📚 Study Notes AI")
st.sidebar.info("Upload → Process → Results")
st.sidebar.success("CPU Offline Mode")

# -----------------------------
# SESSION STATE
# -----------------------------
if "history" not in st.session_state:
    st.session_state.history = []

if "result" not in st.session_state:
    st.session_state.result = None

if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None

# -----------------------------
# TITLE
# -----------------------------
st.title("📚 Offline Study Notes AI")
st.write("Convert PDF / Image / Audio / Text into structured notes (CPU only)")
st.markdown("---")

# =========================================================
# UPLOAD
# =========================================================
st.header("📤 Upload File")

uploaded = st.file_uploader(
    "Upload file",
    type=["pdf", "png", "jpg", "jpeg", "txt", "wav", "mp3"]
)

if uploaded:
    st.session_state.uploaded_file = uploaded
    st.success("Uploaded Successfully")
    st.write("Name:", uploaded.name)
    st.write("Type:", uploaded.type)

st.markdown("---")

# =========================================================
# AUDIO (WHISPER OFFLINE)
# =========================================================
def extract_audio_text(file_bytes, filename):
    """
    Transcribe MP3/WAV/M4A audio using Whisper (Offline)
    """
    try:
        suffix = os.path.splitext(filename)[1]

        # Save uploaded audio temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(file_bytes)
            temp_audio = tmp.name

        # Transcribe using Whisper
        result = whisper_model.transcribe(
            temp_audio,
            fp16=False,      # CPU mode
            verbose=False
        )

        # Delete temp file
        os.remove(temp_audio)

        transcript = result["text"].strip()

        if transcript == "":
            return "No speech detected."

        return transcript

    except Exception as e:
        return f"Could not transcribe audio: {str(e)}"

# =========================================================
# PROCESS
# =========================================================
st.header("⚙️ Process File")

if st.session_state.uploaded_file:

    if st.button("🚀 Start Processing"):

        progress = st.progress(0)
        status = st.empty()

        steps = [
            "Reading file...",
            "Extracting text...",
            "Processing content...",
            "Generating summary...",
            "Extracting topics...",
            "Finalizing..."
        ]

        for i in range(100):
            time.sleep(0.01)
            progress.progress(i + 1)

            status.info(steps[min(i // 20, 5)])

        file_bytes = st.session_state.uploaded_file.getvalue()
        filename = st.session_state.uploaded_file.name
        file_type = st.session_state.uploaded_file.type

        text = ""

        # ---------------- PDF ----------------
        if filename.endswith(".pdf"):
            reader = PdfReader(io.BytesIO(file_bytes))
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

        # ---------------- TEXT ----------------
        elif filename.endswith(".txt"):
            text = file_bytes.decode("utf-8", errors="ignore")

        # ---------------- IMAGE (OCR FIX) ----------------
        elif filename.endswith((".png", ".jpg", ".jpeg")):
            image = Image.open(io.BytesIO(file_bytes))
            text = pytesseract.image_to_string(image)

        elif filename.lower().endswith((".mp3", ".wav", ".m4a", ".flac")):

            with st.spinner("🎤 Transcribing audio using Whisper..."):
                text = extract_audio_text(file_bytes, filename)

            st.subheader("🎙 Transcript")
            st.write(text)

        else:
            text = ""

        # Safety fallback
        if not text.strip():
            text = "No readable content found"

        # ---------------- PIPELINE ----------------
        pipeline = StudyNotesPipeline()
        result = pipeline.process(text)

        st.session_state.result = result

        st.session_state.history.append({
            "file": filename,
            "time": datetime.now().strftime("%d-%m-%Y %H:%M")
        })

        st.success("Processing Completed 🎉")

st.markdown("---")

# =========================================================
# RESULTS
# =========================================================
st.header("📄 Results")

if st.session_state.result:

    result = st.session_state.result

    tab1, tab2, tab3 = st.tabs(["Summary", "Topics", "Flashcards"])

    with tab1:
        st.subheader(result.get("title", "Untitled"))
        st.write(result.get("summary", ""))

    with tab2:
        for t in result.get("topics", []):
            st.write("•", t)

    with tab3:
        for card in result.get("flashcards", []):
            st.write("Q:", card.get("Question", ""))
            st.success(card.get("Answer", ""))

    st.download_button(
        "Download JSON",
        json.dumps(result, indent=4),
        file_name="notes.json",
        mime="application/json"
    )

else:
    st.info("No results yet")

# =========================================================
# HISTORY
# =========================================================
st.header("History")

if not st.session_state.history:
    st.info("No files processed yet")
else:
    for h in st.session_state.history:
        st.write(f"{h['file']} | {h['time']}")

st.markdown("---")
st.caption("CPU Offline AI • Streamlit • Hackathon Ready")