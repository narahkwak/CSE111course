from names import make_full_name, \
    extract_given_name, extract_family_name
import pytest

def test_make_full_name():
    assert make_full_name("john", "smith") == "smith; john"
    assert make_full_name("", "") == "; "
    assert make_full_name("5", "6") == "6; 5"
    assert make_full_name("john", "smith") == "smith; john"
    

def test_extraxt_family():
    assert extract_family_name("smith; brown") == "smith"

def test_extract_given_name():
    assert extract_given_name("smith; brown") == "brown"


    
# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", "test_names.py"])


