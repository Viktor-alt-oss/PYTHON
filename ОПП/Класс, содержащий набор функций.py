class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(value):
        return value * (9/5) + 32
    
    @staticmethod
    def fahrenheit_to_celsius(value):
        return (value - 32) * (5/9)
    
    @staticmethod
    def celsius_to_kelvin(value):
        return value + 273.15
    
    @staticmethod
    def kelvin_to_celsius(value):
        return value - 273.15
    
    @staticmethod
    def fahrenheit_to_kelvin(value):
        return ((9/5)(value - 273.15)) + 32
    
    @staticmethod
    def kelvin_to_fahrenheit(value):
        return ((9/5)(value - 32)) + 273.15
