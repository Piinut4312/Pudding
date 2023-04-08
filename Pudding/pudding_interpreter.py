import math
import operator
from lark.visitors import Interpreter
from pudding_data import Data, DataType, NUMBERS, get_dominant_type, Function, ListData, StringData


COMP_OP = {"gt": operator.gt, "ge":operator.ge, "lt": operator.lt, "le": operator.le, "equ": operator.eq}

class SymbolTable:

    # Symbol table stores information about the symbols (e.g. variable and function names)

    def __init__(self, scope_name, parent=None):
        self.__symbol_table = dict()
        self.scope_name = scope_name
        self.parent = parent

    def insert(self, symbol, value):
        self.__symbol_table[symbol] = value

    def lookup(self, symbol):
        if symbol in self.__symbol_table.keys():
            return self.__symbol_table[symbol]
        return None
    
    def __str__(self):
        return self.scope_name


class ScopedSymbolTables:

    # A symbol table stack that implements scoping

    def __init__(self):
        self.root = SymbolTable('global', parent=None)
        self.current_scope = self.root
    
    def insert(self, symbol, value):
        """
        Attempt to insert symbol and value.
        If the attempt fails in current scope, try again in parent scope.
        If all attempt fails, create a new symbol-value mapping in current scope.
        """
        search_scope = self.current_scope
        while search_scope is not None:
            lookup_result = search_scope.lookup(symbol)
            if lookup_result is not None:
                search_scope.insert(symbol, value)
                return
            search_scope = search_scope.parent
        
        self.current_scope.insert(symbol, value)
        
    def insert_current(self, symbol, value):
        self.current_scope.insert(symbol, value)

    def insert_global(self, symbol, value):
        self.root.insert(symbol, value)

    def lookup(self, symbol):
        search_scope = self.current_scope
        while search_scope is not None:
            
            lookup_result = search_scope.lookup(symbol)
            if lookup_result is not None:
                return lookup_result
                
            search_scope = search_scope.parent
        
        return None

    def open_scope(self, scope_name):
        self.current_scope = SymbolTable(scope_name, parent=self.current_scope)

    def close_scope(self):
        self.current_scope = self.current_scope.parent

    def get_scope_name(self):
        return self.current_scope.scope_name
    

