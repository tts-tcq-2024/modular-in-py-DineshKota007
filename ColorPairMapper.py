from ColorMapping import ColorMapping
from ColorPair import ColorPair
from ColorPairMapperBase import ColorPairMapperBase
 
class ColorPairMapper(ColorPairMapperBase):
    def map_number_to_color_pair(self, pair_number: int) -> ColorPair:
        """Convert pair number to a ColorPair."""
        self.ensure_valid_pair_number(pair_number)
        minor_index = (pair_number - 1) % len(ColorMapping.MINOR_COLORS)
        major_index = (pair_number - 1) // len(ColorMapping.MINOR_COLORS)
        return ColorPair(
            major_color=ColorMapping.MAJOR_COLORS[major_index],
            minor_color=ColorMapping.MINOR_COLORS[minor_index]
        )
 
    def map_color_pair_to_number(self, pair: ColorPair) -> int:
        """Convert ColorPair to a pair number."""
        major_index = ColorMapping.get_color_index(pair.major_color, ColorMapping.MAJOR_COLORS)
        minor_index = ColorMapping.get_color_index(pair.minor_color, ColorMapping.MINOR_COLORS)
        return (major_index * len(ColorMapping.MINOR_COLORS)) + (minor_index + 1)
