class Book:
    """A Book class that demonstrates Python magic methods."""
    
    def __init__(self, title, author, year):
        """
        Constructor: Initialize a Book instance with title, author, and year.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year of the book
        """
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """
        Destructor: Print a message when the book object is deleted.
        """
        print(f"Deleting {self.title}")
    
    def __str__(self):
        """
        String representation: Return a user-friendly string representation.
        
        Returns:
            str: A formatted string showing title, author, and year
        """
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """
        Official representation: Return a string that could recreate the object.
        
        Returns:
            str: A string that represents the constructor call to recreate the object
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
