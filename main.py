from environment import make_env
from agent import Agent

def main():
    env = make_env()
    agent = Agent(env)
    agent.train()