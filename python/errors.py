"""
PROTOTYPE - errors.py

This is the errors file from the python implementation of the Prototype-Engine.
(C) Zoxuyu
"""
class PrototypeError:
    def __init__(self, description, file, line=None):
        self.filename = file
        self.description = description
        self.line = line
    def __str__(self):
        e = "\nSTOP!\n\n"
        e+= "======================================\n"
        e+= "AN ERROR OCCURED DURING THE EXECUTION\n"
        e+= "THIS PROTOTYPE-APPLICATION:\n\n"
        e+= "Error details:\n"
        e+= "---------------\n"
        e+= "file: " + self.filename + "\n"
        if self.line != None:
            e+= "line: " + str(self.line) + "\n"
        e+= "\n"
        e+= "The Application reports:\n"
        e+= "-------------------------\n"
        e+= self.description + "\n"
        e+= "======================================"
        return e
class PrototypeParserError:
    def __init__(self, description, file, line=None):
        self.filename = file
        self.description = description
        self.line = line
    def __str__(self):
        e = "\nSTOP!\n\n"
        e+= "======================================\n"
        e+= "AN PARSER ERROR OCCURED DURING THE\n"
        e+= "EXECUTION THIS PROTOTYPE-APPLICATION:\n\n"
        e+= "Error details:\n"
        e+= "---------------\n"
        e+= "file: " + self.filename + "\n"
        if self.line != None:
            e+= "line: " + str(self.line) + "\n"
        e+= "\n"
        e+= "The Parser reports:\n"
        e+= "-------------------------\n"
        e+= self.description + "\n"
        e+= "======================================"
        return e
class PrototypeSyntaxError:
    def __init__(self, description, file, line=None):
        self.filename = file
        self.description = description
        self.line = line
    def __str__(self):
        e = "\nSTOP!\n\n"
        e+= "======================================\n"
        e+= "AN SYNTAX ERROR OCCURED DURING THE\n"
        e+= "EXECUTION THIS PROTOTYPE-APPLICATION:\n\n"
        e+= "Error details:\n"
        e+= "---------------\n"
        e+= "file: " + self.filename + "\n"
        if self.line != None:
            e+= "line: " + str(self.line) + "\n"
        e+= "\n"
        e+= "The Engine reports:\n"
        e+= "-------------------------\n"
        e+= self.description + "\n"
        e+= "======================================"
        return e
class EngineError:
    def __init__(self, description, file, line=None):
        self.filename = file
        self.description = description
        self.line = line
    def __str__(self):
        e = "\nEngine-Error:\n"
        e+= "=================================================\n"
        e+= "|                                               |\n"
        e+= "|      ++++++++++++++++++++++++++++++++++++     |\n"
        e+= "|      + THE ENGINE HAS FAILED EXECUTION. +     |\n"
        e+= "|      + MAYBE YOU SPECIFIED A WRONG FILE +     |\n"
        e+= "|      + NAME.                            +     |\n"
        e+= "|      ++++++++++++++++++++++++++++++++++++     |\n"
        e+= "|                                               |\n"
        e+= "================================================="
        return e