class PuddingInterpreter(Interpreter):

    def __init__(self):
        Interpreter.__init__(self)
        self.symbol_table = ScopedSymbolTables()

    def program(self, tree):
        self.visit_children(tree)
        return None

    def block(self, tree):
        for child in tree.children:
            return_value = self.visit(child)
            if return_value is not None:
                return return_value
        return None

    # Primary data types
    def integer(self, tree):
        return Data(DataType.INTEGER, int(tree.children[0]))

    def float(self, tree):
        return Data(DataType.FLOAT, float(tree.children[0]))

    def boolean(self, tree):
        value_string = tree.children[0]
        if value_string == "true":
            return Data(DataType.BOOLEAN, True)
        elif value_string == "false":
            return Data(DataType.BOOLEAN, False)
        return None
        
    def string(self, tree):
        return StringData(str(tree.children[0])[1:-1])
    
    def array(self, tree):
        x = ListData(self.visit_children(tree))
        return x

    # Numerical binary operations
    def add(self, tree):
        args = self.visit_children(tree)
        final_type = get_dominant_type(args[0], args[1])
        
        if final_type is not None:
            return Data(final_type, args[0].value+args[1].value)

        print("type error")
        exit()

    def sub(self, tree):
        args = self.visit_children(tree)
        final_type = get_dominant_type(args[0], args[1])
        
        if final_type is not None:
            return Data(final_type, args[0].value-args[1].value)

        print("type error")
        exit()

    def mult(self, tree):
        args = self.visit_children(tree)
        final_type = get_dominant_type(args[0], args[1])
        
        if final_type is not None:
            return Data(final_type, args[0].value*args[1].value)

        print("type error")
        exit()

    def div(self, tree):
        args = self.visit_children(tree)
        
        if args[0].type not in NUMBERS or args[1].type not in NUMBERS:
            print("type error")
            exit()

        if args[1].value == 0:
            print('divide by zero error')
            exit()

        return Data(DataType.FLOAT, args[0].value/args[1].value)

    def mod(self, tree):
        args = self.visit_children(tree)
        
        if args[0].type == DataType.INTEGER and args[1].type == DataType.INTEGER:
            if args[1].value == 0:
                print("modulo by zero error")
                exit()
            return Data(DataType.INTEGER, args[0].value%args[1].value)

        print("type error(modulo)")
        exit()
        
    def exponents(self, tree):
        args = self.visit_children(tree)
        final_type = get_dominant_type(args[0], args[1])
        
        if final_type is not None:
            return Data(final_type, args[0].value**args[1].value)

        print("type error")
        exit()

    # Numerical unary operations
    def neg(self, tree):
        arg = self.visit(tree.children[0])
        if arg.type in NUMBERS:
            return Data(arg.type, -arg.value)

        print("type error")
        exit()

    def abs(self, tree):
        arg = self.visit_children(tree)[0]

        if arg.type in NUMBERS:
            return Data(arg.type, abs(arg.value))

        print("type error")
        exit()

    def factorial(self, tree):
        arg = self.visit_children(tree)[0]

        if arg.type == DataType.INTEGER and arg.value >= 0:
            return Data(DataType.INTEGER, math.factorial(arg.value))

        print("type error")
        exit()

    # Boolean binary operations
    def logic_and(self, tree):
        args = self.visit_children(tree)

        if args[0].type == DataType.BOOLEAN and args[1].type == DataType.BOOLEAN:
            return Data(DataType.BOOLEAN, (args[0].value and args[1].value))

        print("type error")
        exit()

    def logic_or(self, tree):
        args = self.visit_children(tree)

        if args[0].type == DataType.BOOLEAN and args[1].type == DataType.BOOLEAN:
            return Data(DataType.BOOLEAN, (args[0].value or args[1].value))

        print("type error")
        exit()

    def logic_xor(self, tree):
        args = self.visit_children(tree)

        if args[0].type == DataType.BOOLEAN and args[1].type == DataType.BOOLEAN:
            return Data(DataType.BOOLEAN, (args[0].value != args[1].value))

        print("type error")
        exit()

    # Boolean unary operations
    def logic_not(self, tree):
        arg = self.visit_children(tree)[0]

        if arg.type == DataType.BOOLEAN :
            return Data(DataType.BOOLEAN, not arg.value)

        print("type error")
        exit()

    # String operations
    def str_join(self, tree):
        str1 = self.visit(tree.children[0])
        str2 = self.visit(tree.children[1])
        return Data(DataType.STRING, str1.value+str2.value)
    
    # Array operations
    def array_lookup(self, tree):
        id, lookup = self.visit(tree.children[0])
        indexes = [self.visit(tree.children[i]) for i in range(1, len(tree.children))]
        array_slice = lookup
        for i in indexes:
            if i.type != DataType.INTEGER:
                print('index error: array index must be integers')
                exit()
            if not isinstance(array_slice.value, list):
                print('type error: [] only supports lists')
                exit()
            array_slice = array_slice.value[i.value]
        
        if isinstance(array_slice, list):
            return ListData(array_slice)
        else:
            return array_slice

    # Comparison
    def compare(self, tree):
        args = self.visit_children(tree)
        conditions = [tree.children[i].data.value for i in range(1, len(args))]
        for i in range(len(conditions)):
            op = COMP_OP[conditions[i]]
            if not op(args[i].value, args[i+1].value):
                return Data(DataType.BOOLEAN, False)
        
        return Data(DataType.BOOLEAN, True)

    lt = lambda self, tree : self.visit_children(tree)[0]
    le = lambda self, tree : self.visit_children(tree)[0]
    gt = lambda self, tree : self.visit_children(tree)[0]
    ge = lambda self, tree : self.visit_children(tree)[0]
    equ = lambda self, tree : self.visit_children(tree)[0]
    
    # Variable assignment and lookup
    def identifier(self, tree):
        id = tree.children[0].value
        lookup = self.symbol_table.lookup(id)
        return id, lookup
    
    def variable(self, tree):
        id, lookup = self.visit_children(tree)[0]
        if lookup is None:
            print("undeclared variable error: unknown identifier '{}'".format(id))
            exit()
        return lookup

    def container(self, tree):
        id, lookup = self.visit_children(tree)[0]
        return id

    def put_value(self, tree):
        value = self.visit(tree.children[0])
        id = self.visit(tree.children[1])
        if len(tree.children) > 2:
            addr = self.visit(tree.children[2])
            array_slice = self.symbol_table.lookup(id)
            for i in range(len(addr)-1):
                if not isinstance(array_slice.value, list):
                    print('type error: [] only supports lists')
                    exit()
                array_slice = array_slice.value[addr[i]]
            if not isinstance(array_slice.value, list):
                print('type error: [] only supports lists')
                exit()
            array_slice.value[addr[-1]] = value
        else:
            self.symbol_table.insert(id, value)

        return None
    
    def address(self, tree):
        addr = self.visit_children(tree)
        for x in addr:
            if x.type != DataType.INTEGER:
                print('index error: array index must be integers')
                exit()
        return [x.value for x in addr]
            
    # If statement
    def if_stmt(self, tree):
        condition = self.visit(tree.children[0])
        if condition.value:
            p = self.visit(tree.children[1])
            return p
        else:
            for branch in tree.children[2:]:
                stop, returned = self.visit(branch)
                if stop:
                    return returned
        return None

    def elif_stmt(self, tree):
        condition = self.visit(tree.children[0])
        if condition.value:
            return True, self.visit(tree.children[1])
        return False, None

    def else_stmt(self, tree):
        return True, self.visit(tree.children[0])
                
    # For statements
    def loop_stmt(self, tree):
        container = self.visit(tree.children[0])
        lowerbound = self.visit(tree.children[1]).value
        upperbound = self.visit(tree.children[2]).value
        loop_body = tree.children[3]

        self.symbol_table.open_scope("loop_statement")
        for i in range(lowerbound, upperbound+1):
            self.symbol_table.insert_current(container, Data(DataType.INTEGER, i))
            return_value = self.visit(loop_body)
            if return_value is not None:
                return return_value

        self.symbol_table.close_scope()
        return None

    # While statements
    def while_stmt(self, tree):
        loop_body = tree.children[1]
        self.symbol_table.open_scope("while_statement")
        while self.visit(tree.children[0]).value:
            return_value = self.visit(loop_body)
            if return_value is not None:
                return return_value
        return None

    # Functions
    def function_define(self, tree):
        id, lookup = self.visit(tree.children[0])
        self.symbol_table.insert_current(id, Function(arg_names=self.visit(tree.children[1]), function=tree.children[2]))
        return None
        
    def args(self, tree):
        arg_list = [self.visit(tree.children[i]) for i in range(len(tree.children))]
        return arg_list
    
    def function_call(self, tree):
        id, lookup = self.visit(tree.children[0])
        self.symbol_table.open_scope("function")
        return_value = lookup.execute(self, tree)
        self.symbol_table.close_scope()
        
        return return_value

    def function_return(self, tree):
        return_value = self.visit(tree.children[0])
        return return_value