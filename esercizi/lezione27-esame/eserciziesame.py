'''Sviluppa un sistema per la gestione dei contatti in Python che permetta agli utenti di creare, modificare, e cercare contatti basati sui numeri di telefono. Il sistema dovrà essere capace di gestire una collezione (dizionario) di contatti e i loro numeri di telefono.

1. Classe ContactManager:
Gestisce tutte le operazioni legate ai contatti.
 
Attributi:

    contacts: dict[str, list[str]] - Dizionario che ha per chiave il nome del contatto e per valore una lista di numeri di telefono. I numeri di telefono sono espressi sottoforma di stringa.

Metodi:

    create_contact(name: str, phone_numbers: list[str]): Crea un nuovo contatto, aggiungendolo al dizionario contacts con il nome specificato e una lista di numeri di telefono. Restituisce un nuovo dizionario con il solo contatto appena creato o il messaggio di errore "Errore: il contatto esiste già." se il contatto esiste già.
    add_phone_number(contact_name: str, phone_number: str): Aggiunge un numero di telefono al contatto specificato. Restituisce un nuovo dizionario con il solo contatto aggiornato o i messaggi di errore "Errore: il contatto non esiste." se il contatto non esiste oppure "Errore: il numero di telefono esiste già." se il numero di telefono è già presente per il contatto specificato.
    remove_phone_number(contact_name: str, phone_number: str): Rimuove un numero di telefono dal contatto specificato. Restituisce un nuovo dizionario con il solo contatto aggiornato o i messaggi di errore "Errore: il contatto non esiste." se il contatto non esiste oppure "Errore: il numero di telefono non è presente." se il numero di telefono non esiste per il contatto specificato.
    update_phone_number(contact_name: str, old_phone_number: str, new_phone_number: str): Sostituisce un numero di telefono con un altro nel contatto specificato. Restituisce un nuovo dizionario con il solo contatto aggiornato o i messaggi di errore "Errore: il contatto non esiste." se il contatto non esiste oppure "Errore: il numero di telefono non è presente." se il numero di telefono non esiste per il contatto specificato.
    list_contacts(): Ritorna una lista di tutte le chiavi all'interno del dizionario contacts.
    list_phone_numbers(contact_name: str): Mostra i numeri di telefono di un contatto specifico. Restituisce la lista dei numeri di telefono o il messaggio di errore "Errore: il contatto non esiste." se il contatto non esiste.
    search_contact_by_phone_number(phone_number: str): Trova e restituisce tutti i contatti che contengono un determinato numero di telefono. Restituisce una lista di tutte le chiavi all'interno del dizionario contacts che hanno il numero specificato tra i valori oppure il messaggio di errore "Nessun contatto trovato con questo numero di telefono." se nessun contatto contiene il numero di telefono.

'''
class ContactManager:
    def __init__(self):
        self.contacts:dict[str:list]={}
    
    def create_contact(self, name:str,phone_numbers: list[str]):
        new_dict={}
        if name not in self.contacts:
            self.contacts[name]=phone_numbers
            new_dict[name]=phone_numbers
            return new_dict
        else:
            return("Errore: il contatto esiste già.")

    def add_phone_number(self, contact_name: str, phone_number: str):
        new_dict={}
        if contact_name  in self.contacts:
            if phone_number not in self.contacts[contact_name]:
                self.contacts[contact_name].append(phone_number)
                new_dict[contact_name]= self.contacts[contact_name]
                return new_dict
            else:
                return("Errore: il numero di telefono esiste già.")
        else:
            return("Errore: il contatto non esiste.")

    def remove_phone_number(self,contact_name: str, phone_number: str):
        new_dict={}
        if contact_name  in self.contacts:
            if phone_number in self.contacts[contact_name]:
                self.contacts[contact_name].remove(phone_number)
                new_dict[contact_name]= self.contacts[contact_name]
                return new_dict
            else:
                return("Errore: il numero di telefono non è presente.")
        else:
            return("Errore: il contatto non esiste.") 
    
    def update_phone_number(self, contact_name: str, old_phone_number: str, new_phone_number: str):
        newdict={}
        if contact_name in self.contacts.keys():
            if old_phone_number in self.contacts[contact_name]:
                oldI= self.contacts[contact_name].index(old_phone_number)
                self.contacts[contact_name].pop(oldI)
                self.contacts[contact_name].insert(oldI,new_phone_number)
                newdict[contact_name]=self.contacts[contact_name]
                return newdict
            else:
                return("Errore: il numero di telefono non è presente.")    

        else:
            return("Errore: il contatto non esiste.")     
    def listcontacts(self):
        listk=[]
        for k in self.contacts.keys():
            listk.append(k)
        return listk
        
    def list_phone_numbers(self, contact_name: str):
        if contact_name in self.contacts:
            return self.contacts[contact_name]
        else:
            return("Errore: il contatto non esiste.")
    
    def search_contact_by_phone_number(self, phone_number: str):
        listak=[]
        for k,v in self.contacts.items():
            if phone_number in v:
                listak.append(k)
        if listak==[]:
            return("Nessun contatto trovato con questo numero di telefono.")
        else:
            return(listak)