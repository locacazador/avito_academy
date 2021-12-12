import os

from redirect_output import calculate

CONST_FILE_PATH = 'function_output.txt'


def test_redirect_output_into_file():
    """
    Test expected result from function.
    Expect file with name function_output.txt
    """
    calculate()
    with open(CONST_FILE_PATH, 'r') as check_file:
        lines = check_file.readlines()
        expected_lines = ['1 2 3 4 5 6 7 8 9 10 11 12'
                          ' 13 14 15 16 17 18 19 \n',
                          '1 4 9 16 25 36 49 64 81 100 121'
                          ' 144 169 196 225 256 289 324 361 \n',
                          '1 8 27 64 125 216 343 512 729 1000'
                          ' 1331 1728 2197 2744 3375 4096 4913 5832 6859 \n',
                          '1 16 81 256 625 1296 2401 4096 6561 10000'
                          ' 14641 20736 28561 38416 50625 65536 83521 104976'
                          ' 130321 \n']
        assert lines == expected_lines
    os.remove(CONST_FILE_PATH)  # delete after testing
