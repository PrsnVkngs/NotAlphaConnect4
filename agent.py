from torch import multinomal
from torch.nn import Conv2d, Linear, ReLU, Flatten, Sequential, Module


class Agent(Module):
    def __init__(self, env, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.env = env

        self.model = Sequential(
            Conv2d(2, 32, kernel_size=3, stride=1, padding=1),
            ReLU(),
            Conv2d(32, 64, kernel_size=3, stride=1, padding=1),
            ReLU(),
            Conv2d(64, 64, kernel_size=3, stride=1, padding=1),
            ReLU(),
            Conv2d(64, 64, kernel_size=3, stride=1, padding=1),
            ReLU(),
            Conv2d(64, 32, kernel_size=3, stride=1, padding=1),
            ReLU(),
            Flatten(),
            Linear(1344, 128),
            ReLU(),
            Linear(128, env.action_space.n),
        )

    def forward(self, x):
        output = self.model(x)
        return output


    def select_action(self, observation, action_mask=None):
        logits = self.forward(observation)
        if action_mask is not None:
            logits[~action_mask] = -float("inf")
        probabilities = logits.softmax(dim=-1)
        return multinomal(probabilities, 1).item()

