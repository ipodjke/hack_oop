from typing import Union


class GenericCharacteristicFunction:
    """Реализум базовый набор функций для работы с характеристиками
    любого обЪекта игры.
    """
    # вот тут немного эксперемента, хотел поэксперементировать как это работает
    CHARACTERISTIC = '.__dict__[list(self.__dict__)[0]]'

    def calculate_characteristics(self: object,
                                  bonus_characteristics:
                                  Union[dict, object]) -> None:
        """Добавляет характеристики к базовым"""
        self.bonus_characteristics = self._get_bonus_characteristics(
                                        bonus_characteristics
                                    )
        character_characteristic = eval(
            'self' + GenericCharacteristicFunction.CHARACTERISTIC
                                        )
        for key, value in self.bonus_characteristics.items():
            if key not in character_characteristic:
                continue
            character_characteristic[key] = round(
                value + character_characteristic[key], 2
            )

    def _get_bonus_characteristics(self: object, bonus_characteristics:
                                   Union[dict, object]) -> None:
        """Извлекает характеристики из объектов."""
        if type(bonus_characteristics) == dict:
            return bonus_characteristics
        return eval('bonus_characteristics' +
                    GenericCharacteristicFunction.CHARACTERISTIC
                    )

    def clear_base_charasteristics(self: object) -> None:
        """Обнуляет характеристики объектов"""
        character_characteristic = eval(
            'self' + GenericCharacteristicFunction.CHARACTERISTIC
        )
        for key in character_characteristic:
            character_characteristic[key] = 0.0

    def __str__(self: object) -> str:
        """Выводит данные объектов в удобочитаемом ввиде"""
        result = [f'{ key }: { value }\n'
                  for key, value in
                  eval('self' +
                       GenericCharacteristicFunction.CHARACTERISTIC
                       ).items()
                  ]
        try:
            if self.name:
                result.append(f'name: {self.name}\n')
        except AttributeError:
            pass
        return ''.join(result)
