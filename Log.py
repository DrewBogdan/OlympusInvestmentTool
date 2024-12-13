class Log:
    TAG = ""

    def __init__(self, tag):
        self.TAG = tag

    def print(self, msg):
        print(self.TAG + " " + msg)