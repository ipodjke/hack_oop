from abc import ABCMeta, abstractmethod
from typing import List


class CharacterInterface():
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_hit(self: object, attack_damage: float) -> None:
        pass

    @abstractmethod
    def get_attack_damage(self: object) -> float:
        pass

    @abstractmethod
    def get_defens(self: object) -> float:
        pass

    @abstractmethod
    def dress_things(self: object, things: List[object]) -> None:
        pass

    @abstractmethod
    def is_alive(self: object) -> bool:
        pass


class GameEngineInterface():
    __metaclass__ = ABCMeta

    @abstractmethod
    def prepare_players_for_battle(self: object) -> List[object]:
        pass


# class ThingsInterface():
#     __metaclass__ = ABCMeta

#     @abstractmethod
#     def get_thing(self: object) -> object:
#         pass
