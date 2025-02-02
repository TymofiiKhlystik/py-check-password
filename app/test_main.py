import pytest
from app.main import check_password

@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("Abc12345!", True),
        ("abc123!", False),
        ("Abc1234567890", False),
        ("abc1234567890!", False),
        ("Abc!123", False),
        ("abc1234567890%", False),
    ]
)
def test_check_password(password, expected_result):
    assert check_password(password) == expected_result, f"Expected {expected_result} for password '{password}'"
