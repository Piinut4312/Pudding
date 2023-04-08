from lark import Lark
from lark.indenter import Indenter

class PuddingIndenter(Indenter):
    NL_type = '_NL'
    OPEN_PAREN_types = []
    CLOSE_PAREN_types = []
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 4

class PuddingParser:

    # A simple parser powered by Lark
    # The grammar rules are defined in a text file, written in Lark's specified format

    def __init__(self, grammar_file_path, start_symbol):
        grammar_definition_file = open(grammar_file_path, 'r')
        grammar_string = grammar_definition_file.read()
        grammar_definition_file.close()
        self.parser = Lark(grammar_string, start=start_symbol, postlex=PuddingIndenter())
        

    def parse(self, source_code):

        # Generates a parse tree from a string
        # If an error occur while parsing, then it returns None
        try:
            parse_tree = self.parser.parse(source_code)
            return parse_tree
        except Exception as e:
            print(e)
            return None
