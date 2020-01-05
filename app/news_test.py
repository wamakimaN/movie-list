import unittest
from models import news,source
News = news.News
Source = source.Source

class NewsTest(unittest.TestCase):
    """
    test clacc to  test bevaviour of the News class
    """
    def setUp(self):
        self.new_news = News("somebody",
        "once told me that","not to get worked-up","https://www.onsmallthings.com","https://www.itwillsave.com/youthetrouble","2020-01-26T07:58:21Z")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, News))

class SourcesTest(unittest.TestCase):
    """
    Test Case to test the behavior of the sources class
    """
    def setUp(self):
        """
        setUp method that will run before every test
        """
        self.new_sources = Source("tmz","tmz-news", "tmz.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_sources, Source))

if __name__ == '__main__':
    unittest.main()