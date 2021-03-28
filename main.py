import colorama

from game_engine import GameEngineWithGenericRandomCharacteristic


class Main():
    """Класс для запуска игры.

    Основан на использования движка реализующего полный
    рандом в выборе основных характеристик игры.
    """
    def __init__(self: object) -> None:
        """Выбираем движок игры и запускаем игру"""
        self.game_engine = GameEngineWithGenericRandomCharacteristic()
        self.start_game()

    def start_game(self: object) -> None:
        """Реализует основную логику игры."""
        colorama.init()
        print('ARENA GAME', end='')
        print(colorama.Fore.BLACK + colorama.Back.WHITE)
        print('Подготавливаем игроков')
        self.game_engine.prepare_players_for_battle()
        print(colorama.Fore.RED + 'Подготовка завершена. ДАНАЧНЕТСЯ БИТВА!',
              end=''
              )
        print(colorama.Style.RESET_ALL, end='')
        print(colorama.Fore.GREEN + colorama.Back.YELLOW)
        self.game_engine.start_battle()
        print(colorama.Fore.RED + colorama.Back.WHITE)
        print('Битва завершена.', end='')
        print(colorama.Fore.YELLOW + colorama.Back.BLUE)
        self.game_engine.print_winner()


if __name__ == '__main__':
    game = Main()
