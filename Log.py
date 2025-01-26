from colorama import Fore, Back, Style
class Log:
    TAG = ""
    COLOR = None
    def __init__(self, tag, color):
        self.TAG = tag
        self.COLOR = self.color_parse(color)


    def color_parse(self, color):
        if color == "red":
            return Fore.RED
        elif color == "white":
            return Fore.WHITE
        elif color == "lightred":
            return Fore.LIGHTRED_EX
        elif color == "yellow":
            return Fore.YELLOW
        elif color == "green":
            return Fore.GREEN
        elif color == "blue":
            return Fore.BLUE
        elif color == "cyan":
            return Fore.CYAN
        elif color == "morph":
            return Fore.BLACK + Back.RED

    def print(self, msg):
        print(self.COLOR + self.TAG + " " + str(msg) + Style.RESET_ALL)