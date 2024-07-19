from ColorCodeMapperBase import ColorCodeMapperBase
from ClolorPair import ColorPair
class ColorToPairNumberMapper(ColorCodeMapperBase):
    def get_pair_number_from_color(self, color_pair):
        major_index = self.get_color_index(self.color_map_major, color_pair.major_color)
        minor_index = self.get_color_index(self.color_map_minor, color_pair.minor_color)
        self.validate_color_indices(major_index, minor_index, color_pair)
        return (major_index * len(self.color_map_minor)) + (minor_index + 1)
