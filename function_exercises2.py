"""Function examples."""

# func()


def func():
    """E."""
    print("I´m inside the function")
# my_name_is(name)


def my_name_is(name) -> str:
    """Defineerib."""
    print(f"My name is {name}")
# sum_six(num)


def sum_six(num) -> int:
    """L."""
    return 6 + num
# sum_numbers()


def sum_numbers(a, b) -> int:
    """R."""
    sum = a + b
    return sum
# usd_to_eur()


def usd_to_eur(amount_usd) -> int:
    """M."""
    exchange_rate = 0.8
    return amount_usd * exchange_rate