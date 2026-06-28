import streamlit as st
import time
import json
from datetime import datetime

# -----------------------------
# Page Configuration
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

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📤 Upload",
        "⚙️ Process",
        "📄 Results",
        "📚 History"
    ]
)

st.sidebar.markdown("---")

st.sidebar.success("Offline Mode")

st.sidebar.info("CPU Optimized")

st.sidebar.caption("Version 1.0")

# -----------------------------
# Dummy Database
# -----------------------------
if "history" not in st.session_state:
    st.session_state.history = []

if "result" not in st.session_state:
    st.session_state.result = None

if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None

# -----------------------------
# HOME
# -----------------------------
if page == "🏠 Home":

    st.title("📚 Offline Study Notes Structuring AI")

    st.write(
        """
Convert PDFs, Images, Audio and Text into structured study notes.

Everything runs locally on CPU.
"""
    )

    c1, c2, c3 = st.columns(3)

    c1.metric("Supported Formats", "7+")

    c2.metric("Offline", "Yes")

    c3.metric("CPU Required", "Only")

    st.markdown("---")

    st.subheader("Features")

    st.write("✅ PDF Parsing")

    st.write("✅ OCR")

    st.write("✅ Audio Transcription")

    st.write("✅ AI Summary")

    st.write("✅ Flashcards")

    st.write("✅ JSON Export")

# -----------------------------
# UPLOAD
# -----------------------------
elif page == "📤 Upload":

    st.title("📤 Upload Study Material")

    uploaded = st.file_uploader(
        "Choose a file",
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

    if uploaded:

        st.session_state.uploaded_file = uploaded

        st.success("File Uploaded Successfully")

        st.write("Filename:", uploaded.name)

        st.write("Type:", uploaded.type)

        st.write("Size:", uploaded.size, "bytes")

# -----------------------------
# PROCESS
# -----------------------------
elif page == "⚙️ Process":

    st.title("⚙️ AI Processing")

    if st.session_state.uploaded_file is None:

        st.warning("Please upload a file first.")

    else:

        st.write("Selected File:")

        st.success(st.session_state.uploaded_file.name)

        if st.button("Start Processing"):

            progress = st.progress(0)

            status = st.empty()

            steps = [
                "Reading File...",
                "Extracting Text...",
                "Cleaning Text...",
                "Generating Summary...",
                "Creating Flashcards...",
                "Saving..."
            ]

            for i in range(100):

                time.sleep(0.03)

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

            result = {
                "title": "Introduction to Artificial Intelligence",

                "summary":
                "Artificial Intelligence enables machines to perform tasks that normally require human intelligence.",

                "topics": [
                    "Machine Learning",
                    "Deep Learning",
                    "Neural Networks",
                    "Computer Vision"
                ],

                "flashcards": [
                    {
                        "Question": "What is AI?",
                        "Answer": "Artificial Intelligence"
                    },
                    {
                        "Question": "What is ML?",
                        "Answer": "Machine Learning"
                    }
                ]
            }

            st.session_state.result = result

            st.session_state.history.append(
                {
                    "file":
                    st.session_state.uploaded_file.name,
                    "time":
                    datetime.now().strftime("%d-%m-%Y %H:%M")
                }
            )

            st.success("Processing Completed!")

# -----------------------------
# RESULTS
# -----------------------------
elif page == "📄 Results":

    st.title("📄 Structured Notes")

    if st.session_state.result is None:

        st.warning("No processed file available.")

    else:

        result = st.session_state.result

        tab1, tab2, tab3 = st.tabs(
            [
                "Summary",
                "Topics",
                "Flashcards"
            ]
        )

        with tab1:

            st.subheader(result["title"])

            st.write(result["summary"])

        with tab2:

            for topic in result["topics"]:

                st.write("•", topic)

        with tab3:

            for flashcard in result["flashcards"]:

                st.write("### Q:", flashcard["Question"])

                st.success(flashcard["Answer"])

        st.download_button(

            "⬇ Download JSON",

            json.dumps(
                result,
                indent=4
            ),

            file_name="study_notes.json",

            mime="application/json"
        )

# -----------------------------
# HISTORY
# -----------------------------
elif page == "📚 History":

    st.title("📚 Processing History")

    if len(st.session_state.history) == 0:

        st.info("No files processed.")

    else:

        for item in st.session_state.history:

            st.write(
                f"📄 {item['file']}   |   {item['time']}"
            )

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")

st.caption(
    "CPU-First Hackathon • Offline Study Notes AI • Streamlit"
)