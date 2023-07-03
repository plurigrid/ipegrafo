```python
import nats
from . import commands, library, state, events

class Reactor:
    def __init__(self, actor_id):
        self.actor_id = actor_id
        self.current_state = state.current_state
        self.nc = nats.connect()

    def start(self):
        self.nc.subscribe("Pheromone Detected", self.process_event)

    def process_event(self, msg):
        event_name = msg.subject
        if event_name == "Pheromone Detected":
            command = commands.ReceivePheromoneSignal(msg.data)
            self.execute_command(command)

    def execute_command(self, command):
        if isinstance(command, commands.ReceivePheromoneSignal):
            signal = library.process_signal(command.signal)
            self.emit_signal(signal)
            self.update_state(signal)

    def emit_signal(self, signal):
        self.nc.publish("Pheromone Signal Received", signal)

    def update_state(self, signal):
        self.current_state = library.update_state(self.current_state, signal)
        self.nc.publish("State Updated", self.current_state)

    def stop(self):
        self.nc.close()
```