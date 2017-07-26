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

