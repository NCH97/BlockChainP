import os
import json

class Block:
    transaction_number = 1
    def __init__(self,index, timestamp, parent):
        
        #self.base_hash
        self.index = index
        self.timestamp = timestamp
        self.hash = ''
        self.parent_hash = parent # previous bloc

        self.size = 0 # max 256 000 octets and get Json file size
        self.transactions = [] # must check if bloc have suffisant space on size
        self.save

    def  check_hash(): # check if hash bloc is correct with base_hash
        pass


    def add_transaction(self, sender, recipient, amount):
        #Méthode permettant d’ajouter une transaction au bloc. 
        # Une transaction concerne un wallet émetteur, un wallet récepteur et doit également contenir un montant.
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
            'tid' : self.__class__.transaction_number
        }
        self.transactions.append(transaction)
        self.__class__.transaction_number += 1
        #return self.last_block['index'] + 1##############################


    def get_transaction(self, number):
        #Méthode permettant de récupérer une transaction par rapport à
        #son numéro (CF point “transactions” ci-dessous)
        return self.transactions[number - 1]

    def get_weight(self):
        #Méthode permettant de récupérer le poids total du bloc.
        sizeBlock = os.stat('BlockChain_ProjectContext\\BlockChain\\content\\blocs\\' + str(self.hash) + '.json').st_size
        return sizeBlock

    def save(self):
        dt = {}
        dt.update(vars(self))
        with open("BlockChain_ProjectContext/BlockChain/content/blocs/" + str(self.hash) + ".json", "w") as file:
            json.dump(dt, file)

    def load(hash) : 
        #Similaire à la méthode homonyme des Wallets, l’identifiant unique ici étant
        #l’attribut “hash”.
        # try catch exeption
        f = open("BlockChain_ProjectContext/BlockChain/content/blocs/" + str(hash) + ".json")
        l_bloc = json.load(f)
        new_bloc = Block(hash,l_bloc["parent_hash"],l_bloc["transactions"])
        f.close()
        return new_bloc


