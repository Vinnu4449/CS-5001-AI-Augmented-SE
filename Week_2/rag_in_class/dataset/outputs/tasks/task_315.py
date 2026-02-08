def find_Max_Len_Even(str):
    """
    Finds the longest substring with an even number of characters, separated by spaces.
    Returns the substring if found, otherwise returns "-1".
    """
    n = len(str)
    i = 0
    currlen = 0
    maxlen = 0
    st = -1  # start index of the longest even-length substring

    while i < n:
        if str[i] == ' ':
            # Check if current substring has even length
            if currlen % 2 == 0:
                if maxlen < currlen:
                    maxlen = currlen
                    st = i - currlen
            currlen = 0  # Reset for next substring
        else:
            currlen += 1
        i += 1

    # Check the last substring after loop ends
    if currlen % 2 == 0:
        if maxlen < currlen:
            maxlen = currlen
            st = i - currlen

    if st == -1:
        return "-1"
    return str[st: st + maxlen]
