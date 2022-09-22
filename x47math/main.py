"""Math Library."""
import math


def hypothese(length: float, height: float) -> float:
    """Calculates you the hypothese of a triangle.

    Args:
        length (float): Length of one side.
        height (float): Height of second side.

    Returns:
        float: calculated hypothese

    Examples:
        .. code:: python

            >>> hypothese(9.5, 13.5)
            'Hello Roman!'
    """
    return math.sqrt(((length**2) + (height**2)));
