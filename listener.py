import sounddevice as sd
import scipy.io.wavfile as wav
import whisper
import tempfile

# Need to change logic of record voice. Must record voice for example on click some button. Instead of limited duration, this should 
# record until we hold the button.
def record_audio(duration=5, samplerate=16000):
    print(f"🎤 Recording for {duration} seconds...")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()
    
    temp_wav = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    wav.write(temp_wav.name, samplerate, recording)
    return temp_wav.name

def transcribe_audio(file_path):
    print("🧠 Transcribing with Whisper...\n")
    model = whisper.load_model("tiny")  # Options: tiny, base, small, medium, large
    result = model.transcribe(file_path)
    return result["text"]
