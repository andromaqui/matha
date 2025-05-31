from lexer import Lexer
from parser import Parser
from solver import Solver

def run_matha(code):
    lexer = Lexer(code)
    tokenized_code = lexer.tokenize()

    parser = Parser(tokenized_code)
    parsed_code = parser.parse()

    solver = Solver(parsed_code)
    solution = solver.solve()
    return solution

def matha_repl():
    print("Matha Interactive Shell")
    print("Type 'exit' to quit")

    while True:
        try:
            code = input("matha> ")

            if code.strip() == "exit":
                break

            result = run_matha(code)
            print(f"Result: {result}")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    matha_repl()