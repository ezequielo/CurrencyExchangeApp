from utils.custom_exceptions import MathParseException

class Parser:
    """
    This is a math expression parser, which is in charge of making the necessary actions
    for understanding the expression and then compute the results and return a value
    """

    def __init__(self, string):
        """
        Init method, responsible for initiate the Parser object with the math expression

        :param string: Math expression contained in a string
        :return: A Parse object
        """

        self.string = string
        self.index = 0

    def get_value(self):
        """
        This method make the necessary calls to retrieve a value which is the result of the
        math expression. Then this value is returned if the expression is valid

        :return: Result of the math expression
        """

        value = self.parse_addition()
        self.skip_whitespace()
        if self.has_next():
            raise MathParseException("Unexpected character found: '" + self.peek() + "' at index " + str(self.index))
        return value

    def peek(self):
        """
        This method returns the character in the string of the current index
        :return: Character of the expression
        """
        return self.string[self.index:self.index + 1]
    
    def has_next(self):
        """
        has_next() method is able to predict if there are more characters in the string or not
        considering the position given by the index variable

        :return: True/False depending if there are or not more character in the string
        """

        return self.index < len(self.string)
    
    def skip_whitespace(self):
        """
        Helper method for avoiding the whitespaces in the string so that, we can focus on
        the interesting characters such as numbers, operators or parenthesis

        :return: None. It just uptades the index variable
        """

        while self.has_next():
            if self.peek() in ' \t\n\r':
                self.index += 1
            else:
                return
    
    def parse_addition(self):
        """
        With this method, the Parse class can detect if there is a symbol that implies addition
        or division in the char given by the index attribute

        :return: The result of a multiplication/division operation
        """

        values = [self.parse_multiplication()]
        while True:
            self.skip_whitespace()
            char = self.peek()
            if char == '+':
                self.index += 1
                values.append(self.parse_multiplication())
            elif char == '-':
                self.index += 1
                values.append(-1 * self.parse_multiplication())
            else:
                break
        return sum(values)
    
    def parse_multiplication(self):
        """
        With this method, the Parse class can detect if there is a symbol that implies multiplication
        or division in the char given by the index attribute

        :return: The result of a multiplication/division operation
        """

        values = [self.parse_parenthesis()]
        while True:
            self.skip_whitespace()
            char = self.peek()
            if char == '*':
                self.index += 1
                values.append(self.parse_parenthesis())
            elif char == '/':
                div_index = self.index
                self.index += 1
                denominator = self.parse_parenthesis()
                if denominator == 0:
                    raise MathParseException(
                        "Division by 0 kills baby whales (occurred at index " + str(div_index) + ")")
                values.append(1.0 / denominator)
            else:
                break
        value = 1.0
        for factor in values:
            value *= factor
        return value
    
    def parse_parenthesis(self):
        """
        This chunk of code is intended to detect parenthesis in a expression, so that, the operations
        inside them ca be treated with a suitable priority

        :return: The value of a expression contained in a parenthesis
        """

        self.skip_whitespace()
        char = self.peek()
        if char == '(':
            self.index += 1
            value = self.parse_addition()
            self.skip_whitespace()
            if self.peek() != ')':
                raise MathParseException(
                    "No closing parenthesis found at character "
                    + str(self.index))
            self.index += 1
            return value
        else:
            return self.parse_negative()
    
    def parse_negative(self):
        """
        parse_negative() method detects negative values in the expression

        :return: A negative number
        """

        self.skip_whitespace()
        char = self.peek()
        if char == '-':
            self.index += 1
            return -1 * self.parse_parenthesis()
        else:
            return self.parse_number()

    def parse_number(self):
        """
        This method is intended to make the necessary assertions to identify numbers in the
        string attribute

        :return: A substring containing a number with one or more digits including decimals
        """

        self.skip_whitespace()
        char = self.peek()
        if char in '0123456789.':

            self.skip_whitespace()
            str_value = ''
            decimal_found = False
            char = ''

            while self.has_next():
                char = self.peek()
                if char == '.':
                    if decimal_found:
                        raise MathParseException(
                            "Found an extra period in a number at character " + str(self.index))
                    decimal_found = True
                    str_value += '.'
                elif char in '0123456789':
                    str_value += char
                else:
                    break
                self.index += 1

            if len(str_value) == 0:
                if char == '':
                    raise MathParseException("Unexpected end found")
                else:
                    raise MathParseException("I was expecting to find a number at character " +
                        str(self.index) + " but instead I found a '" + char)
            return float(str_value)

        else:
            raise MathParseException("I was expecting a number or a symbol")
