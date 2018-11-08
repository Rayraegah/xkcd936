from xkcd936 import visualize


def test_string():
    memorable_phrase = visualize("helloworld")
    assert memorable_phrase == "this puncturable inconsequential pelican"


def test_symbol():
    memorable_phrase = visualize("h3ll0_w0rld!")
    assert memorable_phrase == "wry that cyanophyte burmese"


def test_random():
    memorable_phrase = visualize("hiywr734bk__mawe@#!")
    assert memorable_phrase == "taoist my plodding gila monster"


def test_consistancy():
    memorable_phrase_1 = visualize("helloworld")
    memorable_phrase_2 = visualize("helloworld")
    assert memorable_phrase_1 == memorable_phrase_2


def test_collision():
    memorable_phrase_1 = visualize("helloworld")
    memorable_phrase_2 = visualize("helloworLd")
    assert memorable_phrase_1 != memorable_phrase_2
