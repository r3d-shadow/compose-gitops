import subprocess

def execute_inline_script(script):
    try:
        subprocess.run(["bash", "-c", script], check=True)
        print("Inline script execution successful")
    except subprocess.CalledProcessError as e:
        print(f"Inline script execution failed with error: {e}")