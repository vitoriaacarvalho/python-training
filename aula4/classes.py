class Writer:
    def __init__(self,name):
        self.__name=name
        self.__tool=None
    @property
    def name(self):
        return self.__name
    @property
    def tool(self):
        return self.__tool

    @tool.setter
    def tool(self,value):
        self.__tool=value


class Pen:
    def __init__(self, type):
        self.__type=type
    @property
    def type(self):
        return self.__type

    def write(self):
        print('the pen is writing')


class WritingMachine:
    def write(self):
        print('the machine is writing')