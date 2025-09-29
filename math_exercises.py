import math
# 11. Time converter
seconds = 4857
minutes = seconds // 60
hours = minutes // 60
minutes = minutes % 60
print(f"{seconds} sekundit on {hours} ja {minutes} minut(it).")

# 12. Stundent helper

angle = 30
sine = math.sin(math.radians(angle))
sine = round(sine, 1)
cosine = math.cos(math.radians(angle))
cosine = round(cosine, 1)

# 13. Greetings

lots_of_heys = n * "Hey"

# 14. Adding numbers

string_numbers = str(num_a) + str(num_b)