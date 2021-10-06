D = {
    "Andra Pradesh":"Hyderabad",
    "Maharashtra":"Mumbai",
    "Rajasthan":"Jaipur",
    "Bihar":"Patna"
    }

print(list(D.keys()))
print(list(D.values()))
del(D['Bihar'])
D['Karnataka'] = "Bangalore"
print(D)

D["Maharashtra"] = "Bombay"
print(D)
D["m"] = "Bombay","cat"
print(D)
D["m"] = "lol"
print(D)