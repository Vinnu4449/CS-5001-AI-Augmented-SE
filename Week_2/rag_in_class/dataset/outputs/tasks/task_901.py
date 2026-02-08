def smallest_multiple(n):
    """Return the smallest positive multiple of n that is divisible by all integers from 1 to n."""
    if n <= 2:
        return n
    i = n * 2
    # Generate factors from n down to 3 (inclusive) where 2*factor > n
    factors = [number for number in range(n, 1, -1) if number * 2 > n]
    while True:
        for a in factors:
            if i % a != 0:
                i += n
                break
            # If we've checked all factors and i is divisible by the last one
            if a == factors[-1] and i % a == 0:
                return i
