class HelloWorld:

    def __init__(self, name: str):
        self.name = name

    def print_info(self):
        print(f"HELLO: {self.name}")

    def updated_info(self, suffix: str):
        self.name = f"{self.name} {suffix}!"
        print(f"HELLO: {self.name}")