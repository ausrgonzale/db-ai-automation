import pytest
from unittest.mock import MagicMock, patch
from data_gen.ai_generator import _parse_json_response, generate_fake_users


def test_parse_clean_json():
    """Should parse clean JSON without code fences."""
    text = '[{"name": "Widget", "price": 9.99, "stock": 10, "description": "A widget."}]'
    result = _parse_json_response(text)
    assert isinstance(result, list)
    assert result[0]["name"] == "Widget"


def test_parse_json_with_code_fences():
    """Should strip markdown code fences before parsing."""
    text = '```json\n[{"name": "Widget", "price": 9.99, "stock": 10, "description": "A widget."}]\n```'
    result = _parse_json_response(text)
    assert isinstance(result, list)
    assert result[0]["name"] == "Widget"


def test_parse_json_with_plain_fences():
    """Should strip plain code fences (no language tag) before parsing."""
    text = '```\n[{"name": "Widget", "price": 9.99, "stock": 10, "description": "A widget."}]\n```'
    result = _parse_json_response(text)
    assert isinstance(result, list)


def test_parse_invalid_json_raises():
    """Should raise JSONDecodeError on invalid JSON."""
    import json
    with pytest.raises(json.JSONDecodeError):
        _parse_json_response("this is not json")


def test_generate_fake_users_count():
    """Should return the correct number of users."""
    users = generate_fake_users(3)
    assert len(users) == 3


def test_generate_fake_users_structure():
    """Each user should have name and email keys."""
    users = generate_fake_users(2)
    for user in users:
        assert "name" in user
        assert "email" in user


def test_generate_fake_users_unique_emails():
    """All generated emails should be unique."""
    users = generate_fake_users(5)
    emails = [u["email"] for u in users]
    assert len(emails) == len(set(emails))
