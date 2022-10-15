from fastapi import APIRouter, Query
from fastapi.templating import Jinja2Templates

from schemas.schemas import Card
from methods.util import (
    generate_random_key
)
from methods.networks import (
    generate_weighted_network_dict,
    generate_unweighted_network_dict
)

from methods.search import (
    get_random_card,
    search_by_company_name,
    search_multiple_frameworks
)

from methods.stats import (
    get_deck_statistics,
    get_most_used_frameworks
)

from methods.comparison import (
    stack_similarity,
    stack_difference,
    stack_symmetric_difference
)

endpoints = APIRouter()
templates = Jinja2Templates(directory="templates")


@endpoints.get("/deck-stats/", status_code=200)
async def get_deck_stats() -> dict:
    result = get_deck_statistics()
    return result


@endpoints.get("/cards/", status_code=200)
async def get_card_by_name(name: str = 'CHAOS') -> Card:
    """
    Returns a card by name.
    """
    search_results = search_by_company_name(name)
    return search_results


@endpoints.get("/cards/random", status_code=200)
async def get_random_item() -> Card:
    """
    Returns a random card from the deck.
    """
    search_results = get_random_card()
    return search_results


@endpoints.get("/cards/similarity/", status_code=200)
async def get_card_similarity(first_company_name: str = 'chaos', second_company_name: str = 'holvi') -> dict:
    """
    """
    common_frameworks = stack_similarity(first_company_name, second_company_name)
    return common_frameworks


@endpoints.get("/cards/difference/", status_code=200)
async def get_card_difference(
        first_company_name: str = 'chaos', second_company_name: str = 'holvi', symmetric: bool = False
) -> dict:
    """
    Returns the difference between stacks of two companies. If symmetric=True returns the symmetric difference.

    This Method uses frozenset.difference(*others) as per python documentation.
    """

    if symmetric:
        card_difference = stack_symmetric_difference(first_company_name, second_company_name)
    else:
        card_difference = stack_difference(first_company_name, second_company_name)
    return card_difference


@endpoints.get("/frameworks/", status_code=200)
async def get_cards_by_frameworks(frameworks=Query(default=None)) -> dict:
    """
    Returns cards that share the list of provided frameworks.
    """
    search_results = search_multiple_frameworks(frameworks)
    return search_results


@endpoints.get("/frameworks/frequency", status_code=200)
async def get_frameworks_by_use_frequency(length: int = 10) -> dict:
    """
    Returns cards that share the list of provided frameworks.
    """
    search_results = get_most_used_frameworks(n=length)
    return search_results


@endpoints.get("/networks/weighted", status_code=200)
async def get_weighted_network_edges(weight_tolerance: int = 8) -> dict:
    """
    Returns dictionary of dictionaries necessary for generating
    weighted edges in networkx.form_dict_of_dicts() method.
    """
    network_edge_dict = generate_weighted_network_dict(weight_tolerance=weight_tolerance)
    return network_edge_dict


@endpoints.get("/networks/unweighted", status_code=200)
async def get_unweighted_network_edges(connectivity_tolerance: int = 8) -> dict:
    """
    Returns dictionary of dictionaries necessary for generating
    unweighted edges in networkx.form_dict_of_dicts() method.
    """
    network_edge_dict = generate_unweighted_network_dict(connectivity_tolerance)
    return network_edge_dict


@endpoints.get("/util/id-generator/", status_code=200)
async def generate_card_id(name: str) -> dict:
    """
    Generates an id for a card.
    Used when adding new entries to the dataset.
    """
    card_id = generate_random_key(name.lower())
    return {"card_id": card_id}
