from results import *
import sys, re
class Engine:
    def __init__(self, filename, parser_list):
        f = open(filename, "r")
        self.code = f.readlines()
        f.close()
        self.parser_list = parser_list
        self.in_program = False
        self.had_program = False
        self.availible_parsers = {}
        self.vars =  {}
        self.n = 0
    def getLines(self):
        return self.code
    def parseLine(self, line):
        res = ParserResult()
        if line.startswith("?"): 
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
            line = line.strip()
            for i in "Program ":
                line = line.lstrip(i)
            for i in "\"":
                line = line.strip(i)
            if "\"" in line:
                print line
                raise Exception("Invalid Syntax")
            if not self.had_program:
                self.had_program = self.in_program = True
            else:
                raise Exception("Only One program per file")
        elif line.strip() == "EndProgram":
            if self.had_program and self.in_program:
                self.in_program = True
            else:
                raise Exception("Unopened program")
        elif self.in_program:
            line = line.strip()
            line = self.tokenize(line)
            cmd = line["cmd"]
            args = line["args"]
            for parser_ in self.availible_parsers.keys():
                parser = self.availible_parsers[parser_]
                if parser.HasCommand(cmd):
                    return parser.ExexuteCommand(cmd, args, ParserResult)
            res.failure("Command not found")
            return res
        else:
            res.failure("Command not found")
            return res
        self.n += 1
        if self.n == len(self.code):
            if self.in_program:
                raise Exception("Unclosed program")
        return res
    def tokenize(self, line):
        if False:
            # Here will be the code for variable-Adding
            pass
        else:
            rexp = re.compile("|^([a-zA-Z0-9_-]*?) \{(.*?)\}$|")
            line_ = rexp.split(line)[0]
            cmd = line_.split(" ")[0]
            cmd = cmd.strip()
            args = " ".join(line_.split(" ")[1:]).strip()
            args = args.strip("{}")
            args = [i.strip() for i in args.split(",")]
            for i in range(len(args)):
                if args[i] == "": continue
                if args[i].startswith('\"') and args[i].endswith('\"'):
                    args[i] = args[i].strip('\"')
                    args[i] = args[i].replace("\\n", "\n")
                    args[i] = args[i].replace("\\t", "\t")
                elif args[i].startswith("\'") and args[i].endswith("\'"):
                    args[i] = args[i].strip("\'")
                    args[i] = args[i].replace("\\n", "\n")
                    args[i] = args[i].replace("\\t", "\t")
                else:
                    try:
                        args[i] = eval(args[i])
                    except: pass
        return {"cmd":cmd, "args":args}