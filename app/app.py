import streamlit as st
import time
import json
from datetime import datetime

from pypdf import PdfReader
import io

from backend.pipeline import StudyNotesPipeline

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Offline Study Notes AI",
    page_icon="📚",
    layout="wide"
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("📚 Study Notes AI")

st.sidebar.markdown("### Navigation (Single Page Mode)")
st.sidebar.info("Upload → Process → Results")

st.sidebar.markdown("---")
st.sidebar.success("Offline Mode")
st.sidebar.info("CPU Optimized")
st.sidebar.caption("Version 1.0")

# -----------------------------
# Session State Init
# -----------------------------
if "history" not in st.session_state:
    st.session_state.history = []

if "result" not in st.session_state:
    st.session_state.result = None

if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None

# -----------------------------
# Title
# -----------------------------
st.title("📚 Offline Study Notes Structuring AI")
st.write("Convert files into structured notes (100% CPU + Offline).")

st.markdown("---")

# =========================================================
# STEP 1 - UPLOAD
# =========================================================
st.header("📤 Step 1: Upload File")

uploaded = st.file_uploader(
    "Upload your study material",
    type=["pdf", "png", "jpg", "jpeg", "txt", "wav", "mp3"]
)

if uploaded:
    st.session_state.uploaded_file = uploaded

    st.success("File Uploaded Successfully ✅")
    st.write("📄 Name:", uploaded.name)
    st.write("📦 Type:", uploaded.type)
    st.write("💾 Size:", uploaded.size, "bytes")

st.markdown("---")

# =========================================================
# STEP 2 - PROCESS
# =========================================================
st.header("⚙️ Step 2: Process File")

if st.session_state.uploaded_file is None:
    st.warning("Please upload a file first.")
else:
    st.info(f"Ready to process: {st.session_state.uploaded_file.name}")

    if st.button("🚀 Start Processing"):

        progress = st.progress(0)
        status = st.empty()

        steps = [
            "Reading File...",
            "Extracting Text...",
            "Cleaning Text...",
            "Generating Summary...",
            "Extracting Topics...",
            "Finalizing Output..."
        ]

        for i in range(100):
            time.sleep(0.01)
            progress.progress(i + 1)

            if i < 20:
                status.info(steps[0])
            elif i < 40:
                status.info(steps[1])
            elif i < 60:
                status.info(steps[2])
            elif i < 80:
                status.info(steps[3])
            elif i < 95:
                status.info(steps[4])
            else:
                status.info(steps[5])

        # -----------------------------
        # REAL FILE CONTENT
        # -----------------------------
        file_bytes = st.session_state.uploaded_file.getvalue()

        try:
            text = file_bytes.decode("utf-8", errors="ignore")
        except:
            text = str(file_bytes)

        # -----------------------------
        # PIPELINE PROCESSING
        # -----------------------------
        pipeline = StudyNotesPipeline()
        result = pipeline.process(text)

        st.session_state.result = result

        # -----------------------------
        # HISTORY
        # -----------------------------
        st.session_state.history.append({
            "file": st.session_state.uploaded_file.name,
            "time": datetime.now().strftime("%d-%m-%Y %H:%M")
        })

        st.success("Processing Completed 🎉")

st.markdown("---")

# =========================================================
# STEP 3 - RESULTS
# =========================================================
st.header("📄 Step 3: Results")

if st.session_state.result is None:
    st.info("No output yet. Please process a file.")
else:
    result = st.session_state.result

    tab1, tab2, tab3 = st.tabs(["📌 Summary", "📚 Topics", "🧠 Flashcards"])

    with tab1:
        st.subheader(result["title"])
        st.write(result["summary"])

    with tab2:
        for topic in result["topics"]:
            st.write("•", topic)

    with tab3:
        for card in result.get("flashcards", []):
            st.write("**Q:**", card["Question"])
            st.success(card["Answer"])

    st.download_button(
        "⬇ Download JSON Notes",
        json.dumps(result, indent=4),
        file_name="study_notes.json",
        mime="application/json"
    )

st.markdown("---")

# =========================================================
# HISTORY
# =========================================================
st.header("📚 History")

if len(st.session_state.history) == 0:
    st.info("No files processed yet.")
else:
    for item in st.session_state.history:
        st.write(f"📄 {item['file']}  |  ⏰ {item['time']}")

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.caption("🚀 CPU-First Offline AI • Streamlit App • Hackathon Ready")