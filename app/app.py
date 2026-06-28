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

# -----------------------------
# AUDIO SUPPORT
# -----------------------------
try:
    import speech_recognition as sr
    from pydub import AudioSegment
    AUDIO_OK = True
except:
    AUDIO_OK = False

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
# AUDIO
# =========================================================
def extract_audio_text(file_bytes, filename):

    if not AUDIO_OK:
        return "Audio libraries missing"

    recognizer = sr.Recognizer()

    try:
        audio_stream = io.BytesIO(file_bytes)

        if filename.endswith(".mp3"):
            audio = AudioSegment.from_file(audio_stream, format="mp3")
        elif filename.endswith(".wav"):
            audio = AudioSegment.from_file(audio_stream, format="wav")
        else:
            return "Unsupported audio format"

        wav_io = io.BytesIO()
        audio.export(wav_io, format="wav")
        wav_io.seek(0)

        with sr.AudioFile(wav_io) as source:
            audio_data = recognizer.record(source)

        try:
            return recognizer.recognize_google(audio_data)
        except:
            return "Could not transcribe audio"

    except Exception as e:
        return f"Audio error: {str(e)}"

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

        # ---------------- AUDIO ----------------
        elif filename.endswith((".mp3", ".wav")):
            text = extract_audio_text(file_bytes, filename)

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