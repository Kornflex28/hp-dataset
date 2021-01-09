import pandas as pd
import re,csv

# DataFrame : columns [movie, scene,character, dialog]
if __name__ == "__main__":
    str_filter = "[\(\[].*?[\)\]]" 
    filename = "hp1"
    with open(f"scripts/{filename}.txt",encoding="utf8") as f:
        script_lines=list(map(str.strip,re.sub(str_filter, "", f.read()).splitlines()))
    movie = script_lines.pop(0)
    scene,charcter,dialog = "","",""
    movie_data = []
    scenes=set()
    for i,line in enumerate(script_lines[:]) :
        if not(line) or ("[" in line) or ("]" in line):
            continue
        # print(l.split(":")[0])
        elif ':' not in line:
            scene = line
            scenes.add(scene)
            print("new scene",scene)
        else:
            character,dialog = map(str.strip,line.split(':',1))
            movie_data.append({'movie': movie,'scene':scene,'character':character,'dialog':dialog})
    movie_df = pd.DataFrame(movie_data)
    movie_df.to_csv(f"formatted/{filename}.csv",quoting=csv.QUOTE_ALL,index=False)
    print(scenes-set(movie_df['scene'].unique()))
