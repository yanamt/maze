class generator:
    def __init__(self, size) -> None:
        self.size = size
        self.start_pos = 0, size-1

    def generate(self):
