from dataclasses import dataclass
 
@dataclass
class ColorPair:
    major_color: str
    minor_color: str
 
    def __str__(self):
        return f"MajorColor: {self.major_color}, MinorColor: {self.minor_color}"
