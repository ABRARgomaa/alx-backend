#!/usr/bin/env python3
"""
start and end
"""


from typing import Tuple, List, Dict, Any
import csv
import math


def index_range(page: int, page_size: int) -> Tuple:
    """
    start and end
    """
    start = (page - 1) * page_size
    end = page * page_size
    return(start, end)


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
        get page
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start >= len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        get_hyper method
        """
        returneddata = self.get_page(page, page_size)
        start, end = index_range(page, page_size)

        def next():
            """
            next method
            """
            if end < len(self.dataset()):
                return page + 1
            return None

        def prev():
            """
            prev method
            """
            if start > 0:
                return page - 1
            return None
        return {
            'page_size': len(returneddata),
            'page': page,
            'data': returneddata,
            'next_page': next(),
            'prev_page': prev(),
            'total_pages': math.ceil(len(self.dataset()) / page_size)
        }
