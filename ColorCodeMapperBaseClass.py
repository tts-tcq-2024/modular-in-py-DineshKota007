class ColorCodeMapperBase:
    color_map_major = ["White", "Red", "Black", "Yellow", "Violet"]
    color_map_minor = ["Blue", "Orange", "Green", "Brown", "SlateGray"]
 
    def get_color_index(self, color_map, color):
        try:
            return color_map.index(color)
        except ValueError:
            return -1
 
    def validate_color_indices(self, major_index, minor_index, color_pair):
        if major_index == -1 or minor_index == -1:
            raise ValueError(f"Unknown Colors: {color_pair}")
