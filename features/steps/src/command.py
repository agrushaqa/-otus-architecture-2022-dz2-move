from abc import ABC


class Command(ABC):
    def execute(self) -> None:
        pass


class CommandException(Exception):
    pass
