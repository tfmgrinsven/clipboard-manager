import pyperclip
import time
from datetime import datetime


def print_history(history: list[dict[str, datetime]]) -> None:
    print(f"History at {datetime.now()}")
    for record in history:
        print(f"{record["time"]}: {record["text"]}")


def app():
    history = [
        {
            "text": pyperclip.paste(),
            "time": datetime.now()
        }
    ]
    while True:
        current = pyperclip.paste()
        if current != history[-1]["text"]:
            history.append({
                "text": current,
                "time": datetime.now()
            })
            print_history(history)
            print()
        time.sleep(3)


if __name__ == "__main__":
    app()