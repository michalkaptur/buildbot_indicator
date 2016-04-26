class State:
    def __init__(self, state_checker):
        self.state_checker = state_checker
        self.state = None
        self.previous_state = None

    def get_current_state(self):
        return self.state

    def update_state(self):
        self.state_checker.update_builders_status
        self.previous_state = self.state
        self.state = self.state_checker.all_builds_succedded()

    def state_changed(self):
        return self.previous_state != self.state