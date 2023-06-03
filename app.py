import streamlit as st
import speech_recognition as sr
import pyaudio

# Title to the app
original_title = '<p style="font-family:Ariel; color:Black; font-size: 25px;"><b>Speech to text Transcription (❁´◡`❁)</b></p>'
st.markdown(original_title, unsafe_allow_html=True)

# adding background from url using the HTML and st.markdown
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()


def transcribe_audio():
    r = sr.Recognizer() #The sr.Recognizer() initializes a recognizer object from the speech_recognition library, which will be used to transcribe the audio.
    with sr.Microphone() as source: #The code uses the with sr.Microphone() as source statement to open the default microphone as the audio source.
        st.write("Say something...")
        # The audio = r.listen(source) line captures the audio input from the microphone and stores it in the audio variable.
        audio = r.listen(source)
    #Error handling
    try:
        # The code uses r.recognize_google(audio) to transcribe the captured audio using the Google Web Speech API. The recognized text is stored in the text variable.
        text = r.recognize_google(audio)
        st.text_area("The transcription is: ",text)
    except sr.UnknownValueError:
        st.write("Unable to recognize speech")
    except sr.RequestError as e:
        st.write("Error: " + str(e))

#button to start transcription
if st.button("**Start Transcription🎙️**"):
    transcribe_audio()
#Button to stop transcription
if st.button("**STOP**"):
    st.markdown("**Thank You💕**")
