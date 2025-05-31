import re

class Lexer():

    def __init__(self, code):
        self.code = code
        self.token_patterns = [
            ('FORWARD', r'forward'),
            ('DATA', r'data'),
            ('INVERSE', r'inverse'),
            ('USING', r'using'),
            ('EQUALS', r'='),
            ('PLUS', r'\+'),
            ('ARROW', r'->'),
            ('LBRACKET', r'\['),
            ('RBRACKET', r'\]'),
            ('COMMA', r','),
            ('NUMBER', r'\d+\.?\d*'),
            ('IDENTIFIER', r'[a-zA-Z_]\w*'),
            ('LPAREN', r'\('),
            ('RPAREN', r'\)'),
            ('WHITESPACE', r'\s+'),
        ]

    def tokenize(self):
        tokens = []
        position = 0

        while position < len(self.code):
            matched = False

            for token_type, pattern in self.token_patterns:
                regex = re.compile(pattern)
                match = regex.match(self.code, position)

                if match:
                    value = match.group(0)
                    if token_type != 'WHITESPACE':
                        tokens.append((token_type, value))
                    position = match.end()
                    matched = True
                    break

            if not matched:
                raise SyntaxError(f"Unknown character: {self.code[position]}")

        return tokens


    sample_input = """forward y = x + b 
    data observed = [2.1, 3.2, 4.0, 5.1] 
    data x_values = [1, 2, 3, 4] 
    inverse estimate(observed, x_values) -> b 
       using y"""

