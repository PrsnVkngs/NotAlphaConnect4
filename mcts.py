from unittest import result


class MCTree:
    def __init__(self):
        pass


class MCTNode:
    def __init__(self, state, parent=None, terminal=False):
        self.state = state
        self.children = []
        self.parent = parent
        self.visits = 0
        self.wins = 0
        self.terminal = terminal

    def add_child(self, child):
        self.children.append(child)

    def _update(self, result):
        self.visits += 1
        self.wins += result

    def update_parent(self, result):
        self._update(result)
        if self.parent:
            self.parent.update_parent(result)

    def get_value(self):
        return self.wins / self.visits

    def get_visits(self):
        return self.visits

