import re
from parser import Parser

def tokenize(text):
    token_patterns = [
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
        ('WHITESPACE', r'\s+'),  # Skip whitespace
    ]

    tokens = []
    position = 0

    while position < len(text):
        matched = False

        for token_type, pattern in token_patterns:
            regex = re.compile(pattern)
            match = regex.match(text, position)

            if match:
                value = match.group(0)
                if token_type != 'WHITESPACE':
                    tokens.append((token_type, value))
                position = match.end()
                matched = True
                break

        if not matched:
            raise SyntaxError(f"Unknown character: {text[position]}")

    return tokens


sample_input = """forward y = x + b 
data observed = [2.1, 3.2, 4.0, 5.1] 
data x_values = [1, 2, 3, 4] 
inverse estimate(observed, x_values) -> b 
   using y"""
tokens = tokenize(sample_input)
parser = Parser(tokens)
print(parser.parse())

