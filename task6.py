def top_3_countries(population):
    top_countries = []
    for i in range(3):
        if not population:
            break
        max_country = None
        max_pop = -1
        for country, pop in population.items():
            if pop > max_pop:
                max_country = country
                max_pop = pop
        top_countries.append((max_country, max_pop))
        del population[max_country]
    return top_countries
    
countries = {
    "China": 1400000000,
    "India": 1380000000,
    "USA": 331000000,
    "Indonesia": 273000000,
    "Pakistan": 220000000
}
result = top_3_countries(countries.copy())
print("Top 3 most populated countries:")
for c, p in result:
    print(c, "-", p)
