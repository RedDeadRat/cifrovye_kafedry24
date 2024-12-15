# TODO решите задачу
import json


INPUT_FILE = "input.json"


def task() -> float:
    with open(INPUT_FILE) as file:
        data = json.load(file)
        answer = sum(para["score"] * para["weight"] for para in data)
    return round(answer, 3)


print(task())
