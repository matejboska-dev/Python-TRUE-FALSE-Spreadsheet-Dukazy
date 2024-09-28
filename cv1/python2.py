import math

number_of_flowers = 14513

life_chance = 0.80

death_rate = 0.08

semen_in_bag = 100

grow_probability = life_chance * (1 - death_rate)

seeds_needed_per_plant = 1 / grow_probability

number_of_semen = seeds_needed_per_plant * number_of_flowers


bags_needed = math.ceil(number_of_semen/ semen_in_bag)

print(f"Customer has to buy {bags_needed} number of semen.")
