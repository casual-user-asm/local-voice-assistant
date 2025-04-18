from listener import record_audio, transcribe_audio
from ai_conversation import get_model_response
from speaker import engine

if __name__ == "__main__":
    while True:
        audio_path = record_audio(duration=5)
        text = transcribe_audio(audio_path)
        if text.lower() in ["bye", "close", "exit"]:
            engine.say("Goodbye, have a nice day!")
            break
        response = get_model_response(text)
        engine.say(response)
        engine.runAndWait()
