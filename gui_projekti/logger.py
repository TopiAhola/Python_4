


class Logger:
    level :int
    do_logging : bool
    name : str


    def __init__(self, name):
        self.level = 0
        self.do_logging = True
        self.name = name


    def log(self, message):
        if self.do_logging:
            print(message)


    def toggle_logger(self):
        self.do_logging = not self.do_logging