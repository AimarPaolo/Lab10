import string
from dataclasses import dataclass

@dataclass
class Contiguity:
    dyad: int
    state1no: int
    state1ab: string
    state2no: int
    state2ab: string
    year: int
    conttype: int
    version: int

    def __hash__(self):
        return hash((self.state1no, self.state2no))

    def __eq__(self, other):
        return self.state1no == other.state1no and self.state2no == other.state2no

    def __str__(self):
        return f"{self.state1no}{self.state2no}{self.year}"
