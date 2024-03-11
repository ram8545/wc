# Unit tests

from wc import wc_main
def test_wc():
    result = wc_main('example.txt')
    print('result', result)
    assert result == (5, 6, 35), "Test case 1 failed"

    result = wc_main('example.txt example2.txt')
    print('result', result)
    assert result == (8, 10, 60), "Test case 2 failed"

    result = wc_main('nonexistent.txt')
    print('result', result)
    assert result == (1, 2, 14), "Test case 3 failed"

    result = wc_main('-')
    print('result', result)
    assert result is not None, "Test case 4 failed"

    print("All test cases passed.")

# Run unit tests
test_wc()
