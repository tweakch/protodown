import argparse, textwrap, collections
from string import Template
from bootstrap.commands import CommandsConfig, ProtodownCommand

"""recursively add subparsers"""
def parseCommands(parser, commandsConfig):
    subparsers = parser.add_subparsers(title="my subparsers") #add subparsers to parser

    for command, config in commandsConfig.items():
        command_parser=subparsers.add_parser(
            command,
            help=config['help'],
            aliases=config['aliases'])

        if 'subcommands' in config:
            subcommands=config['subcommands']
            parseCommands(command_parser, subcommands)
        if 'arguments' in config:
            arguments=config['arguments']


    return subparsers

class Arguments():
    """docstring for Arguments."""

    def __init__(self):
        self.parser=argparse.ArgumentParser(
            description="Parser description",
            epilog="Epilog of the parser class",
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        self.commandsConfig=CommandsConfig()
        self.subparsers=parseCommands(self.parser, self.commandsConfig)

    def __getitem__(self,key):
        if key in self.subparsers.choices:
            return self.subparsers.choices[key]
        else:
             raise KeyError('Command "{0}" was not configured.'.format(key))

    def get_args(self):
        return self.parser.parse_args()

    def print_help(self):
        self.parser.print_help()
