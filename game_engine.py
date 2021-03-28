import random
from typing import List

from base_interface import GameEngineInterface
from character_settings import Player
from game_settings import GameCharacteristics, GameSettings
from race_and_class import available_class, available_race
from thing_settings import Thing


class GameEngineWithGenericRandomCharacteristic(
        GameCharacteristics, GameSettings, GameEngineInterface
     ):
    """Движок игры"""
    def __init__(self: object) -> None:
        """Определяем классы для персонажей вещей,
        подтягиваем игровые классы и расы,
        определяем границу  генерируемых значений,
        устанавливаем дополнительные переменые движка
        """
        super().__init__()
        self._set_border_for_generic_characteristic()
        self.class_character = available_class
        self.race = available_race
        self.player_class = Player
        self.thing_class = Thing
        self.players = []
        self.winner = None

    def prepare_players_for_battle(self: object) -> None:
        """создает список игроков"""
        self.players = self._get_random_class_race_players()
        things = self._get_random_amount_things()
        self._sort_things_by_defens(things)
        self._dress_players(self.players, things)

    def start_battle(self: object) -> None:
        """проводит бой на арене и определяет победителя"""
        while len(self.players) > 1:
            attacker_player = self._choice_player()
            defending_player = self._choice_player()
            attack_damage = attacker_player.get_attack_damage()
            received_damage = (
                attack_damage * (1 - defending_player.get_defens())
            )
            defending_player.get_hit(attack_damage)
            self.players.append(attacker_player)
            if defending_player.is_alive():
                self.players.append(defending_player)
            print(
                f'{attacker_player.name} наносит удар по '
                f'{defending_player.name} на {received_damage:.2f}'
            )
        self.winner = self.players.pop()

    def print_winner(self: object) -> None:
        """печатает победителя"""
        print(f'Поздравляем нашего победителя {self.winner.name}')

    def _get_random_class_race_players(
        self: object
         ) -> List[Player]:
        player_name = (
            'Bred Pitt', 'Antonio Potogin', 'Donald Trump', 'Hoops', 'Riana',
            'Mett Daimond', 'Trall', 'Death Wish', 'Iron Man', 'Tony Hawks',
            'Dmitry Mendeleev', 'Albert', 'Ranetki', 'Batman', 'Joker',
            'Jhony Depp', 'Limp Bizkit', 'Eminem', 'Ilon Mask', 'Nikola'
        )
        return [self.player_class(
                    random.choice(self.race),
                    random.choice(self.class_character),
                    random.choice(player_name)
                )
                for player in range(self.amount_characters)
                ]

    def _get_random_amount_things(self: object) -> List[Thing]:
        max_things = random.randint(1, self.max_things)
        return [self.thing_class(
                    {f'{characteristic}': round(random.uniform(0.01, value), 2)
                     for characteristic, value in (self.game_characteristics
                                                       .items()
                                                   )}
                )
                for thing in range(max_things)
                ]

    def _dress_players(
        self: object, players: List[Player], things: List[Thing]
    ) -> None:
        for player in players:
            things_to_equip = self._get_random_things_for_equip(things)
            if not things_to_equip:
                break
            player.dress_things(things_to_equip)

    def _get_random_things_for_equip(
        self: object, things: List[Thing]
    ) -> List[Thing]:
        amount_things_for_character = random.randint(
                                        1, self.max_things_for_character
                                       )
        result = []
        for i in range(amount_things_for_character):
            if not len(things):
                break
            index_thing = random.randint(0, len(things) - 1)
            thing = things.pop(index_thing)
            result.append(thing)
        return result

    def _choice_player(self: object) -> Player:
        index_player = random.randint(0, len(self.players) - 1)
        return self.players.pop(index_player)

    def _sort_things_by_defens(
            self: object, things: List[Thing]
         ) -> List[Thing]:

        return things.sort(key=lambda x: x.game_characteristics['defens'])

    def _set_border_for_generic_characteristic(
            self: object
         ) -> None:
        for characteristic, value in self.game_characteristics.items():
            if characteristic == 'defens':
                self.game_characteristics[characteristic] = 0.1
                continue
            self.game_characteristics[characteristic] = round(value * 0.25, 4)
