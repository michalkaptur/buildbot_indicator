from mock import Mock
import unittest

from state import State
from stat_checker import StatChecker

class GetStateTestCase(unittest.TestCase):
    def runTest(self):
        stat_checker_mock = Mock()
        stat_checker_mock.all_builds_succedded = Mock(return_value=True)
        state = State(stat_checker_mock)
        state.update_state()
        self.assertEqual(True, state.get_current_state())
        

