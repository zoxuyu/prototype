class Parser:
    def __init__(self):
        self.commandList = ["Read", "Write"]
    def HasCommand(self, cmd):
        return cmd in self.commandList
    def ExexuteCommand(self, cmd, args, ParserResult):
        res = ParserResult()
        if cmd == "Read":
            if len(args) == 0:
                try:
                    res.setResult(raw_input())
                except:
                    try:
                        res.setResult(input())
                    except:
                        res.failure("Input request failed. Maybe an invalid character had been specified.")
            elif len(args) == 1:
                try:
                    res.setResult(raw_input(args[0]))
                except:
                    try:
                        res.setResult(input(args[0]))
                    except:
                        res.failure("Input request failed. Maybe an invalid character had been specified.")
            else:
                res.failure("Read{} expects exactly zero or one arguments.")
        elif cmd == "Write":
            if len(args) == 1:
                try:
                    print(args[0])
                except:
                    res.failure("Output failed. Maybe an invalid character had been specified.")
            else:
                res.failure("Write{} expects exactly one argument .")
        return res