import json

# Zapisanie listy do pliku
my_list_ids = []
with open('lista_in_progress_ids.json', 'w') as f:
    json.dump(my_list_ids, f)

my_list = []
with open('lista_in_progress.json', 'w') as f:
    json.dump(my_list, f)

# Odczytanie listy z pliku
with open('my_list.json', 'r') as f:
    m_list = json.load(f)


m_list.append(56)

print(m_list)