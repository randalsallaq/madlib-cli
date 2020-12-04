from madlib_cli.madlib import *


def test_true():
    content = """Make Me A Video Game!

I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb} {A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!

What are a {Large Animal} and backpacking {Small Animal} to do? Before you can help {A Girl's Name}, you'll have to collect the {Adjective} {Plural Noun} and {Adjective} {Plural Noun} that open up the {Number 1-50} worlds connected to A {First Name's} Lair. There are {Number} {Plural Noun} and {Number} {Plural Noun} in the game, along with hundreds of other"""
    actual = open_file()
    expected = content
    assert actual == expected


def test_removing():
    content = 'insert {name}'
    actual = edit_file(content)
    expected =  'insert {}'
    assert actual == expected 




def test_merge():
    text = 'insert {}'
    answer = ['name']
    actual = merge(text,answer)
    expected = 'insert name'
    assert actual == expected