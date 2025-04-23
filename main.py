from listener import record_audio, transcribe_audio
from coqui import speaker
from ai_response import get_response
import sys
import signal


def signal_handler(sig, frame):
    print("\n🛑 Ctrl+C detected. Exiting now...")
    speaker("Goodbye, have a nice day!")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

#  Write a function to remove * from AI response
if __name__ == "__main__":
    conversation = []
    while True:
        audio_path = record_audio()
        text = transcribe_audio(audio_path)
        conversation.append({"role": "user", "content": text + "Answer in few sentences."})

        print(f'You said: {text}\n\n')
        print("Waiting AI response...\n\n")

        response = get_response(conversation)
        conversation.append({"role": "assistant", "content": response})

        print(f'AI response: {response}\n\n')

        speaker(response)
        
        print("Press Ctrl+C to stop conversation\n\n")
