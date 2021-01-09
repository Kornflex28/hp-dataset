import pandas as pd
import re
import csv

# DataFrame: [movie, chapter,character, dialog]

if __name__ == "__main__":

    str_filter = "[\(\[\{].*?[\)\]\}]"
    character_names_map = {'Dumbledore': "Albus Dumbledore", "Flint": "Marcus Flint", 'McGonagall': "Minerva McGonagall", 'Hagrid': "Rubeus Hagrid", 'Petunia': "Petunia Dursley", 'Dudley': "Dudley Dursley", 'Vernon': "Vernon Dursley", 'Harry': "Harry Potter", 'Quirrell': "Quirinus Quirrell", 'Ollivander': "Garrick Ollivander", 'Mrs. Weasley': "Molly Weasley", 'George': "George Weasley", 'Fred': "Fred Weasley",
                           'Ginny': "Ginny Weasley", 'Ron': "Ron Weasley", 'Hermione': "Hermione Granger", 'Neville': "Neville Longbottom", 'Draco': "Draco Malfoy", 'Seamus': "Seamus Finnigan", 'Percy': "Percy Weasley", 'Nick': "Nearly Headless Nick", 'Snape': "Severus Snape", 'Hooch': "Rolanda Hooch", 'Filch': "Argus Filch", 'Oliver': "Oliver Wood", 'Flitwick': "Filius Flitwick", 'Lee': "Lee Jordan", 'Unseen Inhuman Voice': "Voldemort"}
    filename = "hp1"

    with open(f"scripts/{filename}.txt", encoding="utf8") as f:
        script_lines = list(map(str.strip, re.sub(
            str_filter, "", f.read()).splitlines()))
    movie = script_lines.pop(0)
    chapter, character, dialog = "", "", ""
    movie_data = []
    chapters = set()
    for i, line in enumerate(script_lines[:]):
        if not(line) or ("[" in line) or ("]" in line):
            continue
        # print(l.split(":")[0])
        elif ':' not in line:
            chapter = line
            chapters.add(chapter)
        else:
            characters, dialog = map(str.strip, line.split(':', 1))
            if characters == "All three":
                characters = "Harry and Hermione and Ron"
            for character in characters.split(" and "):
                if character in character_names_map:
                    movie_data.append({'movie': movie, 'chapter': chapter,
                                       'character': character_names_map[character], 'dialog': dialog})
                else:
                    movie_data.append(
                        {'movie': movie, 'chapter': chapter, 'character': character, 'dialog': dialog})
    movie_df = pd.DataFrame(movie_data)
    movie_df.to_csv(f"formatted/{filename}.csv",
                    quoting=csv.QUOTE_ALL, index=False)

    # Check if missing chapter in script original text file
    # print(chapters-set(movie_df['chapter'].unique()))

    print(movie_df.character.unique())
