"""
Utility functions for the project.
This module provides helper functions that are commonly needed.
"""

from typing import Any, List, Optional, Union
import os
import sys


def safe_get_item(collection: Union[List, dict], index: Union[int, str], default: Any = None) -> Any:
    """
    Safely get an item from a collection by index or key.
    
    Args:
        collection: List or dictionary to get item from
        index: Index or key to retrieve
        default: Default value to return if index/key not found
        
    Returns:
        Item at index/key or default value
    """
    try:
        return collection[index]
    except (IndexError, KeyError, TypeError):
        return default


def is_empty(value: Any) -> bool:
    """
    Check if a value is empty.
    
    Args:
        value: Value to check
        
    Returns:
        True if value is empty, False otherwise
    """
    if value is None:
        return True
    if isinstance(value, (str, list, dict, tuple, set)):
        return len(value) == 0
    return False


def ensure_directory(path: str) -> str:
    """
    Ensure a directory exists, creating it if necessary.
    
    Args:
        path: Path to directory
        
    Returns:
        The path that was ensured to exist
    """
    os.makedirs(path, exist_ok=True)
    return path


if __name__ == "__main__":
    # Simple test
    test_list = [1, 2, 3]
    print(f"Safe get item 0: {safe_get_item(test_list, 0)}")
    print(f"Safe get item 10: {safe_get_item(test_list, 10, 'not found')}")
    print(f"Is empty list: {is_empty([])}")
    print(f"Is empty string: {is_empty('')}")
