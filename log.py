from datetime import datetime


def add_log(text):
    with open("log.txt", "a", encoding="utf-8") as file:
        file.write(f'{datetime.now()} : {text}\n')