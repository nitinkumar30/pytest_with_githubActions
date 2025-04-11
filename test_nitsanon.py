import pytest


@pytest.mark.usefixtures("setup")
class TestExample:
    def test_title(self, setup):
        setup.get("http://nitsanon.epizy.com/?i=1")
        assert setup.title == "NITSANON", "Wrong title detected"

    def test_title_myGithub(self, setup):
        setup.get("https://github.com/nitinkumar30")
        print("===========\n\n", setup.title, "\n\n===========")
