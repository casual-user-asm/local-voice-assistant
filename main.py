from listener import record_audio, transcribe_audio
from coqui import speaker
from ai_response import get_response

# Need to rework how should we end our conversation. Because now it doesn't work properly. Write a function to remove * from AI response
if __name__ == "__main__":
    conversation = []
    while True:
        audio_path = record_audio(duration=5)
        text = transcribe_audio(audio_path)
        conversation.append({"role": "user", "content": text + "Answer briefly."})
        # print(f'You say: {text}\n')
        # if text.lower() in ["bye", "close", "exit"]:
        #     engine.say("Goodbye, have a nice day!")
        #     break
        print("Waiting AI response...\n")
        response = get_response(conversation)
        conversation.append({"role": "assistant", "content": response})
        print(f'AI response: {response}')
        speaker(response)
 