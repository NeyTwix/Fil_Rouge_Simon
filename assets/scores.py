try:
    import csv
except Exception as e:
    print(f"\n\n\033[91mModule csv Not Found\nPlease make sure you have installed all module before launching this file again.\n\n\033[0m")

def export_score():
    """
    This function exports the current highscores from the scores.csv file as a list of dictionaries.

    Returns:
        A list of dictionaries containing the information about each score in the scores.csv file. Each dictionary represents a single score and the keys of the dictionary correspond to the column headers in the scores.csv file.
    """
    with open('assets/scores.csv', newline='', encoding='utf-8') as csvfile:
        exported_scores = list(csv.DictReader(csvfile, delimiter=';'))
    return exported_scores


def write_score(scores_to_save):
    """
    Writes the given list of scores to the scores.csv file.

    Args:
        scores_to_save (list): A list of dictionaries containing the information
            about each score to be saved, where each dictionary represents a
            single score and the keys of the dictionary correspond to the
            column headers in the scores.csv file. Each dictionary must contain
            the "nom" and "score" keys, which correspond to the player's name
            and score, respectively.
            Example:
                [{"nom": "Player", "score": "0"}, {"nom": "player", "score": "1"}]
    Returns:
        None

    """
    already_saved_scores = []
    with open('assets/scores.csv', newline='', encoding='utf-8') as csvfile:
        already_saved_scores = list(csv.DictReader(csvfile, delimiter=';'))

    scores_to_import = already_saved_scores + scores_to_save
    with open('assets/scores.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = list(scores_to_import[0].keys())
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        for p in scores_to_import:
            writer.writerow(p)