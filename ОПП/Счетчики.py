class Counter:
    def start_from(self, count = 0):
        self.count = count

    def increment(self):
        self.count += 1

    def display(self):
        print(f'Текущее значение счетчика = {self.count}')

    def reset(self):
        self.count = 0

c1 = Counter()

c1.start_from(45)
c1.display()  # печатает 45
c1.increment()
c1.display()  # печатает 46
c1.increment()
c1.display()  # печатает 47
c1.reset()  # обнулили с1
c1.display()  # печатает 0