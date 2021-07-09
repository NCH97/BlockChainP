import uuid
import json


class Wallet:
    def __init__(self, u_id = None, balance = 100, history = []):
        self.unique_id = u_id or self.generate_unique_id()
        self.balance = balance
        self.history = history # dict or list contains transactions
        self.save

    
    def generate_unique_id(self):
        id = uuid.uuid4()
        # Verifier si l id n'est pas déjà présent dans wallets
        return id

    def add_balance(self , amount):
        self.balance+= amount

    
    def sub_balance(self , amount):
        self.balance-= amount


    def send(self,transaction):
        #ajouter une transaction dans l’historique
        self.history.append(transaction)

    # Convert Wallet to JSON
    def save(self):
        dt = {}
        dt.update(vars(self))
        #Le fichier devra être sauvegardé dans le dossier “content/wallets”
        #Le nom du fichier devra correspondre à l’identifiant unique du wallet en question
        #Vous devrez intégrer l’ensemble des informations du wallet dans le fichier JSON en question
        #Veillez à bien enregistrer le fichier avec l’extension JSON
        with open("BlockChain_ProjectContext/BlockChain/content/wallets/" + str(self.unique_id) + ".json", "w") as file:
            json.dump(dt, file)

    def load(u_id):
        # try catch exeption
        f = open("BlockChain_ProjectContext/BlockChain/content/wallets/" + u_id + ".json")
        l_wallet = json.load(f)
        new_wallet = Wallet(u_id,l_wallet["balance"],l_wallet["history"])
        f.close()
        return new_wallet

