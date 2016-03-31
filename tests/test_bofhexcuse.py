from bofhexcuse import bofh_excuse


def test_single():
    """make sure it generates a single excuse by default"""
    assert(len(bofh_excuse()) == 1)


def test_ten():
    """make sure it generates 10 excuses if asked"""
    assert(len(bofh_excuse(how_many=10)) == 10)
