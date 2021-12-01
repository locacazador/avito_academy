import pytest


from one_hot_encoding import fit_transform


def test_empty_args():
    """
    Check if exception is raised with no argument
    """
    with pytest.raises(TypeError):
        fit_transform()


def test_single_string():
    """
    Test case when only one string in args
    """
    single_arg = 'abc'
    expected_one_hot = [('abc', [1])]
    actual = fit_transform(single_arg)
    assert actual == expected_one_hot


def test_multiple_args():
    """
    Test case when multiple string in args
    """
    multiple_args = ['Madrid', 'Lisbon', 'Berlin', 'Madrid']
    expected_one_hot_multiple_args = [
        ('Madrid', [0, 0, 1]),
        ('Lisbon', [0, 1, 0]),
        ('Berlin', [1, 0, 0]),
        ('Madrid', [0, 0, 1])
    ]
    actual_transform = fit_transform(multiple_args)
    assert actual_transform == expected_one_hot_multiple_args


def test_not_in_result():
    """
    Test case wrong result
    """
    args = ['a', 'b', 'c', 'a', 'b']
    expected_not_in = ('b', [1, 0, 0])
    actual_result = fit_transform(args)
    assert expected_not_in not in actual_result
