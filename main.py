'''
Script for Thoughtful AI's technical assessment for the FDE role. 
Franz Adam
'''

def sort(width, height, length, mass):
  """
    Dispatch a package to the correct stack based on size and weight rules.

    Args:
        width, height, length: Dimensions in centimeters.
        mass: Mass in kilograms.

    Returns:
        "STANDARD", "SPECIAL", or "REJECTED".
    """
  # Input validation to catch edge cases
  for name, value in (("width", width), ("height", height), ("length", length),
                      ("mass", mass)):
    if value is None:
      raise ValueError(f"{name} must not be None")
    if value < 0:
      raise ValueError(f"{name} must be non-negative")

  volume = width * height * length

  bulky = (volume >= 1_000_000) or (width >= 150) or (height
                                                      >= 150) or (length
                                                                  >= 150)
  heavy = mass >= 20

  if bulky and heavy:
    return "REJECTED"
  if bulky or heavy:
    return "SPECIAL"
  return "STANDARD"


if __name__ == "__main__":
  print(sort(10, 10, 10, 1))
