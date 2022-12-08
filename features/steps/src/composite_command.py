from steps.src.command import Command


class CompositeCommand(Command, list):
    def __init__(self, items=[]):
        super().__init__()
        for i in items:
            self.append(i)

    def execute(self) -> None:
        for x in self:
            x.execute()
