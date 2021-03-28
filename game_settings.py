class GameCharacteristics:
    """Основные характеристики предметов, персонажев, рас."""
    def __init__(self: object) -> None:
        self.game_characteristics = {
            'stamina': 110.0,
            'attack': 10.0,
            'defens': 0.05,
        }


class GameSettings():
    """Основные  настройки игры."""
    amount_characters = 10
    max_things = amount_characters * 4
    max_things_for_character = 4
