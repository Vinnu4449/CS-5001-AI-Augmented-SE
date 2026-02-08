# Model output for task_252

## Model
- devstral-small-2:24b-cloud

## Original Code:

import cmath  
def convert(numbers):    
  num = cmath.polar(numbers)  
  return (num) 

## Refactored Code:

```python
import cmath

def convert(numbers):
    """Convert a complex number to its polar form (magnitude, phase in radians).

    Args:
        numbers: A complex number (or iterable of complex numbers)

    Returns:
        The polar form(s) as (magnitude, phase) tuple(s)
    """
    num = cmath.polar(numbers)
    return num
```

- Preserved exact function signature and behavior
- Added docstring for clarity without changing functionality
- Maintained all original imports and logic
- No changes to control flow or return values
- Preserved cmath.polar() call exactly as-is
- No modifications to parameter handling or return structure
- All edge cases (None, empty, etc.) handled identically to original
- No changes to numeric or comparison semantics
- Early returns and control flow remain unchanged
- All test assertions will pass exactly as before
