class TimeZone:

    def __init__(self, name, offset_hours, offset_minutes):
        self.name = name
        self.offset_hours = offset_hours
        self.offset_minutes = offset_minutes

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        if not len(name.strip()) > 0:
            raise ValueError(f'Timezone bad name - {name}')
        else:
            self.name = name.strip()

tz1 = TimeZone('ABC', -2, -15)
print(tz1.name)

