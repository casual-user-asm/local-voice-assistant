import sounddevice as sd
import scipy.io.wavfile as wav
import whisper
import tempfile
import numpy as np
import keyboard

model = whisper.load_model("tiny")


def record_audio(samplerate=16000):
    print("🎤 Hold SPACEBAR to record... release to stop.")

    frames = []
    recording = False

    def callback(indata, frames_count, time_info, status):
        if recording:
            frames.append(indata.copy())

    stream = sd.InputStream(samplerate=samplerate, channels=1, dtype='int16', callback=callback)

    with stream:
        while True:
            if keyboard.is_pressed("space"):
                if not recording:
                    print("🎙️ Recording started...")
                    recording = True
                sd.sleep(100)
            elif recording:
                print("🛑 Recording stopped.")
                break
            else:
                sd.sleep(100)

    audio = np.concatenate(frames, axis=0)

    temp_wav = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    wav.write(temp_wav.name, samplerate, audio)
    return temp_wav.name

def transcribe_audio(file_path):
    print("🧠 Transcribing with Whisper...\n")
    result = model.transcribe(file_path, language="en")
    return result["text"]
