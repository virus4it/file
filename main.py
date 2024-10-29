class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        """Возвращает все товары из файла в виде строки."""
        try:
            with open(self.__file_name, 'r') as file:
                return file.read().strip()  # Читаем и удаляем лишние символы новой строки
        except FileNotFoundError:
            return ""  # Если файла нет, возвращаем пустую строку

    def add(self, *products):
        """Добавляет продукты в файл, если их там еще нет."""
        # Читаем существующие записи из файла
        existing_lines = self.get_products().splitlines()

        with open(self.__file_name, 'a') as file:
            for product in products:
                product_str = str(product)

                # Проверяем, есть ли продукт с такими же данными
                if product_str not in existing_lines:
                    file.write(product_str + '\n')
                    existing_lines.append(product_str)  # Добавляем в список для следующих проверок
                else:
                    print(f"Продукт {product} уже есть в магазине")


# Пример работы программы
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # Проверка метода __str__

s1.add(p1, p2, p3)

print(s1.get_products())  # Чтение из файла и вывод всех товаров
