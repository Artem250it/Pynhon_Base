class Car():
    """Простая модель автомобиля"""

    def __init__(self,make,model,year):
        """Иницилизирует фтрибуты автообиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometr_reading = 555

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



my_used_car = Car('subaru','outback',2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometr(23_500)
my_used_car.read_odometr()

my_used_car.increment_odometer(100)
my_used_car.read_odometr()

# my_new_car = Car('audi','a4','2019')
# print(my_new_car.get_descriptive_name())
# my_new_car.update_odometr(556)
# my_new_car.read_odometr()