# Model output for task_123

## Model
- devstral-small-2:24b-cloud

## Original Code:

def amicable_numbers_sum(limit):
    if not isinstance(limit, int):
        return "Input is not an integer!"
    if limit < 1:
        return "Input must be bigger than 0!"
    amicables = set()
    for num in range(2, limit+1):
        if num in amicables:
            continue
        sum_fact = sum([fact for fact in range(1, num) if num % fact == 0])
        sum_fact2 = sum([fact for fact in range(1, sum_fact) if sum_fact % fact == 0])
        if num == sum_fact2 and num != sum_fact:
            amicables.add(num)
            amicables.add(sum_fact2)
    return sum(amicables)

## Refactored Code:

```python
def amicable_numbers_sum(limit):
    """Calculate the sum of all amicable numbers up to a given limit.

    An amicable number is a number that is the sum of its proper divisors,
    excluding itself, and whose sum of proper divisors is the original number.

    Args:
        limit: The upper bound (inclusive) for finding amicable numbers.

    Returns:
        The sum of all amicable numbers up to the limit, or an error message if
        the input is invalid.
    """
    if not isinstance(limit, int):
        return "Input is not an integer!"
    if limit < 1:
        return "Input must be bigger than 0!"

    amicables = set()
    for num in range(2, limit + 1):
        if num in amicables:
            continue

        # Calculate sum of proper divisors for the current number
        sum_fact = sum(fact for fact in range(1, num) if num % fact == 0)

        # Calculate sum of proper divisors for the sum_fact
        sum_fact2 = sum(fact for fact in range(1, sum_fact) if sum_fact % fact == 0)

        # Check if the numbers form an amicable pair
        if num == sum_fact2 and num != sum_fact:
            amicables.add(num)
            amicables.add(sum_fact2)

    return sum(amicables)
```

- Preserved all function names, signatures, and return types exactly as in the original
- Maintained the same error message strings and validation logic
- Kept the same algorithm for finding amicable numbers (proper divisor sums)
- Preserved the set-based tracking of amicable numbers to avoid duplicates
- Maintained the same control flow including the early continue for already found numbers
- Used generator expressions instead of list comprehensions for better memory efficiency
- Added clear docstring explaining the function's purpose and behavior
- Preserved all numeric operations and comparison semantics exactly
- Maintained the same return value for the sum (including empty set case returning 0)
- Kept the same handling of edge cases (limit < 1, non-integer input)
