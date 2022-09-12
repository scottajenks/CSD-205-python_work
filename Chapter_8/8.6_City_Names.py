# 8-6. City Names
def city_country(city, country):
    '''Return a city and country, formatted'''
    formatted_name = f'"{city}, {country}"'
    return formatted_name.title()


name1 = city_country("Orlando", "United states of america")
name2 = city_country("madrid", "spain")
name3 = city_country(country="Brazil", city="recife")
print(name1)
print(name2)
print(name3)
