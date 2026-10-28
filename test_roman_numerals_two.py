from roman_numerals import to_roman_lazy


    
def test_to_roman_lazy_5():
    assert to_roman_lazy(5)=="V"
    
def test_to_roman_lazy():
    assert to_roman_lazy(1)=="I"
    