# polymorphism with class object
from pytz import country_timezones


class Bangladesh:
    def Capital(self):
        print("Dhaka is the capital city of bangladesh")
    def language(self):
        print("Bangla is the mother language of Bangladesh")

class England:
    def Capital(self):
        print("London is the capital city of England")
    def language(self):
        print("English is the main language")

B=Bangladesh()
E=England()

for country in (B,E):
    country.Capital()
    country.language()