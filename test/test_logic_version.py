import unittest
from logic import __version__


class TestLogicVersion(unittest.TestCase):
    def test_version_always_correct(self):
        self.assertEqual('0.1.0', __version__)
