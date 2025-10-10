class Calculator:
    """Calculator class demonstrating static methods and class methods."""
    
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Sum of a and b
        """
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        Prints the calculation type before performing multiplication.
        
        Args:
            cls: Reference to the class
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
