import pytest
from text_processor import TextProcessor


def test_capitalize_text_equal():
    """1. Assert equal - egyenlőség ellenőrzés"""
    processor = TextProcessor()
    result = processor.capitalize_text("hello world")
    assert result == "HELLO WORLD"

def test_capitalize_text_not_equal():
    """2. Assert not equal - nem egyenlő"""
    processor = TextProcessor()
    result = processor.capitalize_text("hello world")
    assert result != "hello world"
    assert result != "Hello World"

def test_reverse_text_in():
    """3. Assert in - benne van"""
    processor = TextProcessor()
    result = processor.reverse_text("hello")
    assert "o" in result
    assert "h" in result
    assert "olleh" in result

def test_reverse_text_not_in():
    """4. Assert not in - nincs benne"""
    processor = TextProcessor()
    result = processor.reverse_text("hello")
    assert "hello" not in result
    assert "x" not in result


def test_count_words_isinstance():
    """5. Assert isinstance - típus ellenőrzés"""
    processor = TextProcessor()
    result = processor.count_words("This is a test")
    assert isinstance(result, int)
    assert not isinstance(result, str)
    assert isinstance(result, int) and result == 4

def test_count_words_greater_less():
    """6. Assert >, <, >=, <= - összehasonlítás"""
    processor = TextProcessor()
    result1 = processor.count_words("One")
    result2 = processor.count_words("One two")
    result3 = processor.count_words("One two three")

    assert result1 < result2
    assert result3 > result2
    assert result2 >= result1


def test_count_words_empty_string():
    """7. Üres sztring bemenet ellenőrzése"""
    processor = TextProcessor()
    result = processor.count_words("")
    assert result == 0
    assert result is not None


def test_is_palindrome_true_false():
    """8. Assert True/False - boolean ellenőrzés"""
    processor = TextProcessor()
    result_true = processor.is_palindrome("Anna")
    assert result_true is True
    assert processor.is_palindrome("Hello") is False
    assert processor.is_palindrome("") is False
    assert processor.is_palindrome("Indul a görög aludni") is True
    

def test_remove_spaces_multiple_asserts():
    """9. Több assert egy tesztben"""
    pass

#