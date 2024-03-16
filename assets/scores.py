try:
    import csv
except Exception as e:
    print(f"\n\n\033[91mModule csv Not Found\nPlease make sure you have installed all module before launching this file again.\n\n\033[0m")

with open('assets/scores.csv', newline='', encoding='utf-8') as csvfile:
    saved_scores = list(csv.DictReader(csvfile, delimiter=';'))

scores_to_save = saved_scores + [{"nom": "Player", "score": "0"}, {"nom": "player", "score": "1"}]

print(scores_to_save)

with open('assets/scores.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = list(scores_to_save[0].keys())
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()
    for p in scores_to_save:
        writer.writerow(p)
