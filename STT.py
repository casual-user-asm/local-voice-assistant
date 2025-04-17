import sounddevice as sd
import scipy.io.wavfile as wav
import whisper
import tempfile

def record_audio(duration=5, samplerate=16000):
    print(f"🎤 Recording for {duration} seconds...")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()
    
    # Save to a temporary WAV file
    temp_wav = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    wav.write(temp_wav.name, samplerate, recording)
    return temp_wav.name

def transcribe_audio(file_path):
    print("🧠 Transcribing with Whisper...")
    model = whisper.load_model("tiny")  # Options: tiny, base, small, medium, large
    result = model.transcribe(file_path)
    return result["text"]
