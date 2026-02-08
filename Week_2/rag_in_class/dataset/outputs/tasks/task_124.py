import cmath

def angle_complex(a, b):
    """Calculate the phase angle of the complex number formed by a and b.

    Args:
        a: Real part of the complex number
        b: Imaginary part of the complex number

    Returns:
        The phase angle (in radians) of the complex number (a + b*1j)
    """
    cn = complex(a, b)
    angle = cmath.phase(a + b)
    return angle
