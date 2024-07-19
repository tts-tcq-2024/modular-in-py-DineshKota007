class ColorPair:
    def __init__(self, major_color, minor_color):
        self.major_color = major_color
        self.minor_color = minor_color
 
    def __str__(self):
        return f"MajorColor: {self.major_color}, MinorColor: {self.minor_color}"
 
    def __eq__(self, other):
        return self.major_color == other.major_color and self.minor_color == other.minor_color
