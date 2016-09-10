from results import *
import sys
class Engine:
    def __init__(self, filename, parser_list):
        f = open(filename, "r")
        self.code = f.readlines()
        f.close()
        self.parser_list = parser_list
        self.in_program = False
        self.had_program = False
        self.availible_parsers = {}
    def getLines(self):
        return self.code
    def parseLine(self, line):
        res = ParserResult()
        if self.in_program:
            line = line.strip()
            for parser_ in self.availible_parsers.keys():
                parser = self.availible_parsers[parser_]
                if parser.HasCommand("Write"):
                    return parser.ExexuteCommand("Write", ["Hello World!"], ParserResult)
            res.failure("Command not found")
            return res
        elif line.startswith("#! "):
            parser = line.lstrip("#")
            parser = parser.lstrip("!")
            parser = parser.strip()
            if parser in self.parser_list.keys():
                self.availible_parsers[parser] = self.parser_list[parser]()
                return res
            else:
                res.failure("Parser not found")
                return res
        elif line.strip().startswith("Program \"") and line.strip().endswith("\""):
            for i in [" ", "\t"]:
                if line.startswith(i):
                    raise Exception("Keyword Program may not be indented")
                    sys.exit(1)
            for i in "Program \"":
                line = line.lstrip(i)
            for i in "\"":
                line = line.rstrip(i)
            if 
        else:
            res.failure("Command not found")
            return res
        return res