#write at least 3 tests
#test for null input
#test for the translation of the world ‘Hello’ from English to French
#test for the translation of the world ‘Hello’ from English to German
#test for the translation of the world ‘Hello’ from English to French and then French to English
#test for the translation of the world ‘Hello’ from English to German and then German to English

#Test 1: test for null input

def test_null_input():
    assert english_to_french(None) == None, "The input is null"
    assert english_to_french("") == None, "The input is null"
    assert english_to_german(None) == None, "The input is null"


#Test 2: test for the translation of the world ‘Hello’ from English to French

def test_english_to_french():
    assert test_english_to_french("Hello") == "Bonjour", "The translation is wrong"
    assert test_english_to_french("Hello") != "Hello", "The translation is wrong"
    assert test_english_to_french("Hello") != "Hallo", "The translation is wrong"
    assert test_english_to_french("Hello") != "Hola", "The translation is wrong"


#Test 3: test for the translation of the world ‘Hello’ from English to German

def test_english_to_german():
    assert test_english_to_german("Hello") == "Hallo", "The translation is wrong"
    assert test_english_to_german("Hello") != "Hello", "The translation is wrong"
    assert test_english_to_german("Hello") != "Bonjour", "The translation is wrong" 
    assert test_english_to_german("Hello") != "Hola", "The translation is wrong"

