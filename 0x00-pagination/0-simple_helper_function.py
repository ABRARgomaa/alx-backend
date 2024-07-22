#!/usr/bin/env python3
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
