from src.validation import validate_result


def test_valid_result():
    result = validate_result({
        "category": "cartao",
        "urgency": "alta",
        "response": "Bloqueie o cartão através de um canal oficial.",
    })
    assert result.category == "cartao"


def test_unknown_category_is_allowed():
    result = validate_result({
        "category": "desconhecida",
        "urgency": "baixa",
        "response": "Contacte o apoio ao cliente.",
    })
    assert result.category == "desconhecida"
