import streamlit as st
from ebook_ai import generate_ebook_content
from live_meeting_ai import transcribe_and_summarize_meeting

def main():
    st.title("AB Calypser: E-Book Writer & Meeting Summarizer")

    app_mode = st.sidebar.selectbox("Choose Mode", ["E-Book Writer", "Live Meeting Transcriber"])

    if app_mode == "E-Book Writer":
        st.header("Generate E-Book Content")
        topic = st.text_input("Enter e-book topic:")
        if st.button("Generate"):
            if topic:
                content = generate_ebook_content(topic)
                st.write(content)
                st.download_button("Download as DOCX", content, file_name="ebook_content.docx")
                st.download_button("Download as PDF", content, file_name="ebook_content.pdf")
            else:
                st.warning("Please enter a topic.")
    
    elif app_mode == "Live Meeting Transcriber":
        st.header("Live Meeting Transcriber")
        st.write("Use your microphone to record and transcribe meetings.")
        # Implement microphone input and transcription logic here

if __name__ == "__main__":
    main()
