from mock import Mock
import unittest

from state import State

class BaseStateTestCase(unittest.TestCase):
    def setUp(self):
        self.stat_checker_mock = Mock()

class GetStateTestCase(BaseStateTestCase):
    def runTest(self):
        self.stat_checker_mock.all_builds_succedded = Mock(return_value=True)
        state = State(self.stat_checker_mock)
        state.update_state()
        self.assertEqual(True, state.get_current_state())

class StateChangedTestCase(BaseStateTestCase):
    def runTest(self):
        self.stat_checker_mock.all_builds_succedded = Mock(return_value=True)
        state = State(self.stat_checker_mock)
        state.update_state()
        self.assertEqual(True, state.get_current_state())
        self.stat_checker_mock.all_builds_succedded = Mock(return_value=False)
        state.update_state()
        self.assertEqual(False, state.get_current_state())
        self.assertEqual(True, state.state_changed())

class SameStateAfterUpdateTestCase(BaseStateTestCase):
    def runTest(self):
        self.stat_checker_mock.all_builds_succedded = Mock(return_value=True)
        state = State(self.stat_checker_mock)
        state.update_state()
        self.assertEqual(True, state.get_current_state())
        self.stat_checker_mock.all_builds_succedded = Mock(return_value=True)
        state.update_state()
        self.assertEqual(True, state.get_current_state())
        self.assertEqual(False, state.state_changed())


