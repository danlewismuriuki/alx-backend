#!/usr/bin/env python3

import csv
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
        Retrieve a specific page of items from the dataset.

        This method fetches a subset of the dataset
            corresponding to the given page number
        and page size. It is useful for breaking down a large
            dataset into smaller, more manageable pages.

        Args:
            page (int): The page number to retrieve. Must be a 
            positive integer. Defaults to 1.
            page_size (int): The number of items per page.
                Must be a positive integer. Defaults to 10.

        Returns:
            List[List]: A list of lists, where each inner
                list represents a row of data from
            the dataset corresponding to the specified page.

        Raises:
            AssertionError: If the page or page_size
                arguments are not positive integers.

        Example:
            If the dataset contains 100 items and you
                request page 2 with a page_size of 10,
            this method will return a list of items
                from index 10 to 19.

    """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        startIndex, endIndex = self.index_range(page, page_size)
        return self.dataset()[startIndex:endIndex]
