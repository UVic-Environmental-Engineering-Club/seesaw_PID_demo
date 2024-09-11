from . import pid

class HLCS:
    def __init__(self):
        self.target = 0
        self.initialize()

    def initialize(self):
        print("HLCS initialize")
