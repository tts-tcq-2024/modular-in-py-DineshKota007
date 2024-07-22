from ColorPairMapper import ColorPairMapper
from ColorPair import ColorPair
def run_tests():
    mapper = ColorPairMapper()
    pair_number = 4
    test_pair1 = mapper.map_number_to_color_pair(pair_number)
    print(f"[In]Pair Number: {pair_number}, [Out] Colors: {test_pair1}")
    assert test_pair1.major_color == 'White'
    assert test_pair1.minor_color == 'Brown'
    pair_number = 5
    test_pair1 = mapper.map_number_to_color_pair(pair_number)
    print(f"[In]Pair Number: {pair_number}, [Out] Colors: {test_pair1}")
    assert test_pair1.major_color == 'White'
    assert test_pair1.minor_color == 'SlateGray'
    pair_number = 23
    test_pair1 = mapper.map_number_to_color_pair(pair_number)
    print(f"[In]Pair Number: {pair_number}, [Out] Colors: {test_pair1}")
    assert test_pair1.major_color == 'Violet'
    assert test_pair1.minor_color == 'Green'
    test_pair2 = ColorPair(major_color='Yellow', minor_color='Green')
    pair_number = mapper.map_color_pair_to_number(test_pair2)
    print(f"[In]Colors: {test_pair2}, [Out] PairNumber: {pair_number}")
    assert pair_number == 18
    test_pair2 = ColorPair(major_color='Red', minor_color='Blue')
    pair_number = mapper.map_color_pair_to_number(test_pair2)
    print(f"[In]Colors: {test_pair2}, [Out] PairNumber: {pair_number}")
    assert pair_number == 6
if __name__ == "__main__":
    run_tests()
