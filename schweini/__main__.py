'''TODO: Documentation
'''
import argparse

# TODO: Define usage
usage = \
'''
Schweini Usage:

    add | a
        Add a new todo
    addp | ap
        Add a new project
    append
        Appends text to todo
    modify
        Modify the todo
    list | ls
        List todos
'''

schwein_parser = argparse.ArgumentParser(prog="Schweini",
                                         description="Oink, your todo list CLI",
                                         usage=usage)

