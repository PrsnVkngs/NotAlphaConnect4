import pickle

ACTION_SPACE = 7

class MCTree:
    def __init__(self):
        self.root = MCTNode(None, None, False)
        self.current_node = self.root
        self.simulated_node = None

    def step_tree(self, action, simulate=False):
        """Move the tree one step forward"""
        if action not in [child.action for child in self.current_node.children]:
            child = MCTNode(action, self.current_node)
            self.current_node.add_child(child)
        else:
            child = [child for child in self.current_node.children if child.action == action][0]

        if simulate:
            self.simulated_node = child
        else:
            self.current_node = child

    def get_best_action(self, simulate=False):
        """Get the action with the highest visit count"""
        if simulate:
            node = self.simulated_node
        else:
            node = self.current_node

        return max(node.children, key=lambda child: child.get_value()).action

    def get_random_action(self, simulate=False):
        """Get a random action from the current node's children"""
        if simulate:
            node = self.simulated_node
        else:
            node = self.current_node



    def save_tree(self, filename="mcts_tree.pkl"):
        """Serialize the entire MCTS tree to a file"""
        with open(filename, 'wb') as f:
            # Only need to save root - children/parent refs are preserved
            pickle.dump(self.root, f, protocol=pickle.HIGHEST_PROTOCOL)

    def load_tree(self, filename="mcts_tree.pkl"):
        """Load a previously saved tree structure"""
        with open(filename, 'rb') as f:
            self.root = pickle.load(f)



class MCTNode:
    def __init__(self, action, parent=None, terminal=False):
        self.action = action
        self.children = []
        self.parent = parent
        self.visits = 0
        self.wins = 0
        self.actions = ACTION_SPACE
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

    def is_fully_expanded(self) -> bool:
        return len(self.children) == self.actions

