from src.own.sample import add_word, size, check


# Test add_word() function with an existing word
def test_add_existing_word():
    add_word("apple")
    assert not add_word("apple")  # Should return False for existing word

    assert size() == 1


def test_check():
    global words
    words.update(["cat", "dog"])
    result = check()
    assert result == ["cat", "dog"]
