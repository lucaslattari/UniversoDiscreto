import pyaudio
import wave
import sys
import pydub
import speech_recognition as sr  
 
BUFFER_SIZE = 1024

def verificaMusica(string):
    if(string == "Toca Raul"):

        # Opening audio file as binary data
        wf = wave.open("raul.wav", 'rb')

        # Instantiate PyAudio
        p = pyaudio.PyAudio()

        #retorna comprimento de amostra em bytes
        #1 => 32 bits
        #2 => 8 bits
        #3 => 4 bits
        file_sw = wf.getsampwidth()
        stream = p.open(format=p.get_format_from_width(file_sw),
                        channels=wf.getnchannels(),
                        #taxa de amostragem
                        rate=wf.getframerate(), 
                        start=True,
                        output=True)

        data = wf.readframes(BUFFER_SIZE)
        while data != '':
            stream.write(data)
            data = wf.readframes(BUFFER_SIZE)

        stream.stop_stream()
        stream.close()

        p.terminate()

# get audio from the microphone                                                                       
r = sr.Recognizer()                                                                                   
with sr.Microphone() as source:
    print("Fale...\n\n")
    audio = r.listen(source)
 
try:
    string =  r.recognize_google(audio)
    print("Você disse: " + r.recognize_google(audio) + "\n\n")
    verificaMusica(string)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:    
    print("Could not request results; {0}".format(e))
