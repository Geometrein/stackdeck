from collections import Counter, defaultdict
from methods.util import load_deck


def generate_weighted_network_dict(weight_tolerance) -> dict:
    """
    Returns dictionary of dictionaries necessary for generating
    weighted edges in networkx.form_dict_of_dicts() method.
    https://networkx.org/documentation/stable/reference/generated/networkx.convert.from_dict_of_dicts.html
    """
    deck = load_deck()
    edge_dict = defaultdict(dict)
    for first_key, first_company in deck.items():
        first_company_name = first_company['name']
        first_company_stack = set(first_company['stack'])
        for second_key, second_company in deck.items():
            edge_weight = 0
            second_company_name = second_company['name']
            second_company_stack = set(second_company['stack'])
            common_technologies = first_company_stack.intersection(second_company_stack)
            if first_key != second_key and len(common_technologies) > weight_tolerance:
                edge_weight += len(common_technologies)
                edge_dict[first_company_name][second_company_name] = {"weight": edge_weight}
    return edge_dict


def generate_unweighted_network_dict(connectivity_tolerance) -> dict:
    """
    Returns dictionary of dictionaries necessary for generating
    unweighted edges in networkx.form_dict_of_dicts() method.
    https://networkx.org/documentation/stable/reference/generated/networkx.convert.from_dict_of_dicts.html
    """
    deck = load_deck()
    edge_dict = defaultdict(dict)
    for first_key, first_company in deck.items():
        first_company_name = first_company['name']
        first_company_stack = set(first_company['stack'])
        for second_key, second_company in deck.items():
            second_company_name = second_company['name']
            second_company_stack = set(second_company['stack'])
            common_technologies = first_company_stack.intersection(second_company_stack)
            if first_key != second_key and len(common_technologies) > connectivity_tolerance:
                edge_dict[first_company_name][second_company_name] = {"weight": 0}
    return edge_dict
