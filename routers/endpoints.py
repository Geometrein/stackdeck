from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from schemas.schemas import Card
from methods.util import (
    get_random_card,
    check_query_results,
    get_deck_statistics,
    search_by_company_name,
    search_multiple_frameworks,
    stack_similarity,
    stack_difference,
    stack_symmetric_difference,
    get_mots_used_frameworks
)

endpoints = APIRouter()
templates = Jinja2Templates(directory="templates")


@endpoints.get("/deck-stats/", status_code=200)
async def get_deck_stats() -> dict:
    result = get_deck_statistics()
    return result


@endpoints.get("/cards/", status_code=200, response_model=Card)
async def get_card_by_name(name: str = 'CHAOS') -> Card:
    """
    Returns a card by name.
    """
    search_results = search_by_company_name(name)
    return search_results


@endpoints.get("/cards/random", status_code=200, response_model=Card)
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
    if check_query_results(common_frameworks):
        return common_frameworks
    else:
        return {}


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

    if check_query_results(card_difference):
        return card_difference
    else:
        return {}


@endpoints.post("/frameworks/", status_code=200)
async def get_cards_by_frameworks(frameworks: list[str]) -> dict:
    """
    Returns cards that share the list of provided frameworks.
    """
    search_results = search_multiple_frameworks(frameworks)
    if check_query_results(search_results):
        return search_results
    else:
        return {}


@endpoints.get("/frameworks/frequency", status_code=200)
async def get_frameworks_by_use_frequency(length: int = 10) -> dict:
    """
    Returns cards that share the list of provided frameworks.
    """
    search_results = get_mots_used_frameworks(n=length)
    if check_query_results(search_results):
        return search_results
    else:
        return {}
