from pudding_data import Function, Data, DataType, StringData, NUMBERS
import math

# System and basic IO

class ExitFunction(Function):

    def __init__(self):
        super().__init__(arg_names=[], function=None)

    def execute(self, intepreter, tree):
        exit()

class PrintFunction(Function):

    def __init__(self):
        super().__init__(arg_names=['<message>'], function=None)

    def execute(self, intepreter, tree):
        self.populate_args(intepreter, tree)
        message = str(self.lookup_symbol_table(intepreter, self.arg_names[0]))
        print(message)

class InputFunction(Function):

    def __init__(self):
        super().__init__(arg_names=['<prompt>'], function=None)

    def execute(self, intepreter, tree):
        self.populate_args(intepreter, tree)
        prompt = self.lookup_symbol_table(intepreter, self.arg_names[0]).value
        return StringData(input(prompt))

# Typing
class TypeFunction(Function):

    def __init__(self):
        super().__init__(arg_names=['<value>'], function=None)

    def execute(self, intepreter, tree):
        self.populate_args(intepreter, tree)
        data = self.lookup_symbol_table(intepreter, self.arg_names[0])
        return Data(DataType.TYPE, data.type)
    
class ToIntFunction(Function):

    def __init__(self):
        super().__init__(arg_names=['<x>'], function=None)

    def execute(self, intepreter, tree):
        self.populate_args(intepreter, tree)
        data = self.lookup_symbol_table(intepreter, self.arg_names[0])
        return Data(DataType.INTEGER, int(data.value))
    
class ToFloatFunction(Function):

    def __init__(self):
        super().__init__(arg_names=['<x>'], function=None)

    def execute(self, intepreter, tree):
        self.populate_args(intepreter, tree)
        data = self.lookup_symbol_table(intepreter, self.arg_names[0])
        return Data(DataType.FLOAT, float(data.value))
    
class ToStrFunction(Function):

    def __init__(self):
        super().__init__(arg_names=['<x>'], function=None)

    def execute(self, intepreter, tree):
        self.populate_args(intepreter, tree)
        data = self.lookup_symbol_table(intepreter, self.arg_names[0])
        return StringData(str(data.value))

# Numbers

class FloorFunction(Function):

    def __init__(self):
        super().__init__(arg_names=['<x>'], function=None)

    def execute(self, intepreter, tree):
        self.populate_args(intepreter, tree)
        x = self.lookup_symbol_table(intepreter, self.arg_names[0])
        if x.type != DataType.FLOAT and x.type != DataType.INTEGER:
            print('type error: expecting numeric value (integer or float)')
            exit()

        return Data(DataType.INTEGER, int(x.value))
    
class CeilingFunction(Function):

    def __init__(self):
        super().__init__(arg_names=['<x>'], function=None)

    def execute(self, intepreter, tree):
        self.populate_args(intepreter, tree)
        x = self.lookup_symbol_table(intepreter, self.arg_names[0])
        if x.type != DataType.FLOAT and x.type != DataType.INTEGER:
            print('type error: expecting numeric value (integer or float)')
            exit()

        return Data(DataType.INTEGER, int(math.ceil(x.value)))

BuiltinFunctions = {
    'exit' : ExitFunction(),
    'print': PrintFunction(),
    'input': InputFunction(),
    'floor': FloorFunction(),
    'ceil' : CeilingFunction(),
    'type': TypeFunction(),
    'to_int': ToIntFunction(),
    'to_float': ToIntFunction(),
    'to_str': ToStrFunction(),
}