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

