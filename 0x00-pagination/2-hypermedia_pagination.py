#!/usr/bin/env python3


"""
Adds `get_page` method to `Server` class
"""

import csv
import math
from typing import List, Tuple


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
        Retrieve a page of items with additional
            pagination metadata.

        This method retrieves a specific page of data from
            the dataset, along with
        metadata that provides information about the
            pagination state. It is useful
        for implementing paginated views of a dataset, where
            users can navigate
        through pages of data.

        Args:
            page (int): The page number to retrieve.
                defaults to 1.
            page_size (int): The number of items per page.
                Defaults to 10.

        Returns:
            dict: A dictionary containing the following key-value pairs:
                - "page_size" (int): The number of items on the current page.
                - "page" (int): The current page number.
                - "data" (List[List]): The list of items on the current page.
                - "next_page" (Optional[int]): The page number of the
                next page, or None if this is the last page.
                - "prev_page" (Optional[int]): The page number of the
                previous page,
                or None if this is the first page.
                - "total_pages" (int): The total number of pages available.

        Raises:
            AssertionError: If the page or page_size
                arguments are invalid.

        Example:
            If you have a dataset with 100 items and request
                page 2 with a page_size of 10,
            this method will return a dictionary with the items
                from index 10 to 19, along with
            metadata about the pagination state.
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
