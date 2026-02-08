# Model output for task_783

## Model
- devstral-small-2:24b-cloud

## Original Code:

def rgb_to_hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df/mx)*100
    v = mx*100
    return h, s, v

## Refactored Code:

```python
def rgb_to_hsv(r, g, b):
    # Normalize RGB values to the range [0, 1]
    r, g, b = r / 255.0, g / 255.0, b / 255.0

    # Find the maximum and minimum values among r, g, b
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn  # Delta (difference between max and min)

    # Calculate Hue (H)
    if mx == mn:
        h = 0  # Grayscale case
    elif mx == r:
        h = (60 * ((g - b) / df) + 360) % 360  # Red is dominant
    elif mx == g:
        h = (60 * ((b - r) / df) + 120) % 360  # Green is dominant
    elif mx == b:
        h = (60 * ((r - g) / df) + 240) % 360  # Blue is dominant

    # Calculate Saturation (S)
    if mx == 0:
        s = 0  # Black case
    else:
        s = (df / mx) * 100  # Saturation as percentage

    # Calculate Value (V)
    v = mx * 100  # Value as percentage

    return h, s, v
```

- Preserved all function names, signatures, and return types exactly as in the original
- Maintained the exact same control flow and early-exit behavior
- Kept all mathematical operations and comparisons identical
- Added clear comments explaining each calculation step without changing logic
- Preserved the exact same handling of edge cases (grayscale, black, etc.)
- Maintained the same normalization and percentage calculations
- Kept the same modulo operations for hue calculation
- Preserved all variable names that are part of the public interface
- Verified that the hue calculation for each color channel follows the original formula precisely
- Ensured the saturation and value calculations remain unchanged in their logic and structure
