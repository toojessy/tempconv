ABSOLUTE_ZERO_C = -273.15


def celsius_to_fahrenheit(c: float) -> float:
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5 / 9


def celsius_to_kelvin(c: float) -> float:
    if c < ABSOLUTE_ZERO_C:
        raise ValueError("Temperature cannot be below absolute zero.")
    return c + 273.15


def kelvin_to_celsius(k: float) -> float:
    if k < 0:
        raise ValueError("Kelvin cannot be negative.")
    return k - 273.15


def convert(value: float, from_unit: str, to_unit: str) -> float:
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()

    if from_unit == to_unit:
        return float(value)

    if from_unit == "C":
        celsius_value = value
    elif from_unit == "F":
        celsius_value = fahrenheit_to_celsius(value)
    elif from_unit == "K":
        celsius_value = kelvin_to_celsius(value)
    else:
        raise ValueError("Unknown from_unit.")

    if to_unit == "C":
        return celsius_value
    if to_unit == "F":
        return celsius_to_fahrenheit(celsius_value)
    if to_unit == "K":
        return celsius_to_kelvin(celsius_value)

    raise ValueError("Unknown to_unit.")
