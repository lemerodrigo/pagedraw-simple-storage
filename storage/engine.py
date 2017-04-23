# -*- coding: utf-8 -*-

"""PageDraw Simple Storage Engine.

Author:
    Rodrigo Leme de Mello
    lemerodrigo@gmail.com

Version:
    1.0

Last revision:
    Sunday, April 23rd, 2017

ToDo:
    * Implement a daemon usign sockets
    * Receive commands via socket instead of object binding 
    * Implement TTL for data
    * Develop a garbage collector to eliminate expired data
    * Extend data types to allow hashes, sorted sets and lists 
"""

class Core():

    storage = {}
    storage_transactions_chain = []
    transaction_active = False

    def get_data(self):
        """Returns the data from the current storage"""
        return self.storage

    def get_active_data_structure(self):
        """Returns the data structure that iscurrently being used by the engine"""
        if self.transaction_active:
            try:
                # If a transaction is active, we always return the last transaction in the transaction chain
                return self.storage_transactions_chain[-1]
            except IndexError:
                self.init_new_transaction_storage()
                return self.storage_transactions_chain[-1]
        else:
            return self.storage

    def set(self, key, value):
        """Sets a key value pair into the storage"""
        if not key or not value:
            raise ValueError('Expected a key and a value')
        else:
            self.get_active_data_structure()[key] = value

    def get(self, key):
        # Going through all storages to check if we have the searched key
        for last_transaction_storage in reversed(self.storage_transactions_chain):
            if last_transaction_storage.has_key(key):
                return last_transaction_storage[key]
        
        # If the keys was not found in the transaction chain, search in current storage
        if self.storage.has_key(key):
            return self.storage[key]
        else:
            return None

    def rollback(self):
        if self.transaction_active:
            try:
                # Remove the last data structure from the transaction chain
                self.storage_transactions_chain.pop()
                if len(self.storage_transactions_chain) == 0:
                    self.transaction_active = False
            except IndexError:
                self.transaction_active = False
                print 'No donuts for you. There is no more rollback data'
        else:
            print 'Sorry, you are not inside a transaction so there is nothing to rollback'

    def commit(self):
        if self.transaction_active:
            merged = {}
            # Merging from right to left all data structures (dictionaries) in the transaction chain
            for dic in reversed(self.storage_transactions_chain):
                merged.update(dic)
            self.reset_transaction_chain()
            # The final merge with the current storage
            merged.update(self.storage)
            self.storage = merged
        else:
            print 'Sorry, you are not inside a transaction so there is nothing to commit'
    
    def reset_transaction_chain(self):
        self.storage_transactions_chain = []
        self.transaction_active = False
        
    def init_new_transaction_storage(self):
        self.storage_transactions_chain.append({})

    def begin(self):
        if self.transaction_active:
            self.init_new_transaction_storage()
        else:
            self.transaction_active = True
            self.init_new_transaction_storage()

    def flushdb(self):
        self.storage = {}
        self.reset_transaction_chain()
        print 'Hooray, no data in your storage anymore!'

    def show(self):
        """ Print storage """
        print 'Storage', self.storage, 'Transaction chain', self.storage_transactions_chain