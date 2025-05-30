import re

def tokenize(text):
    token_patterns = [
        ('NUMBER', r'\d+'),  # 123
        ('IDENTIFIER', r'[a-zA-Z_]\w*'),
        ('PLUS', r'\+'),
        ('MINUS', r'-'),
        ('TIMES', r'\*'),
        ('DIVIDE', r'/'),
        ('EQUALS', r'='),
        ('LPAREN', r'\('),
        ('RPAREN', r'\)'),
        ('WHITESPACE', r'\s+'),
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


code = "x = 42 + 7"
tokens = tokenize(code)
print(tokens)
