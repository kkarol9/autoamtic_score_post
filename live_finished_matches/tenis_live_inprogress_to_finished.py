import json

with open('tenis.json') as f:
    jsondata = json.load(f)

with open('lista_in_progress_ids.json', 'r') as f:
    in_progress_ids = json.load(f)

with open('lista_in_progress.json', 'r') as f:
    in_progress = json.load(f)

for match in jsondata['events']:
    match_id = match['id']
    status = match['status']['type']

    if match_id in in_progress_ids:
        if status == 'finished':
            tournament = match['tournament']['name']
            name_1 = match['homeTeam']['name']
            name_2 = match['awayTeam']['name']

            # Tworzenie słownika z danymi
            zawodnicy = {
                'tournament': tournament,
                'name1': name_1,
                'name2': name_2
            }

            print(f"{tournament} | {name_1} - {name_2} {status}")
            print("Zakończony")

            # Zapis do pliku JSON
            with open('zawodnicy.json', 'w') as f:
                json.dump(zawodnicy, f)

            in_progress_ids.remove(match_id)
    elif status == 'inprogress':
        in_progress_ids.append(match_id)
        in_progress.append(match)

with open('lista_in_progress_ids.json', 'w') as f:
    json.dump(in_progress_ids, f)

with open('lista_in_progress.json', 'w') as f:
    json.dump(in_progress, f)

print("Koniec")