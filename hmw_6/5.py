class Stationery:
    title = ""

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки. Инструмент: {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки. Инструмент: {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки. Инструмент: {self.title}")


p = Pen("Pen")
p.draw()

penc = Pencil("Pencil")
penc.draw()

h = Handle("Handle")
h.draw()