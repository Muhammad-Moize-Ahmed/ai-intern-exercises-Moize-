import math


SAFE_MATH_FUNCTIONS = {
    "sqrt": math.sqrt,
    "pow": math.pow,
    "abs": abs,
    "round": round,
    "pi": math.pi,
    "e": math.e,
}


def calculator(expression: str) -> float | str:
    """
    Evaluate a mathematical expression safely.

    Args:
        expression: A string containing a math expression e.g. '25 * 8'

    Returns:
        The numeric result or an error message string.
    """
    try:
        result = eval(expression, {"__builtins__": {}}, SAFE_MATH_FUNCTIONS)
        return round(result, 6)
    except Exception as error:
        return f"Calculator error: {error}"
