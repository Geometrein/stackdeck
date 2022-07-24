import os
import json
import random
from statistics import mode, mean
from collections import Counter
from schemas.schemas import Card


def load_deck() -> dict:
    deck_path = os.path.join('data', 'deck.json')
    with open(deck_path) as file:
        deck = json.load(file)
    return deck


def get_random_card() -> Card:
    deck = load_deck()
    random_entry_key = random.choice(list(deck.keys()))
    office_by_id = deck[random_entry_key]
    return office_by_id


def get_card_count() -> int:
    deck = load_deck()
    company_count = len(deck.keys())
    return company_count


def get_framework_count(deck: dict) -> int:
    framework_list = []
    for key, value in deck.items():
        for framework in value['stack']:
            framework_list.append(framework)
    framework_count = len(set(framework_list))
    return framework_count


def get_most_used_frameworks(n: int = 10) -> dict:
    deck = load_deck()
    framework_list = []
    for key, value in deck.items():
        for framework in value['stack']:
            framework_list.append(framework)

    frequency = Counter(framework_list)
    if len(frequency) > n:
        top_n_frameworks = frequency.most_common(n)
    else:
        top_n_frameworks = frequency.most_common(len(frequency))
    results = {key: value for key, value in top_n_frameworks}
    return results


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


def check_query_results(result: dict) -> bool:
    if len(result) > 0 and result.keys():
        return True
    else:
        return False


def get_mean_stack_length(deck: dict) -> int:
    stack_lengths = []
    for key, card in deck.items():
        stack_lengths.append(len(card['stack']))
    return int(mean(stack_lengths))


def get_most_used_framework(deck: dict) -> str:
    stacks = []
    for key, card in deck.items():
        stack = card['stack']
        for framework in stack:
            stacks.append(framework)
    return mode(stacks)


def get_deck_statistics() -> dict:
    deck = load_deck()
    deck_length = get_card_count()
    framework_count = get_framework_count(deck)
    most_used = get_most_used_framework(deck)
    mean_stack_length = get_mean_stack_length(deck)
    results = {
        'deck_length': deck_length,
        'most_used_framework': most_used,
        'total_frameworks': framework_count,
        'mean_stack_length': mean_stack_length
    }
    return results


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


def stack_similarity(first_card: str, second_card: str) -> dict:
    firs_company = search_by_company_name(company_name=first_card)
    second_company = search_by_company_name(company_name=second_card)
    result = set(firs_company['stack']).intersection(set(second_company['stack']))
    result = {
        'similarity': result,
    }
    return result


def stack_difference(first_card: str, second_card: str) -> dict:
    firs_company = search_by_company_name(company_name=first_card)
    second_company = search_by_company_name(company_name=second_card)
    result = set(firs_company['stack']).difference(set(second_company['stack']))
    result = {
        'difference': result,
    }
    return result


def stack_symmetric_difference(first_card: str, second_card: str) -> dict:
    firs_company = search_by_company_name(company_name=first_card)
    second_company = search_by_company_name(company_name=second_card)
    result = set(firs_company['stack']).symmetric_difference(set(second_company['stack']))
    result = {
        'symmetric_difference': result,
    }
    return result
