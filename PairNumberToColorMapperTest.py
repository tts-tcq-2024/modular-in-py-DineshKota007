from PairNumberToColorMapper import PairNumberToColorMapper
def PairNumberToColorMapper():
    mapper = PairNumberToColorMapper()
    test_color_from_pair_number(mapper, 4, "White", "Brown")
    test_color_from_pair_number(mapper, 5, "White", "SlateGray")
    test_color_from_pair_number(mapper, 23, "Violet", "Green")
    test_color_from_pair_number(mapper, 1, "White", "Blue")
    test_color_from_pair_number(mapper, 25, "Violet", "SlateGray")
    test_invalid_pair_number(mapper, 0)
    test_invalid_pair_number(mapper, 26)
 
def ColorToPairNumberMapper(mapper, pair_number, expected_major, expected_minor):
    try:
        test_pair = mapper.get_color_from_pair_number(pair_number)
        print(f"[In] Pair Number: {pair_number}, [Out] Colors: {test_pair}")
        assert test_pair.major_color == expected_major
        assert test_pair.minor_color == expected_minor
    except Exception as e:
        print(f"Error: {e}")
 
def PairNumberToColorMapper(mapper, pair_number):
    try:
        test_pair = mapper.get_color_from_pair_number(pair_number)
        print(f"[In] Pair Number: {pair_number}, [Out] Colors: {test_pair}")
    except ValueError:
        print(f"Passed: Pair number {pair_number} is out of range.")
    except Exception as e:
        print(f"Error: {e}")
