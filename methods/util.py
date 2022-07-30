import os
import json
import random
import string


def load_deck() -> dict:
    deck_path = os.path.join('data', 'deck.json')
    with open(deck_path) as file:
        deck = json.load(file)
    return deck


def generate_random_key(name: str, length: int = 10) -> str:
    random.seed(name)
    characters = list(string.ascii_letters + string.digits)
    random.shuffle(characters)
    key = []
    for _ in range(length):
        key.append(random.choice(characters))
    random.shuffle(key)
    string_key = "".join(key)
    return string_key


def check_query_results(result: dict) -> bool:
    if len(result) > 0 and result.keys():
        return True
    else:
        return False
