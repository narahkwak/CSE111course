from W5sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase, get_punctuations
import pytest

def test_get_determiner():
    singular_determiners = ["the", "one"]
    for _ in range(4):
        word = get_determiner(1)
    assert word in singular_determiners
    plural_determiners = ["some", "many"]
    for _ in range(4):
        word = get_determiner(2)
    assert word in plural_determiners

def test_get_noun():
    singular_nouns = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]
    for _ in range(20):
        noun = get_noun(1)
    assert noun in singular_nouns
    plural_nouns = ["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]
    for _ in range(20):
        noun = get_noun(2)
    assert noun in plural_nouns

def test_get_verb():
    past_verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    for _ in range(40):
        verb = get_verb(1, 'past')
    for _ in range(40):
        verb = get_verb(2, 'past')
    assert verb in past_verbs
    present_singular_verbs = ["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(40):
        verb = get_verb(1, 'present')
    assert verb in present_singular_verbs
    present_plural_verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    for _ in range(40):
        verb = get_verb(2, 'present')
    assert verb in present_plural_verbs
    future_verbs = ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    for _ in range(40):
        verb = get_verb(1, 'future')
    assert verb in future_verbs
    for _ in range(40):
        verb = get_verb(2, 'future')
    assert verb in future_verbs

def test_get_preposition():
    preposition_list = ["about", "above", "across", "after", "along","around", "at", "before", "behind", "below","beyond", "by", "despite", "except", "for","from", "in", "into", "near", "of","off", "on", "onto", "out", "over","past", "to", "under", "with", "without"]
    for _ in range(30):
        preposition = get_preposition()
    assert preposition in preposition_list

def test_get_puncutations():
    puncutuation_list = [".", "?", "!", ",", ";"]
    for _ in range(5):
        punctuation = get_punctuations()
    assert punctuation in puncutuation_list


def test_get_prepositional_phrase():
    prepositional_phrase = get_prepositional_phrase(2).split(" ")
    assert len(prepositional_phrase) == 3


pytest.main(["-v", "--tb=line", "-rN", "test_sentences.py"])