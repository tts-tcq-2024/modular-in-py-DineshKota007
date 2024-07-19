from ColorPair import ColorPair
from ColorToPairNumberMapper import ColorToPairNumberMapper
from PairNumberToColorMapper import PairNumberToColorMapper
def run_tests(pair_number_to_color_mapper, color_to_pair_number_mapper):
    test_color_from_pair_number(pair_number_to_color_mapper, 4, "White", "Brown")
    test_color_from_pair_number(pair_number_to_color_mapper, 5, "White", "SlateGray")
    test_color_from_pair_number(pair_number_to_color_mapper, 23, "Violet", "Green")
    test_color_from_pair_number(pair_number_to_color_mapper, 1, "White", "Blue")
    test_color_from_pair_number(pair_number_to_color_mapper, 25, "Violet", "SlateGray")
    test_invalid_pair_number(pair_number_to_color_mapper, 0)
    test_invalid_pair_number(pair_number_to_color_mapper, 26)
 
    test_pair_number_from_color(color_to_pair_number_mapper, "Yellow", "Green", 18)
    test_pair_number_from_color(color_to_pair_number_mapper, "Red", "Blue", 6)
 
 
def test_color_from_pair_number(mapper, pair_number, expected_major, expected_minor):
    try:
        test_pair = mapper.get_color_from_pair_number(pair_number)
        print(f"[In] Pair Number: {pair_number}, [Out] Colors: {test_pair}")
        assert test_pair.major_color == expected_major
        assert test_pair.minor_color == expected_minor
    except Exception as e:
        print(f"Error: {e}")
 
 
def test_pair_number_from_color(mapper, major_color, minor_color, expected_pair_number):
    try:
        test_pair = ColorPair(major_color, minor_color)
        pair_number = mapper.get_pair_number_from_color(test_pair)
        print(f"[In] Colors: {test_pair}, [Out] Pair Number: {pair_number}")
        assert pair_number == expected_pair_number
    except Exception as e:
        print(f"Error: {e}")
 
 
def test_invalid_pair_number(mapper, pair_number):
    try:
        test_pair = mapper.get_color_from_pair_number(pair_number)
        print(f"[In] Pair Number: {pair_number}, [Out] Colors: {test_pair}")
    except ValueError:
        print(f"Passed: Pair number {pair_number} is out of range.")
    except Exception as e:
        print(f"Error: {e}")
 
 
if __name__ == "__main__":
    pair_number_to_color_mapper = PairNumberToColorMapper()
    color_to_pair_number_mapper = ColorToPairNumberMapper()
    run_tests(pair_number_to_color_mapper, color_to_pair_number_mapper)
