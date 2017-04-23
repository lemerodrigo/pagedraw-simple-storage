# -*- coding: utf-8 -*-

# My modules
from storage import engine
from client import cli

if __name__ == '__main__':
    storage = engine.Core()
    client = cli.CursorHandler()
    client.set_storage(storage)
    client.prompt = 'PageDraw S2 > '
    client.cmdloop('Starting PageDraw Simple Storage CLI')