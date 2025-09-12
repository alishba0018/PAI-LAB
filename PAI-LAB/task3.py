def employee(name, salary):
    if salary:
        newsalary = salary * 0.98
    else:
        newsalary = 10000
    
    return name, newsalary


name, newsalary = employee("Ali", 7000)
print(name, newsalary)  # Output: Ali 6860.0
name2, newsalary2 = employee("Omar", 0)
print(name2, newsalary2) # Output: Omar 10000