import hashlib
import json
import os
import datetime
from time import time
from uuid import uuid4

class BlockChain:
   def __init__(self):
      self.blocks = []
      self.last_transaction_number = ''
      self.add_block("The Genesis Block has been created the " + str(datetime.datetime.now().timestamp))
   

   def generate_block_hash(self, block):
      return generate_hash(block.index,block.parent_hash,block.timestamp,block.transactions)

   def generate_hash(index, parent_hash, timestamp, transactions):
      #Méthode qui vous permettra de créer des blocs
      value = str(index) + str(parent_hash) + str(timestamp) + str(transactions)[1:-1]
      sha = hashlib.sha256(value.encode('utf-8'))
      return str(sha.hexdigest())
      

   def verify_hash():
      #Méthode permettant de vérifier si un hash correspond aux critères denla chaîne ou non.
      #le hash ne doit pas déjà exister
      #le hash doit systématiquement commencer par quatre “zéro” (0000)
      pass


   def add_block(self,previous_hash=None) : 
      #Méthode permettant de créer un nouveau bloc. Une fois un nouveau
      #hash trouvé, vous devrez utiliser cette méthode afin de créer un bloc, et donc
      #enregistrer un nouveau fichier JSON grâce à la méthode “save()” déjà créée. Vérifiez
      #bien que le hash en question ne soit pas déjà existant (et donc qu’un bloc homonyme
      #n’existe pas déjà).
      block = Block(
            index=self.chain[-1].index + 1,
            timestamp= datetime.datetime.now().timestamp,
            parent= self.chain[-1].hash
      )
      block.hash = previous_hash or generate_block_hash(block)
      self.chain.append(block)

      return block


   def get_block(self,hash) : 
      #Méthode permettant de récupérer un bloc en fonction de son hash
      for i in self.blocks:
         if i.hash == hash:
            return i

   def add_transaction(self,actual_block_hash, senderid, recipientid, amount) : 
      #Méthode permettant d’ajouter une transaction à un bloc. Cette
      #méthode appellera la méthode homonyme du bloc dans lequel elle sera enregistrée.
      actual_block = Block.load(actual_block_hash)
      if os.path.isfile("BlockChain_ProjectContext/BlockChain/content/wallets/" + senderid + ".json"):
         sender = Wallet.load(senderid)
         if os.path.isfile("BlockChain_ProjectContext/BlockChain/content/wallets/" + recipientid + ".json"):
            recipient = Wallet.load(recipientid)
         if sender.balance >= amount:
            #Pour procéder à une transaction, vous devez vérifier qu’il est possible d’écrire une transaction sur un bloc
            if len(actual_block.transactions) < 4:
               sender.sub_balance(amount)
               recipient.add_balance(amount)
               actual_block.add_transaction(senderid, recipientid, amount)
               sender.send(self.blocks[-1].transactions[-1][-1])
               recipient.send(self.blocks[-1].transactions[-1][-1])
               self.last_transaction_number = get_last_transaction_number(actual_block)
               actual_block.save
               sender.save
               recipient.save
               
               print("new transaction added")
            else:
               next_block = self.add_block()
               sender.sub_balance(amount)
               recipient.add_balance(amount)
               next_block.add_transaction(senderid, recipientid, amount)
               sender.send(self.blocks[-1].transactions[-1][-1])
               recipient.send(self.blocks[-1].transactions[-1][-1])
               self.last_transaction_number = get_last_transaction_number(next_block)
               sender.save
               recipient.save
               next_block.save
               print("new transaction added")
   


   def find_transaction(self,transactionN):
      for i in self.blocks:
         for j in i.transactions:
            for k in j:
               if k['tid'] == str(transactionN):
                  return i
   

   def get_last_transaction_number(self):
      return self.blocks[-1].transactions[-1][-1]['tid']
