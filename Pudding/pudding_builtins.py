from pudding_data import Function, Data, DataType, StringData,ListData, NUMBERS, ITERABLES
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

# Math
class FloorFunction(Function):

    def __init__(self):
        super().__init__(arg_names=['<x>'], function=None)

    def execute(self, intepreter, tree):
        self.populate_args(intepreter, tree)
        x = self.lookup_symbol_table(intepreter, self.arg_names[0])
        if x.type not in NUMBERS:
            print('type error: expecting numeric value (integer or float)')
            exit()

        return Data(DataType.INTEGER, int(x.value))
    
class CeilingFunction(Function):

    def __init__(self):
        super().__init__(arg_names=['<x>'], function=None)

    def execute(self, intepreter, tree):
        self.populate_args(intepreter, tree)
        x = self.lookup_symbol_table(intepreter, self.arg_names[0])
        if x.type not in NUMBERS:
            print('type error: expecting numeric value (integer or float)')
            exit()

        return Data(DataType.INTEGER, int(math.ceil(x.value)))
    
class SqrtFunction(Function):

    def __init__(self):
        super().__init__(arg_names=['<x>'], function=None)

    def execute(self, intepreter, tree):
        self.populate_args(intepreter, tree)
        x = self.lookup_symbol_table(intepreter, self.arg_names[0])
        if x.type not in NUMBERS:
            print('type error: expecting numeric value (integer or float)')
            exit()

        return Data(DataType.FLOAT, math.sqrt(x.value))
    
class SinFunction(Function):

    def __init__(self):
        super().__init__(arg_names=['<x>'], function=None)

    def execute(self, intepreter, tree):
        self.populate_args(intepreter, tree)
        x = self.lookup_symbol_table(intepreter, self.arg_names[0])
        if x.type not in NUMBERS:
            print('type error: expecting numeric value (integer or float)')
            exit()

        return Data(DataType.FLOAT, math.sin(x.value))
    
class CosFunction(Function):

    def __init__(self):
        super().__init__(arg_names=['<x>'], function=None)

    def execute(self, intepreter, tree):
        self.populate_args(intepreter, tree)
        x = self.lookup_symbol_table(intepreter, self.arg_names[0])
        if x.type not in NUMBERS:
            print('type error: expecting numeric value (integer or float)')
            exit()

        return Data(DataType.FLOAT, math.cos(x.value))
    
class TanFunction(Function):

    def __init__(self):
        super().__init__(arg_names=['<x>'], function=None)

    def execute(self, intepreter, tree):
        self.populate_args(intepreter, tree)
        x = self.lookup_symbol_table(intepreter, self.arg_names[0])
        if x.type not in NUMBERS:
            print('type error: expecting numeric value (integer or float)')
            exit()

        return Data(DataType.FLOAT, math.tan(x.value))
    
class AsinFunction(Function):

    def __init__(self):
        super().__init__(arg_names=['<x>'], function=None)

    def execute(self, intepreter, tree):
        self.populate_args(intepreter, tree)
        x = self.lookup_symbol_table(intepreter, self.arg_names[0])
        if x.type not in NUMBERS:
            print('type error: expecting numeric value (integer or float)')
            exit()

        return Data(DataType.FLOAT, math.asin(x.value))
    
class AcosFunction(Function):

    def __init__(self):
        super().__init__(arg_names=['<x>'], function=None)

    def execute(self, intepreter, tree):
        self.populate_args(intepreter, tree)
        x = self.lookup_symbol_table(intepreter, self.arg_names[0])
        if x.type not in NUMBERS:
            print('type error: expecting numeric value (integer or float)')
            exit()

        return Data(DataType.FLOAT, math.acos(x.value))
    
class AtanFunction(Function):

    def __init__(self):
        super().__init__(arg_names=['<x>'], function=None)

    def execute(self, intepreter, tree):
        self.populate_args(intepreter, tree)
        x = self.lookup_symbol_table(intepreter, self.arg_names[0])
        if x.type not in NUMBERS:
            print('type error: expecting numeric value (integer or float)')
            exit()

        return Data(DataType.FLOAT, math.atan(x.value))
    
class LogFunction(Function):

    def __init__(self):
        super().__init__(arg_names=['<x>', '<base>'], function=None)

    def execute(self, intepreter, tree):
        self.populate_args(intepreter, tree)
        x = self.lookup_symbol_table(intepreter, self.arg_names[0])
        base = self.lookup_symbol_table(intepreter, self.arg_names[1])
        if x.type not in NUMBERS or base.type not in NUMBERS:
            print('type error: expecting numeric value (integer or float)')
            exit()

        return Data(DataType.FLOAT, math.log(x.value, base.value))
    
# Strings and lists
class LenFunction(Function):

    def __init__(self):
        super().__init__(arg_names=['<x>'], function=None)

    def execute(self, intepreter, tree):
        self.populate_args(intepreter, tree)
        x = self.lookup_symbol_table(intepreter, self.arg_names[0])
        if x.type not in ITERABLES:
            print('type error: expecting iterables (string or list)')
            exit()

        return Data(DataType.INTEGER, len(x.value))

class ConcatFunction(Function):

    def __init__(self):
        super().__init__(arg_names=['<x>', '<y>'], function=None)

    def execute(self, intepreter, tree):
        self.populate_args(intepreter, tree)
        x = self.lookup_symbol_table(intepreter, self.arg_names[0])
        y = self.lookup_symbol_table(intepreter, self.arg_names[1])
        if x.type != DataType.LIST or y.type != DataType.LIST:
            print('type error: expecting lists')
            exit()

        return ListData(x.value+y.value)

class SliceFunction(Function):

    def __init__(self):
        super().__init__(arg_names=['<source>', '<begin>', 'end'], function=None)

    def execute(self, intepreter, tree):
        self.populate_args(intepreter, tree)
        source = self.lookup_symbol_table(intepreter, self.arg_names[0])
        begin = self.lookup_symbol_table(intepreter, self.arg_names[1])
        end = self.lookup_symbol_table(intepreter, self.arg_names[2])

        if source.type not in ITERABLES:
            print('type error: expecting iterables (string or list)')
            exit()
        
        if begin.type != DataType.INTEGER or end.type != DataType.INTEGER:
            print('type error: slice function indexes must be integers')
            exit()

        if source.type == DataType.LIST:
            return ListData(source.value[begin.value:end.value])
        
        if source.type == DataType.STRING:
            return StringData(source.value[begin.value:end.value])

BuiltinFunctions = {
    'exit' : ExitFunction(),
    'print': PrintFunction(),
    'input': InputFunction(),
    'floor': FloorFunction(),
    'ceil' : CeilingFunction(),
    'sqrt' : SqrtFunction(),
    'sin' : SinFunction(),
    'cos' : CosFunction(),
    'tan' : TanFunction(),
    'asin' : AsinFunction(),
    'acos' : AcosFunction(),
    'atan' : AtanFunction(),
    'log' : LogFunction(),
    'type': TypeFunction(),
    'to_int': ToIntFunction(),
    'to_float': ToIntFunction(),
    'to_str': ToStrFunction(),
    'len' : LenFunction(),
    'concat' : ConcatFunction(),
    'slice' : SliceFunction(),
}