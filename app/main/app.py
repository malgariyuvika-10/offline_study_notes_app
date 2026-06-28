import streamlit as st
from pathlib import Path
import time

# --------------------
# Page Config
# --------------------
st.set_page_config(
    page_title="StudyStruct AI",
    page_icon="📚",
    layout="wide"
)

UPLOAD_DIR = Path("uploads")
OUTPUT_DIR = Path("outputs")

UPLOAD_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

# --------------------
# Sidebar
# --------------------

st.sidebar.title("📚 StudyStruct AI")

model = st.sidebar.selectbox(
    "AI Model",
    [
        "Llama",
        "Mistral",
        "Gemma"
    ]
)

st.sidebar.success("Offline Mode")

# --------------------
# Header
# --------------------

st.title("📚 StudyStruct AI")

st.caption("Offline AI Study Notes Structuring")

st.divider()

# --------------------
# Upload Section
# --------------------

uploaded_file = st.file_uploader(
    "Upload PDF / Image / Audio / Text",
    type=[
        "pdf",
        "png",
        "jpg",
        "jpeg",
        "txt",
        "wav",
        "mp3"
    ]
)

if uploaded_file:

    save_path = UPLOAD_DIR / uploaded_file.name

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File Uploaded Successfully!")

    col1, col2, col3 = st.columns(3)

    col1.metric("File", uploaded_file.name)

    col2.metric(
        "Type",
        uploaded_file.type
    )

    col3.metric(
        "Size",
        f"{uploaded_file.size/1024:.1f} KB"
    )

    st.divider()

    if st.button(
        "🚀 Process File",
        use_container_width=True
    ):

        progress = st.progress(0)

        status = st.empty()

        for i in range(101):

            time.sleep(0.02)

            progress.progress(i)

            status.text(
                f"Processing... {i}%"
            )

        status.success("Processing Complete!")

        # --------------------
        # Dummy Results
        # (Replace with backend later)
        # --------------------

        st.divider()

        st.header("📑 Results")

        from app.backend.pipeline import StudyNotesPipeline

        pipeline = StudyNotesPipeline()

        result = pipeline.process_file(str(save_path))

        summary = result["summary"]
        topics = result["topics"]
        flashcards = result["flashcards"]

        keypoints = [
            "Point 1",
            "Point 2",
            "Point 3",
            "Point 4"
        ]

        flashcards = [
            ("Question 1","Answer 1"),
            ("Question 2","Answer 2")
        ]

        quiz = [
            "1. Sample MCQ?",
            "2. Sample MCQ?"
        ]

        tab1, tab2, tab3 = st.tabs(
            [
                "Summary",
                "Flashcards",
                "Quiz"
            ]
        )

        with tab1:

            st.subheader("Summary")

            st.write(summary)

            st.subheader("Key Points")

            for point in keypoints:
                st.write("•", point)

        with tab2:

            st.subheader("Flashcards")

            for q, a in flashcards:

                with st.expander(q):

                    st.write(a)

        with tab3:

            st.subheader("Quiz")

            for q in quiz:

                st.write(q)

        st.download_button(
            "📥 Download Notes",
            summary,
            file_name="summary.txt"
        )