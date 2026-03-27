import pytest
from converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    celsius_to_kelvin,
    kelvin_to_celsius,
    convert,
)


def test_freezing_c_to_f(freezing_point):
    assert celsius_to_fahrenheit(freezing_point["C"]) == pytest.approx(
        freezing_point["F"]
    )


def test_boiling_c_to_f(boiling_point):
    assert celsius_to_fahrenheit(boiling_point["C"]) == pytest.approx(
        boiling_point["F"]
    )


@pytest.mark.parametrize(
    "c, expected_f",
    [
        (0, 32.0),
        (100, 212.0),
        (-40, -40.0),
        (37, 98.6),
    ],
)
def test_c_to_f_cases(c, expected_f):
    assert celsius_to_fahrenheit(c) == pytest.approx(expected_f, rel=1e-3)


def test_f_to_c():
    assert fahrenheit_to_celsius(32) == pytest.approx(0.0)


def test_kelvin_to_celsius():
    assert kelvin_to_celsius(273.15) == pytest.approx(0.0)


@pytest.mark.edge
def test_absolute_zero_kelvin():
    assert celsius_to_kelvin(-273.15) == pytest.approx(0.0)


@pytest.mark.edge
def test_below_absolute_zero_raises():
    with pytest.raises(ValueError):
        celsius_to_kelvin(-300)


def test_negative_kelvin_raises():
    with pytest.raises(ValueError):
        kelvin_to_celsius(-1)


def test_convert_same_unit():
    assert convert(25, "C", "C") == 25.0


def test_convert_c_to_k():
    assert convert(0, "C", "K") == pytest.approx(273.15)


def test_convert_f_to_c():
    assert convert(32, "F", "C") == pytest.approx(0.0)


def test_convert_k_to_f():
    assert convert(273.15, "K", "F") == pytest.approx(32.0)


def test_convert_unknown_unit():
    with pytest.raises(ValueError):
        convert(10, "X", "C")
