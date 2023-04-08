import sys
from pudding_parser import PuddingParser
from pudding_interpreter import PuddingInterpreter
from pudding_builtins import BuiltinFunctions

def main():

    grammar_definition = "grammar_definition.txt"
    parser = PuddingParser(grammar_definition, "program")
    interpreter = PuddingInterpreter()

    # Loading source code
    source_code_file = open(sys.argv[1], 'r')
    source_code = source_code_file.read()
    source_code_file.close()

    # Linking libraries
    for key, value in BuiltinFunctions.items():
        interpreter.symbol_table.insert_global(key, value)

    print(">>> Parsing code...")
    parse_tree = parser.parse(source_code)
    
    if parse_tree:
        
        # print(parse_tree.pretty())

        print(">>> Running code...\n")
        result = interpreter.visit(parse_tree)

if __name__ == "__main__":
    main()