def sequence_generator(n):
    """
    Generates sequence of numbers for a given positive integer 'n' by iterative process as specified in Goldbach
    conjecture.
    :param n: positive
    :return: list of numbers in the generated sequence, boolean indicating whether last element of sequence is 1
    """
    if not isinstance(n,int):
        # Will raise an exception if n cant be converted to int
        n = int(n)
    if n <= 0:
        raise ValueError("Input value has to be at least 1.")
    curr_number = n
    sequence = [curr_number]
    check = False
    while curr_number != 1 and not check:
        if curr_number%2 == 0:
            curr_number = int(curr_number/2)
        else:
            curr_number = 3*curr_number + 1
        if curr_number in sequence:
            check = True
            sequence.append(curr_number)
            break
        else:
            sequence.append(curr_number)
    return sequence, sequence[-1] == 1

