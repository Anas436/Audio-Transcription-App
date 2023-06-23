
# Import dependencies
import streamlit as st
import whisper
import ffmpeg

# Title of the app
st.title("Whisper App")

#upload audio file with streamlit
audio_file = st.file_uploader("Upload Audio", type=["wav", "mp3", "m4a"])

# Define Whisper Model
model = whisper.load_model("base")
st.text("Whisper Model Loaded")


# Transcribe Audio File
if st.sidebar.button("Transcribe Audio"):
    if audio_file is not None:
        st.sidebar.success("Transcribing Audio")
        transcription = model.transcribe(audio_file.name)
        st.sidebar.success("Transcription Completed")
        st.markdown(transcription["text"])

    else:
        st.sidebar.error("Please Upload an Audio File")

# Play Audio File 
st.sidebar.header("Play Original Audio File")
st.sidebar.audio(audio_file)
