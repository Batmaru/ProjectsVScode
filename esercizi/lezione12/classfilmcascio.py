"""
Classe:
- MovieCatalog: Gestisce tutte le operazioni legate al catalogo dei film.

    Metodi:
    - add_movie(director_name, movies): Aggiunge uno o più film a un regista specifico nel catalogo. 
    Se il regista non esiste, viene creato un nuovo record. Se il regista esiste, la sua lista di film viene aggiornata.

    - remove_movie(director_name, movie_name): Rimuove un film specifico dall'elenco dei film di un regista. Se tutti i film sono rimossi, 
    il regista può essere opzionalmente rimosso dal catalogo.

    - list_directors(): Elenca tutti i registi presenti nel catalogo.

    - get_movies_by_director(director_name): Restituisce tutti i film di un regista specifico.

    - search_movies_by_title(title): Trova tutti i film che contengono una certa parola nel titolo. Restituisce un elenco dei registi e dei 
    rispettivi film che contengono la parola cercata o un messaggio di errore se nessun film contiene la parola cercata nel titolo.
Last modified: Thursday, 30 May 2024, 12:48 PM"""

class MovieCatalog:
    def __init__(self, catalog={}):
        self.catalog: dict[str: list]=catalog
    
    def __str__(self):
        return str(self.catalog)
    
    def list_directors(self):
        list_name=[]
        for director in self.catalog:
            list_name.append(director)
        return list_name

        

    def add_movie(self, director_name: str, movies: str):
        if director_name not in self.catalog:
            self.catalog[director_name]=[movies]
        else:
            self.catalog[director_name].append(movies)

    def remove_movie(self, director_name: str, movies:str):
        if director_name in self.catalog:
            if movies in self.catalog[director_name]:
                self.catalog[director_name].remove(movies)
                if len(self.catalog[director_name]) == 0:
                    del self.catalog[director_name]

    def get_movies_by_director(self, director_name):
        lista=[n for n in self.catalog[director_name]]
        return lista

    def search_movies_by_title(self, movie):
        dict_movies={}
        for k,v in self.catalog.items():
            if movie in v:
                dict_movies[k]=movie

        return dict_movies


        
    

catalogo = MovieCatalog(catalog={})

catalogo.add_movie("leonardo_dicaprio","shu")
catalogo.add_movie("leonardo_dicaprio","shu2")
catalogo.add_movie("ale","shu")
print(catalogo)

print(catalogo.list_directors())
print(catalogo.get_movies_by_director("leonardo_dicaprio"))
print(catalogo.search_movies_by_title("shu"))


