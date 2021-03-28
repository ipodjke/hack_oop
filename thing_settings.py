from game_settings import GameCharacteristics
from help_mixin_func import GenericCharacteristicFunction


class Thing(GameCharacteristics, GenericCharacteristicFunction):
    """Класс описывыющий вещи в игре"""
    def __init__(self: object, characteristics: dict = None) -> None:
        super().__init__()
        self.clear_base_charasteristics()
        self.calculate_characteristics(characteristics)
