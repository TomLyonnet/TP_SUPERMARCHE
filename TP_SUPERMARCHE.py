"""
@author: tomlyonnet
"""
from datetime import datetime
from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017/')
    Hypermarche_DB = client['Magasin']
    Supermarche = Hypermarche_DB['Produits']

    Produit1 = {"Name": "Côte de porcs",
                "Reference": 123,
                "Prix" : 5,
                "tags": ["mongodb", "python", "pymongo"],}        

    Produit2 = {"Name": "Chips",
                "Reference": 456,
                "Prix": 1,
                "tags": ["mongodb", "python", "pymongo"],}  
                
    Produit3 = {"Name": "Bière",
                "Reference": 789,
                "Prix": 2,
                "tags": ["mongodb", "python", "pymongo"],}  
        
        
    Produits = [Produit1, Produit2, Produit3]
   # Supermarche.insert(Produits),
    
    print(Produits)
    
if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017/')
    Hypermarche_DB = client['Magasin']
    Supermarche = Hypermarche_DB['Commandes']
    

    Commande1 = {"Numéro_commande": 10,
                "liste": [456, 3, 789,5],
                "tags": ["mongodb", "python", "pymongo"],
                "date": datetime.utcnow()}
    
    
    Commande2 = {"Numéro_commande": 11,
                "liste": [123, 10],
                "tags": ["mongodb", "python", "pymongo"],
                "date": datetime.utcnow()}
    
    Commande3 = {"Numéro_commande": 12,
                "liste":[456, 1, 789,3, 123, 4],
                "tags": ["mongodb", "python", "pymongo"],
                "date": datetime.utcnow()}

    Commandes = [Commande1, Commande2, Commande3]
    #Supermarche.insert(Commandes),
    
    print(Commandes)
    
if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017/')
    Hypermarche_DB = client['Magasin']
    Supermarche = Hypermarche_DB['Caisses']
    
    Caisse1 = {"Caisse_ID": 1, 
                "Produits_Commande" : [123, 1, 456, 4],}
    
    Caisse2 = {"Caisse_ID": 2, 
                "Produits_Commande" : [789, 10, 456, 2],} 
    
    Caisse3 = {"Caisse_ID": 3, 
                "Produits_Commande" : [123, 2, 456, 1, 789, 5],} 
    
    Caisses = [Caisse1, Caisse2, Caisse3]
    #Supermarche.insert(Caisses),
               
    print(Caisses)
            
                
if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017/')
    Hypermarche_DB = client['Magasin']
    Supermarche = Hypermarche_DB['Stock']

    Inventaire = {"Stock": [Produit1, 19, Produit2, 25, Produit3, 105]} 
   # Supermarche.insert(Inventaire),




        
