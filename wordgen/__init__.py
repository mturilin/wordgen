import random
from functools32 import lru_cache
from path import path
__author__ = 'mikhailturilin'

DIR = path(__file__).dirname()

def clean_lines(lines):
    return [line.rstrip() for line in lines if line != '\n']

@lru_cache()
def words_from(filename):
    with open(DIR.joinpath(filename)) as file:
        return clean_lines(file.readlines())


def adjectives():
    return words_from("adjectives.txt")

def nouns():
    return words_from("nouns.txt")

def towns():
    return words_from("towns.txt")


def compound_noun():
    adj = random.choice(adjectives())
    noun = random.choice(nouns())

    return " ".join((adj, noun)).title()

def town_name():
    return random.choice(towns()).title()

def first_name():
    return random.choice( words_from("first_names.txt")).title()