import cmath
def len_complex(a, b):
    """Calculate the length (magnitude) of a complex number formed from real part a and imaginary part b.

    Args:
        a: Real part of the complex number
        b: Imaginary part of the complex number

    Returns:
        float: The magnitude (length) of the complex number
    """
    complex_number = complex(a, b)
    length = abs(complex_number)
    return length
