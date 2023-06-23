# Audio-Transcription-App



This is a Python application that allows you to load a Audio file and create transcription using natural language. The application uses a recently releases Whishper of OpenAI. The Whisper will not answer show any text unrelated to the Audio.


![](https://github.com/Anas436/Audio-Transcription-App/blob/main/Demo.png)

## How it works

The "Whisper App" is a Streamlit-based application that allows users to upload audio files and transcribe them into text using the Whisper model. Users can easily upload their audio files, initiate the transcription process, and view the transcribed text. The app also provides a feature to play the original audio file. It simplifies audio transcription and offers a user-friendly interface for a seamless experience.

## Installation

To install the repository, please clone this repository and install the requirements:

```
pip install -r requirements.txt
```

You will also need to add your OpenAI API key to the `.env` file.

## Usage

To use the application, run the `main.py` file with the streamlit CLI (after having installed streamlit): 

```
streamlit run app.py
```
