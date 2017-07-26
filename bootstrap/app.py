#!/usr/bin/env python3
"The protodown app module"

from bootstrap.build import Arguments

def init(arguments):
    return "Initialized empty repository"

def config(arguments):
    print(arguments)
    if(arguments.option=='help'):
        return 'display config help'
    else:
        s = Template("setting $option to $value")
        return s.substitute(option=arguments.option,value=arguments.value)

def lookup(arguments):
    return "lookup tests"

def resolve(arguments):
    return "Looking for UC0..."

def generate(arguments):
    return "Generating prototype..."

def run(arguments):
    return "Starting application..."

class Protodown(object):
    """generate prototypes from markdown"""
    def __init__(self):
        super(Protodown, self).__init__()
        self.arguments=Arguments()

        #This should be in the kernel.
        self.arguments['config'].set_defaults(func=config);
        self.arguments['resolve'].set_defaults(func=resolve);
        self.arguments['generate'].set_defaults(func=generate);
        self.arguments['run'].set_defaults(func=run);
        self.arguments['lookup'].set_defaults(func=lookup);

        self.args=self.arguments.get_args()

    def print_help(self):
        self.arguments.print_help()
#group = parser.add_argument_group('Available protodown commands')
#group.add_argument('init', help="Create an empty Protodown repository or reinitialize an existing one")
#group.add_argument('config', help="Configure your protodown repository")
#group.add_argument('resolve', help="Find solutions for your prototype")
#group.add_argument('generate', help="Let the magic happen")
#group.add_argument('run', help="Start your prototype")
