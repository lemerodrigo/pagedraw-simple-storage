# Project Title

PageDraw Simple Storage (S2)

# TL;DR

python init.py
> help

## Structure

The simple storage was designed with a mindset to transform it into a real in memory storage engine.

In order for this evolution turns into reality, the first change must be an implementation of a socket library that is going to allow the building of a daemon of the storage engine to be running and listening for commands.

The client folder, for now, just have the CLI client, but the idea was to have all clients types that are going to be used to connect to the database engine. E.g. PHP, Ruby, JavaScript, etc.

## Assumptions

1. Following the docs, the commands are case sensitive, so the command set is invalid. The correct is SET and so on and so forth.

2. The sum method does not consider the values inside transactions.

3. The get command also search inside transactions chains.

## Getting Started

1. tar -xvzf pagedraw-simple-storage.tgz

2. cd pagedraw-simple-storage/

3. python init.py

4. Type help in the command line

### Prerequisites

Python 2.7

## Authors

* Rodrigo Leme de Mello (lemerodrigo@gmail.com)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details