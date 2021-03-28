from character_settings import ClassCharacter, Race

# реализуем классы и расы игры

orc = Race({'stamina': 50, 'attack': 5, 'defens': 0.01})
human = Race({'stamina': 30, 'attack': 3, 'defens': 0.1})
gnome = Race({'stamina': 10, 'attack': 1, 'defens': 0.2})

warrior = ClassCharacter({'stamina': 100, 'attack': 10, 'defens': 0.15})
paladin = ClassCharacter({'stamina': 80, 'attack': 12, 'defens': 0.1})
mage = ClassCharacter({'stamina': 30, 'attack': 25, 'defens': 0.0})

available_race = (orc, human, gnome)
available_class = (warrior, paladin, mage)
