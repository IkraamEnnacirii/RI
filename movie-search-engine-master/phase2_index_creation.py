import json
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize


#nltk.download('stopwords')
#nltk.download('punkt')


#Chargement de donnees depuis le fichier movies.json
with open("movies.json", "r") as data_file:
    movies = json.load(data_file)


def getIndex(key):
    index = dict()# créer un dictionnaire vide
    #on utilise la bibliothèque NLTK pour charger les stop words en anglais à partir
    # de la fonction stopwords.words('english'
    stop_words = set(stopwords.words('english'))
    stop_words.update(['the', ':', "'s", ',', '-', '.', '!', '&', "'", '?'])
    for movie in movies:
        #Pour chaque film, elle prend la valeur associée à la clé spécifiée (key),
        # la convertit en minuscules et la divise en tokens (mots) en utilisant
        # la fonction word_tokenize de la bibliothèque NLTK
        word_tokens = word_tokenize(movie[key].lower())
        #word_tokens Cette une liste contient tous les mots présents dans le texte du film,
        #et ils sont convertis en minuscules à l'aide de lower().

        #Ces tokens word_tokens sont ensuite filtrés pour exclure les mots vides (stop words).
        #Sur chaque élément (token) dans la liste word_tokens. Si le token n'est pas présent dans
        #l'ensemble stop_words, alors il est inclus dans la liste filtered_tokens.
        filtered_tokens = [token for token in word_tokens if not token in stop_words]

        #Ensuite, la fonction parcourt les tokens filtrés et les utilise comme clés dans le dictionnaire index.
        #Si un token n'est pas déjà présent dans le dictionnaire, il est ajouté avec la valeur correspondante
        #étant une liste contenant l'ID du film en cours. Si le token est déjà présent, l'ID du film en cours
        #est simplement ajouté à la liste existante.
        for token in filtered_tokens:
            if token not in index:
                index[token] = [movie['id']]
            else:
                index[token].append(movie['id'])
    return index

def groupIndex(key):
    index = dict()
    for movie in movies:
        for i in movie[key]:
            if i.lower() not in index:
                index[i.lower()] = [movie['id']]
            else:
                index[i.lower()].append(movie['id'])
    return index
    
    

title_index = getIndex('title')
description_index = getIndex('description')
genre_index = groupIndex('genre')    
stars_index = groupIndex('stars')

year_index = dict()
for movie in movies:
    if movie['year'] not in year_index:
        year_index[movie['year']] = [movie['id']]
    else:
        year_index[movie['year']].append(movie['id'])

if __name__ == '__main__':
    print("Start of the script")
    stop_words = set(stopwords.words('english'))
    print(stop_words)
    print(title_index)
    print("End of the script")

























