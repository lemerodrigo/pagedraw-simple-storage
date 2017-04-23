# Project Title

PageDraw Simple Storage (S2)

## Structure

The simple storage was designed with a evolution mindset to work in the future as a real in memory storage engine.

In order for this evolution turns into reality, the first change must be an implementation of a socket library that is going to allow the building of a daemon of the storage engine to be running and listening for commands.

The client folder/module, for now, just have the cli client, but the idea was to have all clients types that are going to be used to connect to the database. E.g. PHP, Ruby, JavaScript, etc.

## Assumptions

1. Following the docs, the commands are case sensitive, so the command set is invalid. The correct is SET and so on and so forth.

2. The sum method does not consider the values inside transactions.

3. 

## Getting Started

1. tar -xvzf pagedraw-simple-storage.tgz

2. cd pagedraw-simple-storage/

3. python init.py

### Prerequisites

Python 2.7

## Running the tests

python tests.py

## Authors

* Rodrigo Leme de Mello (lemerodrigo@gmail.com)

## License

This project is licensed under the MIT License