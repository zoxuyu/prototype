class Parser:
    def __init__(self):
        self.commandList = ["Read", "Write"]
    def HasCommand(self, cmd):
        return False
    def ExexuteCommand(self, cmd, args, ParserResult):
        res = ParserResult()
        return res