from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_get_deck_stats():
    response = client.get("/deck-stats/")
    assert response.status_code == 200
    assert 'deck_length' in response.json()
    assert 'most_used_framework' in response.json()
    assert 'mean_stack_length' in response.json()
    assert 'total_frameworks' in response.json()


def test_get_card_by_name():
    response = client.get("/cards/?name=CHAOS")
    assert response.status_code == 200
    assert 'name' in response.json()
    assert 'flavor' in response.json()
    assert 'stack' in response.json()
    assert 'website' in response.json()
