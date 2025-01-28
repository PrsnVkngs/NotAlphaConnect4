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
        logits = self.model(x)
        return logits
