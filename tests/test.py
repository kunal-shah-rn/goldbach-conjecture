from goldbach import genSequence


def test_sequence_generator():
    assert genSequence.sequence_generator(7) == ([7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], True)
