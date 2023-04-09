from enum import Enum, auto

class DataType(Enum):
    NONE = auto()
    TYPE = auto()
    BOOLEAN  = auto()
    INTEGER = auto()
    FLOAT = auto()
    STRING = auto()
    LIST = auto()
    FUNCTION = auto()

NUMBERS = (DataType.INTEGER, DataType.FLOAT)
ITERABLES = (DataType.STRING, DataType.LIST)

class Data:

    def __init__(self, type: DataType, value):
        self.type = type
        self.value = value

    def __repr__(self) -> str:
        return str(self.value)
    

class StringData(Data):

    def __init__(self, value):
        super().__init__(DataType.STRING, value)

    def __repr__(self) -> str:
        return '"'+self.value+'"'
    
    def __str__(self) -> str:
        return self.value
    
    
class ListData(Data):

    def __init__(self, value):
        super().__init__(DataType.LIST, value)

    def __repr__(self) -> str:
        return str(self.value)
    
    
class Function:

    def __init__(self, arg_names, function=None):
        self.arg_names = arg_names
        self.function = function
    
    def populate_args(self, intepreter, tree):
        for i in range(1, len(tree.children)):
            arg_value = intepreter.visit(tree.children[i])
            intepreter.symbol_table.insert_current(self.arg_names[i-1], arg_value)

    def lookup_symbol_table(self, intepreter, symbol):
        return intepreter.symbol_table.lookup(symbol)
    
    def insert_symbol_table(self, intepreter, symbol, value):
        intepreter.symbol_table.insert(symbol, value)

    def execute(self, intepreter, tree):
        self.populate_args(intepreter, tree)
        return intepreter.visit(self.function)

    
def get_dominant_type(v1, v2):
    i1 = (v1.type == DataType.INTEGER)
    i2 = (v2.type == DataType.INTEGER)
    f1 = (v1.type == DataType.FLOAT)
    f2 = (v2.type == DataType.FLOAT)

    if i1 and i2:
        return DataType.INTEGER
    elif (i1 and f2) or (f1 and i2) or (f1 and f2):
        return DataType.FLOAT
        
    return None