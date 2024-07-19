class PairNumberToColorMapper(ColorCodeMapperBase):
    def get_color_from_pair_number(self, pair_number):
        self.validate_pair_number(pair_number)
        major_index, minor_index = self.get_indices_from_pair_number(pair_number)
        return ColorPair(self.color_map_major[major_index], self.color_map_minor[minor_index])
 
    def validate_pair_number(self, pair_number):
        if pair_number < 1 or pair_number > len(self.color_map_major) * len(self.color_map_minor):
            raise ValueError(f"PairNumber {pair_number} is outside the allowed range")
 
    def get_indices_from_pair_number(self, pair_number):
        zero_based_pair_number = pair_number - 1
        major_index = zero_based_pair_number // len(self.color_map_minor)
        minor_index = zero_based_pair_number % len(self.color_map_minor)
        return major_index, minor_index
