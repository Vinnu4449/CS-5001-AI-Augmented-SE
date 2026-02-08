# Model output for task_107

## Model
- devstral-small-2:24b-cloud

## Original Code:

def count_Hexadecimal(L,R) :  
    count = 0;  
    for i in range(L,R + 1) : 
        if (i >= 10 and i <= 15) : 
            count += 1;  
        elif (i > 15) : 
            k = i;  
            while (k != 0) :  
                if (k % 16 >= 10) : 
                    count += 1;  
                k = k // 16;  
    return count;  

## Refactored Code:

```python
def count_Hexadecimal(L, R):
    """
    Counts the number of hexadecimal digits in the decimal representation of numbers from L to R (inclusive).

    A hexadecimal digit is any digit in the range 10-15 (A-F in hexadecimal).
    For numbers 10-15, they are counted directly as they represent single hexadecimal digits.
    For numbers >15, each digit in their base-16 representation is checked if it's a hexadecimal digit (10-15).

    Args:
        L (int): Start of range (inclusive)
        R (int): End of range (inclusive)

    Returns:
        int: Count of hexadecimal digits found in the range
    """
    count = 0
    for i in range(L, R + 1):
        if (i >= 10 and i <= 15):
            count += 1
        elif (i > 15):
            k = i
            while (k != 0):
                if (k % 16 >= 10):
                    count += 1
                k = k // 16
    return count
```

- Preserved exact function name `count_Hexadecimal` and signature
- Maintained original logic for counting hexadecimal digits (10-15)
- Kept the same control flow structure with identical condition boundaries
- Preserved the special case handling for numbers 10-15
- Maintained the base-16 digit checking logic for numbers >15
- Kept the same loop and while loop structures unchanged
- Preserved all return behavior and early-exit conditions
- Added docstring for clarity without changing functionality
- Maintained all numeric operations exactly as original
- Preserved the inclusive range behavior (R + 1 in range)
