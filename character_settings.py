from typing import List

from base_interface import CharacterInterface
from game_settings import GameCharacteristics
from help_mixin_func import GenericCharacteristicFunction


class Race(GameCharacteristics, GenericCharacteristicFunction):
    def __init__(self: object,
                 bonus_race_characteristics: dict = None) -> None:

        super().__init__()
        self.clear_base_charasteristics()
        self.calculate_characteristics(bonus_race_characteristics)


class ClassCharacter(GameCharacteristics, GenericCharacteristicFunction):
    def __init__(self: object,
                 bonus_class_characteristics: dict = None) -> None:

        super().__init__()
        self.clear_base_charasteristics()
        self.calculate_characteristics(bonus_class_characteristics)


class Character(GameCharacteristics,
                CharacterInterface,
                GenericCharacteristicFunction):

    def __init__(self: object, race: Race,
                 class_character: ClassCharacter) -> None:
        super().__init__()
        self.calculate_characteristics(race)
        self.calculate_characteristics(class_character)

    def dress_things(self: object, things: List[object]) -> None:
        for thing in things:
            self.calculate_characteristics(thing)

    def get_attack_damage(self: object) -> float:
        return self.game_characteristics['attack']

    def get_defens(self: object) -> float:
        return self.game_characteristics['defens']

    def is_alive(self: object) -> bool:
        if self.game_characteristics['stamina'] > 0:
            return True
        return False

    def get_hit(self: object, attack_damage: float) -> None:
        self.game_characteristics['stamina'] -= (
            attack_damage * (1 - self.game_characteristics['defens'])
        )


class Player(Character):
    def __init__(self: object, race: Race,
                 class_character: ClassCharacter, name: str) -> None:
        super().__init__(race, class_character)
        self.name = name
