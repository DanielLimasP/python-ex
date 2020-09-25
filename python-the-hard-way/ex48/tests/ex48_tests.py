from nose.tools import *
import lexicon as lex


def test_directions():
    assert_equal(lex.scan_lexicon("north"), [("direction", "north")])
    result = lex.scan_lexicon("north south east")
    assert_equal(result, [("direction", "north"),
                          ("direction", "south"), ("direction", "east")])


def test_verbs():
    assert_equal(lex.scan_lexicon("go"), [("verb", "go")])
    result = lex.scan_lexicon("go eat kill")
    assert_equal(result, [("verb", "go"),
                          ("verb", "eat"), ("verb", "kill")])


def test_nouns():
    assert_equal(lex.scan_lexicon("princess"), [("noun", "princess")])
    result = lex.scan_lexicon("princess door cabinet")
    assert_equal(result, [("noun", "princess"),
                          ("noun", "door"), ("noun", "cabinet")])


def test_stops():
    result = lex.scan_lexicon("of the in")
    assert_equal(result, [("stop", "of"),
                          ("stop", "the"), ("stop", "in")])


def test_numbers():
    result = lex.scan_lexicon("91 100 24")
    assert_equal(result, [("number", "91"),
                          ("number", "100"), ("number", "24")])


def test_errors():
    result = lex.scan_lexicon("bitch fuck nuts")
    assert_equal(result, [("error", "bitch"),
                          ("error", "fuck"), ("error", "nuts")])
