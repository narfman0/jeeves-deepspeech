import sys
import unittest
try:
    from unittest import mock
except ImportError:
    from mock import mock
from jasper_deepspeech.stt import DeepSpeechSTT


class TestJasperDeepSpeech(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        stt = DeepSpeechSTT()
        self.assertFalse(stt is None)


if __name__ == '__main__':
    unittest.main()
