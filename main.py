from cmd import Cmd

class CLI(Cmd):

    storage = {}
    transaction_active = False
    storage_transaction = []

    def get_storage(self):
        if self.transaction_active:
            try:
                return self.storage_transaction[-1]
            except IndexError:
                self.init_new_transaction_storage()
                return self.storage_transaction[-1]
        else:
            return self.storage

    def set(self, key, value):
        self.get_storage()[key] = value

    def get(self, key):
        for last_transaction_storage in reversed(self.storage_transaction):
            if last_transaction_storage.has_key(key):
                return last_transaction_storage[key]
                 
        if self.storage.has_key(key):
            return self.storage[key]
        else:
            return None

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def do_set(self, args):
        """ SET something just to curt check """
        args = args.split(' ')
        if len(args) == 2:
            self.set(args[0], args[1])
        else:
            print 'The correct usage of set: set <key> <value>'

    def do_get(self, args):
        """GET"""
        args = args.split(' ')
        if len(args) == 1:
            print self.get(args[0])
        else:
            print 'The correct usage of get: get <key>'

    def do_sum(self, args):
        """SUM"""
        values = self.get_storage().values()
        values = [float(i) for i in values if self.is_number(i)]
        print reduce((lambda x, y: x + y), values)

    def do_rollback(self, args):
        """ROLLBACK"""
        if self.transaction_active:
            try:
                self.storage_transaction.pop()
                if len(self.storage_transaction) == 0:
                    self.transaction_active = False
            except IndexError:
                self.transaction_active = False
                print 'No donuts for you. There is no more rollback data'
        else:
            print 'Sorry, you are not inside a transaction so there is nothing to rollback'

    def do_commit(self, args):
        """COMMIT"""
        if self.transaction_active:
            merged = {}
            for dic in reversed(self.storage_transaction):
                merged.update(dic)
                print  'MERGED -> ', merged
            self.storage_transaction = {}
            print 'STORAGE', self.storage
            merged.update(self.storage)
            print  'MERGED -> ', merged
            print 'STORAGE', self.storage
        else:
            print 'Sorry, you are not inside a transaction so there is nothing to commit'
        
    def init_new_transaction_storage(self):
        self.storage_transaction.append({})

    def do_begin(self, args):
        """BEGIN"""
        if self.transaction_active:
            self.init_new_transaction_storage()
        else:
            self.transaction_active = True
            self.init_new_transaction_storage()

    def do_flushdb(self, args):
        """Empty the storage"""
        self.storage = {}
        self.storage_transaction = []
        print 'Hooray, no data in your storage anymore!'

    def do_storage(self, args):
        """ Print storage """
        print 'Storage', self.storage, 'Transaction', self.storage_transaction

    def do_quit(self, args):
        """Ends the simple storage"""
        print 'Exiting from pagedraw simple storage'
        raise SystemExit

if __name__ == '__main__':
    cli = CLI()
    cli.prompt = 'Pagedraw S2 > '
    cli.cmdloop('Starting Pagedraw Simple Storage...')