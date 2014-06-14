import random
import string

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


def company():
    return random.choice(words_from("companies.txt")).title()


def first_name():
    return random.choice(words_from("first_names.txt")).title()


def last_name():
    return random.choice(words_from("last_names.txt")).title()


def full_name():
    return " ".join((first_name(), last_name())).title()


def random_chars(chars, length):
    return ''.join([random.choice(chars) for i in range(length)])


def random_digits(length):
    return random_chars(string.digits, length)


def phone_number():
    return "(%s) %s-%s" % map(random_digits, [3, 3, 4])