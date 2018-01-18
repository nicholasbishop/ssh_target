import unittest

from ssh_target import SshTarget

class TestTarget(unittest.TestCase):
    def test_str_default_port(self):
        self.assertEqual(str(SshTarget('host', 'user')), 'user@host')
