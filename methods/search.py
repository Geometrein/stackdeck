import random

from schemas.schemas import Card
from methods.util import load_deck


def get_random_card() -> Card:
    deck = load_deck()
    random_entry_key = random.choice(list(deck.keys()))
    office_by_id = deck[random_entry_key]
    return office_by_id


def search_single_framework(framework: str) -> dict:
    deck = load_deck()
    search_results = {}
    for key, card in deck.items():
        stack_list_lowercase = [string.lower() for string in card['stack']]
        if framework.lower() in stack_list_lowercase:
            search_results[key] = card
    return search_results


def search_multiple_frameworks(frameworks: list) -> dict:
    deck = load_deck()
    search_results = {}
    for key, card in deck.items():
        stack_list_lowercase = [string.lower() for string in card['stack']]
        search_stack_lowercase = [framework.lower() for framework in frameworks]
        if set(search_stack_lowercase).issubset(set(stack_list_lowercase)):
            search_results[key] = card
    return search_results


def search_by_company_name(company_name: str) -> Card:
    deck = load_deck()
    search_results = {}
    for key, card in deck.items():
        if company_name.lower() == card['name'].lower():
            search_results = deck[key]
            break
    return search_results


def search_framework_list(frameworks: list) -> dict:
    deck = load_deck()
    search_results = {}
    for key, card in deck.items():
        stack = card['stack']
        check = all(item in frameworks for item in stack)
        if check:
            search_results[key] = card
        else:
            pass
    return search_results