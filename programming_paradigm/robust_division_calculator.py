def safe_divide(numerator, denominator):
    """
    Performs division with robust error handling.
    
    Args:
        numerator: The dividend (can be string or numeric)
        denominator: The divisor (can be string or numeric)
    
    Returns:
        str: Result message or error message
    """
    try:
        # Convert inputs to floats
        num = float(numerator)
        denom = float(denominator)
        
        # Check for division by zero
        if denom == 0:
            return "Error: Cannot divide by zero."
        
        # Perform division
        result = num / denom
        return f"The result of the division is {result}"
        
    except ValueError:
        # Handle non-numeric inputs
        return "Error: Please enter numeric values only."