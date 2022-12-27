from validator import Validator, validate


def test_master_card():
    Validator("5555555555554444")


def test_visa():
    Validator("4242424242424242")


def test_amex():
    Validator("378282246310005")


def test_caller():
    validate("4242424242424242")
    validate(4242424242424242)


def test_caller_sad():
    for sadness in ("abc", 123):
        try:
            validate(sadness)
        except SystemExit:
            pass
