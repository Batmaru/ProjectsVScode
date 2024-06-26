"""Obiettivo:
Implementare una classe Media che rappresenti un media generico (ad esempio, un film o un libro) e una classe derivata Film che rappresenti specificamente un film. Gli studenti dovranno anche creare oggetti di queste classi, aggiungere valutazioni e visualizzare le recensioni.

Specifiche della Classe Media:
 
Attributi:
- title (stringa): Il titolo del media.
- reviews (lista di interi): Una lista di valutazioni del media, con voti compresi tra 1 e 5, dove 1=Terribile, 2=Brutto, 3=Normale, 4=Bello, 5=Grandioso.

Metodi:
- set_title(self, title): Imposta il titolo del media.
- get_title(self): Restituisce il titolo del media.
- aggiungiValutazione(self, voto): Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5).
- getMedia(self): Calcola e restituisce la media delle valutazioni.
- getRate(self): Restituisce una stringa che descrive il giudizio medio basato sulla media delle valutazioni, ovvero mostra "Terribile" se il voto medio si avvicina a 1, "Brutto" se il voto medio si avvicina a 2, "Normale" se il voto medio si avvicina a 3, "Bello" se il voto medio si avvicina a 4, "Grandioso" se il voto medio si avvicina a 5.
- ratePercentage(self, voto): Calcola e restituisce la percentuale di un voto specifico nelle recensioni.
- recensione(self): Mostra un riassunto delle recensioni e delle valutazioni del media, stampando il titolo, il voto medio, il giudizio e le percentuali di ciascun voto. Esempio di riassunto:
 
Titolo del Film: The Shawshank Redemption
Voto Medio: 3.80
Giudizio: Bello
Terribile: 10.00%
Brutto: 10.00%
Normale: 10.00%
Bello: 30.00%
Grandioso: 40.00%

Si verifichi il funzionamento scrivendo un codice che crei almeno due oggetti di tipo Film, aggiunga a ognuno dei due almeno dieci valutazioni e richiami il metodo recensione().


"""

class Media:
    def __init__(self):
        self.reviews = []

    def __str__(self):
        return f"Titolo del Media: {self.title}"

    def set_title(self, title):
        self.title = title
        
    
    def get_title(self):
        return self.title
    
    def aggiungiValutazione(self, voto):
        if 1 <= voto <= 5:
            self.reviews.append(voto)
        else:
            print("Valutazione non valida")
    
    def get_media(self):
        if len(self.reviews) == 0:
            return 0
        else:
            return round(sum(self.reviews) / len(self.reviews),2)
        
    def get_rate(self):
        media = self.get_media()
        if media < 1.5:
            return "Terribile"
        elif media < 2.5:
            return "Brutto"
        elif media < 3.5:
            return "Normale"
        elif media < 4.5:
            return "Bello"
        else:
            return "Grandioso"
        
    def ratePercentage(self, Voto: int):
        media=0
        for n in self.reviews:
            if n == Voto:
                media= round(self.reviews.count(Voto) / len(self.reviews) * 100, 2)
        return f'{media}%'    

        
    def recensioni(self):
        print(f"Titolo del film{self.title}")
        print(f"Valutazione:{self.get_rate()}")
        print(f"Media delle valutazioni: {self.get_media()}")
        print(f"Terribile: {self.ratePercentage(1)}")
        print(f"Brutto: {self.ratePercentage(2)}")
        print(f"Normale: {self.ratePercentage(3)}")
        print(f"Bello: {self.ratePercentage(4)}")
        print(f"Grandioso: {self.ratePercentage(5)}")

        
        
class Film(Media):
    def __init__(self, title):
        super().__init__()
        self.set_title(title)

media1=Media()
film1:Film= Film(title="yeahbuddy")
film1.aggiungiValutazione(4)
film1.aggiungiValutazione(5)
film1.aggiungiValutazione(5)
film1.aggiungiValutazione(1)
print(film1.get_media())
print(film1.get_rate())
film1.recensioni()

print(film1.reviews)
print(media1)