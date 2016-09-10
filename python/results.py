class ParserResult:
    def __init__(self):
        self.failed = False
        self.errorMessage = ""
        self.result = ""
    def failure(self, msg):
        self.errorMessage = msg
        self.failed = True
    def setResult(self, res):
        self.result = res