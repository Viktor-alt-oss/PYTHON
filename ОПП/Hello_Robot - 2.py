class Robot:

    def set_name(self, name):
        self.name = name

    def say_hello(self):
        if not hasattr(self, 'name'):
            print('У робота нет имени')
        else:
            print(f'Hello, human! My name is {self.name}')

    def say_bye(self):
        print('See u later alligator')

d = Robot()
d.say_hello()
d.set_name('Wally')
d.say_hello()
d.say_bye()


