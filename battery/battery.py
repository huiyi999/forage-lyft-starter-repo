"""
Created on 2022-05-30
@author: chy
"""

from abc import ABC, abstractmethod


class Battery(ABC):
    """An abstract battery class."""

    def __init__(self) -> None:
        pass

    @abstractmethod
    def needs_service(self):
        pass
