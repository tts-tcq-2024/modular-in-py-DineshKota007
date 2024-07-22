from ColorToPairNumberMapper import ColorToPairNumberMapper
from ColorPair import ColorPair
def ColorToPairNumberMapper():
    mapper = ColorToPairNumberMapper()
    ColorToPairNumberMapperTest(mapper, "Yellow", "Green", 18)
    ColorToPairNumberMapperTest(mapper, "Red", "Blue", 6)
 
def PairNumberToColorMapper(mapper, major_color, minor_color, expected_pair_number):
    try:
        test_pair = ColorPair(major_color, minor_color)
        pair_number = mapper.get_pair_number_from_color(test_pair)
        print(f"[In] Colors: {test_pair}, [Out] Pair Number: {pair_number}")
        assert pair_number == expected_pair_number
    except Exception as e:
        print(f"Error: {e}")
