class OperationError(Exception):
    def __init__(self, name: str, massage: str):
        self.name = name
        self.massage = massage