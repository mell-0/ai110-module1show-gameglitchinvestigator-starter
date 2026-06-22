from logic_utils import check_guess, parse_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- parse_guess tests ---

def test_parse_guess_valid_integer():
    ok, value, error = parse_guess("25", 1, 50)
    assert ok is True
    assert value == 25
    assert error is None

def test_parse_guess_boundary_low():
    ok, value, error = parse_guess("1", 1, 50)
    assert ok is True
    assert value == 1
    assert error is None

def test_parse_guess_boundary_high():
    ok, value, error = parse_guess("50", 1, 50)
    assert ok is True
    assert value == 50
    assert error is None

def test_parse_guess_whole_float():
    # "3.0" is a whole number and should be accepted
    ok, value, error = parse_guess("3.0", 1, 50)
    assert ok is True
    assert value == 3
    assert error is None

def test_parse_guess_decimal_float():
    # "3.5" is not a whole number and should be rejected
    ok, value, error = parse_guess("3.5", 1, 50)
    assert ok is False
    assert value is None
    assert error == "Please enter a whole number."

def test_parse_guess_empty_string():
    ok, value, error = parse_guess("", 1, 50)
    assert ok is False
    assert value is None
    assert error == "Enter a guess."

def test_parse_guess_non_numeric():
    ok, value, error = parse_guess("abc", 1, 50)
    assert ok is False
    assert value is None
    assert error == "That is not a number."

def test_parse_guess_too_low():
    ok, value, error = parse_guess("0", 1, 50)
    assert ok is False
    assert value is None
    assert error == "Guess must be between 1 and 50."

def test_parse_guess_too_high():
    ok, value, error = parse_guess("51", 1, 50)
    assert ok is False
    assert value is None
    assert error == "Guess must be between 1 and 50."


# --- get_range_for_difficulty tests ---

def test_range_easy():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_range_normal():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 50

def test_range_hard():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 100

def test_range_unknown_defaults():
    low, high = get_range_for_difficulty("Unknown")
    assert low == 1
    assert high == 50
