import unittest
from mock import *
from databaseFunc import displayAll,search,keyword

class Testdb(unittest.TestCase):

    def test_displayAll(self):
        with patch('databaseFunc.fetchAll') as mocked_fetchAll:
            mocked_fetchAll.return_value = [
                'Dog',
                'Dog Town',
                'Dog City',
                'Ball',
            ]
            results = displayAll()
            expected = 4
            self.assertEqual(results, expected)

    def test_search_True(self):
        with patch('databaseFunc.fetchAll') as mocked_fetchAll:
            mocked_fetchAll.return_value = [
                'Dog',
                'Dog Town',
                'Dog City',
                'Ball',
            ]
            results = search('Dog')
            self.assertTrue(results)

    def test_search_False(self):
        with patch('databaseFunc.fetchAll') as mocked_fetchAll:
            mocked_fetchAll.return_value = [
                'Dog',
                'Dog Town',
                'Dog City',
                'Ball',
            ]
        results = search('Cat')
        expected = None
        self.assertEqual(results,expected)

    def test_keyword_True(self):
        with patch('databaseFunc.fetchAll') as mocked_fetchAll:
            mocked_fetchAll.return_value = [
                'Dog',
                'Dog Town',
                'Dog City',
                'Ball',
            ]
            results = keyword('Dog')
            expected = ['Dog', 'Dog Town', 'Dog City']
            self.assertEqual(results,expected)

    def test_keyword_False(self):
        with patch('databaseFunc.fetchAll') as mocked_fetchAll:
            mocked_fetchAll.return_value = [
                'Dog',
                'Dog Town',
                'Dog City',
                'Ball',
            ]
            results = keyword('Cat')
            expected = []
            self.assertEqual(results,expected)

if __name__ == '__main__':
    unittest.main()