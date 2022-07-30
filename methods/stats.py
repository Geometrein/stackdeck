from statistics import mode, mean
from collections import Counter

from methods.util import load_deck


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
