__author__ = 'ebury'

class MathParseException(Exception):
    """
    MathParseException is a generic exception intended to be raised when a
    problem occurs during the parsing process in the Parse class
    """

    def __init__(self, message, errors={}):
        super(MathParseException, self).__init__(message)
        self.errors = errors


class RateNotFound(Exception):
    """
    RateNotFound is a specific exception made to be raised when retrieving
    some rate fails as it returns an empty list
    """

    def __init__(self, message, errors={}):
        super(RateNotFound, self).__init__(message)
        self.errors = errors