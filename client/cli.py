# -*- coding: utf-8 -*-

"""Command line interface (client) for accessing PageDraw Simple Storage.

Author:
    Rodrigo Leme de Mello
    lemerodrigo@gmail.com

Version:
    1.0

Last revision:
    Sunday, April 23rd, 2017
"""

# BuiltIn Modules
import sys
import os
from cmd import Cmd

# My modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
from helpers import functions

class CursorHandler(Cmd):

    # As I still don't have a storage listening in some TCP port,
    # I have to bind the storage to the client.
    obj_storage = None
    def set_storage(self, obj_storage):
        self.obj_storage = obj_storage

    def do_set(self, args):
        """Sends the set command to the storage

        Args:
            key: string
            value: any

        Usage:
            set <key> <value>

        Example:
            > set x 8
            >
        """

        args = args.split(' ')
        if len(args) == 2:
            self.obj_storage.set(args[0], args[1])
        else:
            print self.do_set.__doc__

    def do_get(self, args):
        """Sends the get command to the storage

        Args:
            key: string

        Usage:
            get <key>
        
        Return:
            <value> corresponding with the passed key

        Example:
            > get x
            > 8
        """

        args = args.split(' ')
        if len(args) == 1 and args[0]:
            print self.obj_storage.get(args[0])
        else:
            print self.do_get.__doc__

    def do_sum(self, args):
        """Sum all numeric values stored in the current storage (values inside transactions are ignored)

        Usage:
            sum

        Return:
            float number

        Example:
            > sum
            > 8.0
        """
        values = self.obj_storage.get_data().values()
        values = [float(i) for i in values if functions.is_number(i)]
        if values:
            print reduce((lambda x, y: x + y), values)
        else:
            print 'Impossible to sum the values in the storage'

    def do_begin(self, args):
        """Initialize a transaction sequence
        
        Usage:
            begin
        
        Example:
            > begin
            > set x 8
        """
        self.obj_storage.begin()

    def do_rollback(self, args):
        """Process a rollback discarding the last transactions inputs
        
        Usage:
            rollback

        Example:
            > begin
            > set x 8
            > rollback
        """
        self.obj_storage.rollback()

    def do_commit(self, args):
        """Process all pending transactions merging with the current storage
        
        Usage:
            commit

        Example:
            > begin
            > set x 8
            > commit
        """
        self.obj_storage.commit()
        
    def do_flushdb(self, args):
        """Flush all data stored and also ends all transactions

        Usage:
            flushdb
        """
        self.obj_storage.flushdb()

    def do_show(self, args):
        """Show the data strcture of the storage

        Usage:
            show
        """
        self.obj_storage.show()

    def do_quit(self, args):
        """Ends the simple storage"""
        print 'Exiting from pagedraw simple storage'
        raise SystemExit