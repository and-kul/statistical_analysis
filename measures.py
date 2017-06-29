import statistics
from typing import Collection, Sequence


class Measures:
    def __init__(self):
        self.average: float = None
        self.min: int = None
        self.max: int = None
        self.median: int = None
        self.standard_deviation: float = None

    @classmethod
    def from_data(cls, data: Sequence[int]):
        result = cls()
        result.average = statistics.mean(data)
        result.min = min(data)
        result.max = max(data)
        result.median = statistics.median(data)
        result.standard_deviation = statistics.pstdev(data)
        return result

    def __str__(self):
        return "average = {0};  st_dev = {1};  median = {2};  min = {3};  max = {4}".format(self.average,
                                                                                            self.standard_deviation,
                                                                                            self.median,
                                                                                            self.min,
                                                                                            self.max)
