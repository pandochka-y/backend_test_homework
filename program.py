# импортируйте библиотеку math
import math

class Planet:
    def __init__(self, name, radius, temp_celsius):
        self.name = name
        self.surface_area = round(4*math.pi*math.sqrt(radius))
        self.average_temp_celcius = temp_celsius
        self.average_temp_fahrenheit = round((temp_celsius*9/5)+32)


    def show_info(self):
        print(f"Планета {self.name} имеет площадь поверхности {self.surface_area} кв.км.")

        print(f"Средняя температура поверхности планеты: {self.average_temp_fahrenheit}° по Фаренгейту.")



jupiter = Planet('Юпитер', 69911, -108)

# вызовите метод show_info для Юпитера
jupiter.show_info()