from TTS.api import TTS
import sounddevice as sd

tts = TTS(model_name="tts_models/en/ljspeech/vits", progress_bar=False, gpu=False)

def speaker(text):
    try:
        wav = tts.tts(text)
        sd.play(wav, samplerate=22050)
        sd.wait()
    except Exception as e:
        print(f"Error with TTS: {e}")
