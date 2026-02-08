def upper_ctr(str):
    """Count the number of uppercase letters in the input string."""
    upper_ctr = 0
    for i in range(len(str)):
        if str[i] >= 'A' and str[i] <= 'Z':
            upper_ctr += 1
        return upper_ctr
