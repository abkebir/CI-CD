from sample import add_word,size

# Test add_word() function with an existing word
def test_add_existing_word():
    add_word('apple')
    assert add_word('apple') == False
    assert size() == 1