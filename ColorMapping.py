from typing import List, Tuple
 
class ColorMapping:
    # Define major and minor colors
    MAJOR_COLORS: List[str] = ['White', 'Red', 'Black', 'Yellow', 'Violet']
    MINOR_COLORS: List[str] = ['Blue', 'Orange', 'Green', 'Brown', 'SlateGray']
 
    @staticmethod
    def get_color_index(color: str, color_list: List[str]) -> int:
        """Find the index of the color in the provided color list."""
        try:
            return color_list.index(color)
        except ValueError:
            raise ValueError(f"Unknown color: {color}")
