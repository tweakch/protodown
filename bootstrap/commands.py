import argparse, pickle, os, collections

class ProtodownCommand:
    def __init__(self, name, help, func=None, aliases=[]):
        self.name = name
        self.help = help
        self.func = func
        self.aliases = aliases

class CommandsConfig(dict):
    def __init__(self):
        self.loadCommands()

    def loadCommands(self):
        dbfile = open('protodown-commands', 'rb')
        commands = pickle.load(dbfile)
        dbfile.close()
        for command, config in commands.items():
            self[command]=config
