from abc import ABC, abstractmethod
 
class ColorPairMapperBase(ABC):
    @abstractmethod
    def map_number_to_color_pair(self, pair_number: int) -> 'ColorPair':
        """Map a pair number to a ColorPair."""
        pass
 
    @abstractmethod
    def map_color_pair_to_number(self, pair: 'ColorPair') -> int:
        """Map a ColorPair to a pair number."""
        pass
 
    @staticmethod
    def ensure_valid_pair_number(pair_number: int) -> None:
        """Ensure that the pair number is within valid range."""
        max_pair_number = len(ColorMapping.MAJOR_COLORS) * len(ColorMapping.MINOR_COLORS)
        if not (1 <= pair_number <= max_pair_number):
            raise ValueError(f"PairNumber: {pair_number} is outside the allowed range of 1 to {max_pair_number}")
