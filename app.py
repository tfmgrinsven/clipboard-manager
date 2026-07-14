import pyperclip
import time

def app():
    last = ""
    while True:
        current = pyperclip.paste()
        if current != last:
            print(f"New clipboard content: {current}")
            last = current
        time.sleep(1)

if __name__ == "__main__":
    app()