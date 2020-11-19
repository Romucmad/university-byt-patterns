from __future__ import annotations
from abc import ABC, abstractmethod


class NumberRequest:
    def __init__(self, first_number: int, second_number: int, do: str):
        self.first_number = first_number
        self.second_number = second_number
        self.do = do


class IChain(ABC):

    @classmethod
    @abstractmethod
    def set_next_chain(cls, chain: IChain) -> None:
        """set next chain"""

    @classmethod
    @abstractmethod
    def calculate(cls, numbers: NumberRequest) -> int:
        """calculates"""


class AddDo(IChain):
    next_chain = None

    @classmethod
    def set_next_chain(cls, chain: IChain) -> None:
        cls.next_chain = chain

    @classmethod
    def calculate(cls, numbers: NumberRequest) -> int:
        if numbers.do == '+':
            return numbers.first_number + numbers.second_number
        else:
            return cls.next_chain.calculate(numbers)


class SubtractDo(IChain):
    next_chain = None

    @classmethod
    def set_next_chain(cls, chain: IChain) -> None:
        cls.next_chain = chain

    @classmethod
    def calculate(cls, numbers: NumberRequest) -> int:
        if numbers.do == '-':
            return numbers.first_number - numbers.second_number
        else:
            return cls.next_chain.calculate(numbers)


class MultiplyDo(IChain):
    next_chain = None

    @classmethod
    def set_next_chain(cls, chain: IChain) -> None:
        cls.next_chain = chain

    @classmethod
    def calculate(cls, numbers: NumberRequest) -> int:
        if numbers.do == '*':
            return numbers.first_number * numbers.second_number
        else:
            return cls.next_chain.calculate(numbers)


class DivideDo(IChain):
    next_chain = None

    @classmethod
    def set_next_chain(cls, chain: IChain) -> None:
        cls.next_chain = chain

    @classmethod
    def calculate(cls, numbers: NumberRequest):
        if numbers.do == '/':
            return int(numbers.first_number / numbers.second_number)
        else:
            return 'The end of the chain, wrong do'
