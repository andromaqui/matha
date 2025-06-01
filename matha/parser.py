class Parser:
    def __init__(self, tokens: list) -> None:
        self.tokens = tokens


    def parse(self):
        result = {}
        i = 0

        assert self.tokens[i][0] == 'FORWARD'
        i += 1

        var_name = self.tokens[i][1]
        i += 1

        assert self.tokens[i][0] == 'EQUALS'
        i += 1

        expr = []
        while self.tokens[i][0] in ['IDENTIFIER', 'PLUS', 'MULTIPLY', 'EXP', 'LPAREN', 'RPAREN', 'POWER', 'NUMBER']:
            expr.append(self.tokens[i][1])
            i += 1

        result['forward'] = {'var': var_name, 'expr': expr}

        result['data'] = {}
        for _ in range(2):
            assert self.tokens[i][0] == 'DATA'
            i += 1

            data_name = self.tokens[i][1]
            i += 1

            assert self.tokens[i][0] == 'EQUALS'
            i += 1

            assert self.tokens[i][0] == 'LBRACKET'
            i += 1

            values = []
            while self.tokens[i][0] == 'NUMBER':
                values.append(float(self.tokens[i][1]))
                i += 1
                if self.tokens[i][0] == 'COMMA':
                    i += 1

            assert self.tokens[i][0] == 'RBRACKET'
            i += 1

            result['data'][data_name] = values

        assert self.tokens[i][0] == 'INVERSE'
        i += 1

        i += 1
        return result