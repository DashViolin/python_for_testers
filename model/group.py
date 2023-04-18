from dataclasses import dataclass


@dataclass
class Group:
    name: str
    header: str
    footer: str


class OldGroup:
    def __init__(self, name, header, footer):
        self.name = name
        self.header = header
        self.footer = footer
