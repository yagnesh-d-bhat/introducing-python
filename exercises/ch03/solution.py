years_list = [1986, 1987, 1988, 1989, 1990, 1991]

third_birthday = years_list[4]
print("Third Birthday", third_birthday)

print("Oldest on", years_list[5])

things = ["mozzarella", "cinderella", "salmonella"]
things[1] = things[1].capitalize()
things[0] = things[0].upper()
del things[2]
print(things)

surprise = ["Groucho", "Chico", "Harpo"]
surprise[-1] = surprise[-1].lower()
surprise = surprise[::-1]
print(surprise)
surprise[0] = surprise[0].capitalize()
print(surprise)

e2f = {
    "dog": "chien",
    "cat": "chat",
    "walrus": "morse"
}

print("French word for walrus is", e2f["walrus"])

f2e = {}
for english, french in e2f.items():
    f2e[french] = english

print(f2e)

print("English words from e2f", e2f.keys())

life = {
    'animals': {
        'cats': ['Henri', 'Grumpy', 'Lucy'],
        'octopi': {},
        'emus': {}
    },
    'plants': {},
    'other': {}
}

print("Top level keys of life dict are", life.keys())
print("Keys for life['animals]", life['animals'].keys())
print("Values for life['animals']['cats']", life['animals']['cats'])
