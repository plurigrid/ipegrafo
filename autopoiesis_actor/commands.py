```python
class Command:
    def __init__(self, name, actor_id):
        self.name = name
        self.actor_id = actor_id

    def execute(self):
        raise NotImplementedError("Subclasses must implement this method")


class SendPheromoneSignalCommand(Command):
    def __init__(self, actor_id, signal):
        super().__init__("Send Pheromone Signal", actor_id)
        self.signal = signal

    def execute(self):
        # Code to send the pheromone signal goes here
        pass


class ReceivePheromoneSignalCommand(Command):
    def __init__(self, actor_id):
        super().__init__("Receive Pheromone Signal", actor_id)

    def execute(self):
        # Code to receive the pheromone signal goes here
        pass
```