import doctest


class Computer:
    def __init__(self, cpu_ghz: float, gpu_ghz: float, storage_capacity: int, occupied_space: int, ram_gb: int):
        """
        Создание и подготовка к работе объекта "Компьютер"

        :param cpu_ghz: Частота ЦП, GHz
        :param gpu_ghz: Частота ГП, GHz
        :param storage_capacity: Размер хранилища, Gb
        :param ram_gb: Размер ОЗУ, Gb
        :param occupied_space: Занятое место в хранилище, Gb

        Примеры:
        >>> pc1 = Computer(3.13, 2.4, 1024, 16)  # инициализация экземпляра класса
        """
        if not isinstance(cpu_ghz, (int, float)):
            raise TypeError("Частота ЦПУ должна быть типа int или float")
        if cpu_ghz <= 0:
            raise ValueError("Частота ЦПУ должна быть положительным числом")
        self.cpu_ghz = cpu_ghz

        if not isinstance(gpu_ghz, (int, float)):
            raise TypeError("Частота ГПУ должна быть типа int или float")
        if gpu_ghz <= 0:
            raise ValueError("Частота ГПУ должна быть положительным числом")
        self.gpu_ghz = gpu_ghz

        if not isinstance(storage_capacity, (int, float)):
            raise TypeError("Размер хранилища должен быть типа int или float")
        if storage_capacity <= 0:
            raise ValueError("Размер хранилища должен быть положительным числом")
        self.storage_gb = storage_capacity

        if not isinstance(occupied_space, (int, float)):
            raise TypeError("Заполненность хранилища должна быть типа int или float")
        if occupied_space < 0:
            raise ValueError("Заполненность хранилища должна быть положительным числом")
        if occupied_space > storage_capacity:
            raise ValueError("Размер хранилища должен быть больше чем занятое пространство")
        self.occupied_space = occupied_space

        if not isinstance(ram_gb, int):
            raise TypeError("Размер ОЗУ должен быть типа int")
        if ram_gb <= 0:
            raise ValueError("Размер ОЗУ должен быть положительным числом")
        self.ram_gb = ram_gb

    def free_space(self) -> float:
        """
        Функция которая выводит свободное место на диске

        :return: Размер свободного места

        Примеры:
        >>> pc1 = Computer(3.13, 2.4, 1024, 16)
        >>> pc1.free_space()
        """
        ...

    def add_storage(self, capacity: (int,float)) -> None:
        """
        Добавление дискового пространства.
        :param capacity: Объем добавляемого пространства


        Примеры:
        >>> pc1 = Computer(3.13, 2.4, 1024, 16)
        >>> pc1.add_storage(256)
        """
        if not isinstance(capacity, (int, float)):
            raise TypeError("Добавляемое пространство должно быть типа int или float")
        if capacity < 0:
            raise ValueError("Добавляемое пространство должно быть положительным числом")
        ...

    def install_soft(self, soft_size: (int, float)) -> None:
        """
        Установка программы (Занятие свободного пространства)

        :param soft_size: Размер программы

        Примеры:
        >>> pc1 = Computer(3.13, 2.4, 1024, 16)
        >>> pc1.install_soft(0.256)
        """

        if not isinstance(soft_size, (int, float)):
            raise TypeError("Размер программы должен быть типа int или float")
        ...

class RPGPlayer:
    def __init__(self, name: str, level: int, health: int, mana: int):
        """
        Создание и подготовка к работе объекта "Игрок в RPG"

        :param name: Имя персонажа игрока
        :param level: Уровень персонажа
        :param health: Здоровье персонажа
        :param mana: Мана (магическая энергия) персонажа

        Примеры:
> player = RPGPlayer('Герой', 5, 100, 50)  # инициализация экземпляра класса
>         """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        if not isinstance(level, int) or level < 1:
            raise ValueError("Уровень должен быть целым числом и не меньше 1")
        if not isinstance(health, int) or health < 0:
            raise ValueError("Здоровье должно быть неотрицательным целым числом")
        if not isinstance(mana, int) or mana < 0:
            raise ValueError("Мана должна быть неотрицательным целым числом")

        self.name = name
        self.level = level
        self.health = health
        self.mana = mana

    def attack(self, target: 'RPGPlayer') -> None:
        """
        Атака другого игрока или монстра.

        :param target: Цель атаки (другой персонаж или монстр)

        Примеры:
        >>> player1 = RPGPlayer('Герой', 5, 100, 50)
        >>> player2 = RPGPlayer('Монстр', 3, 80, 30)
        >>> player1.attack(player2)
        """
        ...

    def cast_spell(self, spell: str) -> None:
        """
        Использование заклинания.

        :param spell: Название заклинания

        Примеры:
        >>> player = RPGPlayer('Герой', 5, 100, 50)
        >>> player.cast_spell('огонь')
        """
        if self.mana < 10:  # Предположим, что каждое заклинание требует 10 маны
            print("Недостаточно маны!")
        else:
            self.mana -= 10
            ...

    def gain_experience(self, amount: int) -> None:
        """
        Получение опыта.

        :param amount: Количество полученного опыта

        Примеры:
        >>> player = RPGPlayer('Герой', 5, 100, 50)
        >>> player.gain_experience(20)
        """
        if not isinstance(amount, int) or amount < 0:
            raise ValueError("Количество опыта должно быть неотрицательным целым числом")

        self.level += amount // 100  # Предположим, что за каждые 100 опытных очков повышается уровень
        ...

    def heal(self) -> None:
        """
        Восстановление здоровья.

        Примеры:
        >>> player = RPGPlayer('Герой', 5, 100, 50)
        >>> player.heal()
        """
        self.health += 20  # Предположим, что исцеление восстанавливает 20 здоровья
        if self.health > 100:  # Максимальное здоровье — 100
            self.health = 100


class FuelTank:
    def __init__(self, capacity_volume: float, occupied_volume: float):
        """
        Создание и подготовка к работе объекта "Топливный бак"

        :param capacity_volume: Объем топливного бака
        :param occupied_volume: Объем топлива в баке

        Примеры:
        >>> tank1 = FuelTank(45, 20)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем топливного бака должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем топливного бака должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Объем топлива в баке должен быть int или float")
        if occupied_volume < 0:
            raise ValueError("Объем топлива в баке не может быть отрицательным числом")
        self.occupied_volume = occupied_volume

    def is_tank_empty(self) -> bool:
        """
        Функция которая проверяет является ли бак пустым

        :return: Является ли бак пустым

        Примеры:
        >>> tank1 = FuelTank(45, 20)
        >>> tank1.is_tank_empty()
        """
        ...

    def add_fuel_to_tank(self, fuel: float) -> None:
        """
        Добавление топлива в бак.
        :param fuel: Объем добавляемого топлива

        :raise ValueError: Если количество добавляемого топлива превышает свободное место в баке, то вызываем ошибку

        Примеры:
        >>> tank1 = FuelTank(45, 20)
        >>> tank1.add_fuel_to_tank(10)
        if not isinstance(water, (int, float)):
            raise TypeError("Добавляемое топливо должно быть типа int или float")
        if water < 0:
            raise ValueError("Добавляемое топливо должно быть положительным числом")
        ...
        """

    def use_fuel_from_tank(self, used_fuel: float) -> None:
        """
        Использование топлива из бака.

        :param used_fuel: Объем использованого топлива
        :raise ValueError: Если количество используемого топлива превышетает кол-во топлива в баке,
        то возвращается ошибка.


        Примеры:
        >>> tank1 = FuelTank(45, 20)
        >>> tank1.use_fuel_from_tank(10)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации