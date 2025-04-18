import subprocess


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
