def filter_and_double(values):
    """
    Filters numbers greater than 10 and doubles them.

    Refactoring goals:
    - Better naming
    - Clear intent
    - Same behavior
    """
    result = []

    for value in values:
        if value > 10:
            result.append(value * 2)

    return result
