class Car():
    """Простая модель автомобиля"""

    def __init__(self,make,model,year):
        """Иницилизирует фтрибуты автообиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometr_reading = 0

    def get_descriptive_name(self):
        """Возращение фккуратно отформатированого описания."""
        long_mane = f"{self.year}  {self.make} {self.model}"
        return long_mane.title()

    def read_odometr(self):
        """Выводит пробег машины в милях """
        print(f"This car has {self.odometr_reading} miles on it.")

    def update_odometr(self,mileage):
        """Устаравливает задонное значение на одометре."""
        if mileage >= self.odometr_reading:
            self.odometr_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        """Увеличивает покозание одометра с заданным ариращиванием."""
        self.odometr_reading += miles

class Battery():
    """Простая модель аккумулятора электромобиля."""
    def __init__(self,battery_size=75):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print(f"This car has a {self.battery_size} - kWh battery.")


class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
