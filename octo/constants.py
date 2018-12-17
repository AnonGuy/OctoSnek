"""Constant and user-defined variables needed for the program."""

from configparser import ConfigParser


config = ConfigParser()
config.read('config.ini')

CLONE_DIR = config.get('clone_dir')

