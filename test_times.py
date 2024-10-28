from times import time_range, compute_overlap_time


def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), 
                ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def do_not_overlap():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 13:00:00", "2010-01-12 13:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = []
    assert result == expected

def both_contain_intervals():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 120)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_same_time():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 12:00:00", "2010-01-12 12:45:00")
    result = compute_overlap_time(large, short)
    expected = []
    assert result == expected

if __name__ == "__main__":
    #test_given_input()
    #do_not_overlap()
    #both_contain_intervals()
    test_same_time()