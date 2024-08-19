#!/usr/bin/env python3

import csv
import math
from typing import List, Tuple

"""
Adds `get_page` method to `Server` class
"""


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

    def index_range(self, page, page_size) -> Tuple[int, int]:
        """function should return a tuple of size two
        containing a start index and an end index
        """
        start_index = (page-1) * page_size
        end_index = start_index + page_size
        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get items for the given page number
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        startIndex, endIndex = self.index_range(page, page_size)
        return self.dataset()[startIndex:endIndex]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Retrieve a page of items with additional pagination metadata.
        """
        current_page_data = self.get_page(page, page_size)

        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        if page < total_pages:
            next_page = page + 1
        else:
            next_page = None

        if page > 1:
            prev_page = page - 1
        else:
            prev_page = None

        dict = {
            "page_size": page_size,
            "page": page,
            "data": current_page_data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
        return dict
