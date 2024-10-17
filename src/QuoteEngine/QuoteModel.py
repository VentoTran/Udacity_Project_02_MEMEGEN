"""
Module for QuoteModel Class.

Implementation of the Quote Model.
"""


class QuoteModel:
    """Represent models for Quote."""

    def __init__(self, body, author):
        """Create a new QuoTeModel."""
        self.body = body
        self.author = author
    # enddef

    def __repr__(self):
        """Return a representation of QuotelModel."""
        return f"{self.body} - {self.author}"
    # enddef

# endclass
