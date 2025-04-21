from listener import record_audio, transcribe_audio
from ai_conversation import get_model_response
from coqui import speaker

# Need to rework how should we end our conversation. Because now it doesn't work properly. Write a function to remove * from AI response

if __name__ == "__main__":
    while True:
        audio_path = record_audio(duration=5)
        text = transcribe_audio(audio_path)
        print(f'You say: {text}\n')
        # if text.lower() in ["bye", "close", "exit"]:
        #     engine.say("Goodbye, have a nice day!")
        #     break
        print("Waiting AI response...\n")
        response = get_model_response(text)
        print(f'AI response: {response}')
        speaker(response)
 