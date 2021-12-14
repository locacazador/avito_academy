"""Testing Abstract base classes via Pokemons"""
import random
from abc import ABC, abstractmethod


class AnimeMon(ABC):
    """Abstract Base class of Monster"""

    def __init__(self):
        """
        Set exp equals to zero to any monster.
        """
        self._exp = 0

    @property
    @abstractmethod
    def exp(self) -> int:
        """
        Property to get experience
        :return: value of experience
        """
        return self._exp

    @abstractmethod
    def inc_exp(self, value: int):
        """Base method of increasing exp"""


class Pokemon(AnimeMon):
    """Pokemon class"""

    @property
    def exp(self) -> int:
        """
        Use abstract parent property
        :return: experience of pokemon
        """
        return super().exp

    def inc_exp(self, value: int) -> None:
        """
        Increasing experience by value inplace.
        Formula is new_exp = prev_exp + value * 4.
        :param value: number of exp to be multi.
        >>> pokemon = Pokemon()
        >>> pokemon.inc_exp(3)
        >>> print(pokemon.exp)
        12
        """

        self._exp += value * 4


class Digimon(AnimeMon):
    """Digimon class of monsters"""

    @property
    def exp(self) -> int:
        """
        Get experience of the monster.
        Use abstract parent method.
        :return: Current experience
        """
        return super().exp

    def inc_exp(self, value: int):
        """
        Increase experience of the monster by
        formula:
        new_exp = prev_exp + value * 8
        :param value: number of exp to be multi.
        >>> digimon = Digimon()
        >>> digimon.inc_exp(3)
        >>> print(digimon.exp)
        24
        """
        self._exp += value * 8


def train(warrior: AnimeMon):
    """
    Function to mimic farming of the monster.
    :param warrior: Anime monster to train.
    """
    step_size, level_size = 10, 100
    sparring_qty = (level_size - warrior.exp % level_size) // step_size
    for _ in range(sparring_qty):
        win = random.choice([True, False])
        if win:
            warrior.inc_exp(step_size)


if __name__ == '__main__':
    pokemon = Pokemon()
    digimon = Digimon()
    assert pokemon.exp == 0 and digimon.exp == 0, 'Wrong init'
    train(digimon)  # expect increasing of exp
    print(f'Digimon exp is {digimon.exp}')
    train(pokemon)
    print(f'Pokemon exp is {pokemon.exp}')  # pokemon exp tend to be less
