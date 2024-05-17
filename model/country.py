import string
from dataclasses import dataclass


@dataclass
class Country:
    StateAbb: str
    CCode: int
    StateNme: str

    def __hash__(self):
        return hash((self.CCode, self.StateAbb))

    @property
    def name(self):
        return self.StateNme

    def __lt__(self, other):
        return self.StateNme < other.StateNme
