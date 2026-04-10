import pytest
from temperatura import TemperatureConverter


@pytest.fixture
def tc():
    return TemperatureConverter()

def test_celsius_to_kelvin(tc):
    assert tc.celsius_to_kelvin(0) == 273.15
    assert tc.celsius_to_kelvin(25) == 298.15


def test_kelvin_to_celsius(tc):
    assert tc.kelvin_to_celsius(273.15) == 0
    assert tc.kelvin_to_celsius(300) == 26.85
    
def test_celsius_to_fahrenheit(tc):
    assert tc.celsius_to_fahrenheit(0) == 32
    assert tc.celsius_to_fahrenheit(100) == 212
    assert tc.celsius_to_fahrenheit(-40) == -40

def test_fahrenheit_to_celsius(tc):
    assert tc.fahrenheit_to_celsius(32) == 0
    assert tc.fahrenheit_to_celsius(212) == 100
    

def test_below_absolute_zero_celsius(tc):
    with pytest.raises(ValueError):
        tc.celsius_to_kelvin(-300)


def test_negative_kelvin(tc):
    with pytest.raises(ValueError):
        tc.kelvin_to_celsius(-1)
        

def test_invalid_type(tc):
    with pytest.raises(TypeError):
        tc.celsius_to_kelvin("vinte")
        
def test_boolean_value(tc):
    with pytest.raises(TypeError):
        tc.celsius_to_kelvin(True)
