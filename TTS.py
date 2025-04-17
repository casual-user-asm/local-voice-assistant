import pyttsx3
import subprocess
from STT import record_audio, transcribe_audio


engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0")
engine.setProperty('rate', rate-40)


def get_model_response(prompt):
    try:
        process = subprocess.Popen(
            ['ollama', 'run', 'gemma3:12b'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8'
        )

        stdout, stderr = process.communicate(input=prompt)

        if stderr:
            print("Error:", stderr)

        return stdout.strip()

    except Exception as e:
        return f"Error: {e}"


while True:
    audio_path = record_audio(duration=5)
    text = transcribe_audio(audio_path)
    if text.lower() in ["bye", "close", "exit"]:
        engine.say("Goodbye, have a nice day!")
        break
    response = get_model_response(text)
    engine.say(response)
    engine.runAndWait()
