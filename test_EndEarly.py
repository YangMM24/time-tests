from times import time_range, compute_overlap_time
import pytest

large = time_range("2010-01-12 10:00:00", "2010-01-12 09:00:00")
short = time_range("2010-01-12 12:00:00", "2010-01-12 12:45:00")
result = compute_overlap_time(large, short)
print(result)