countries = input().split(", ")
capitals = input().split(", ")

my_dict = {country: capital for country, capital in zip(countries, capitals)}

for country, capital in my_dict.items():
    print(f"{country} -> {capital}")
