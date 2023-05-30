
import json

data = []  # Pusta lista

# Zapisz listę do pliku JSON
with open('match_id2.json', 'w') as f:
    json.dump(data, f)