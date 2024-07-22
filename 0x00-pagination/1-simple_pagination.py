#!/usr/bin/env python3
import csv
import math
from typing import List
"""
index range
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    index range method
    """
    startindex = (page - 1) * page_size
    endindex = page * page_size
    return (startindex, endindex)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        get page method
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        if start_index >= len(dataset) or start_index < 0 or end_index <= start_index:
            return []
        return dataset[start_index:end_index]
