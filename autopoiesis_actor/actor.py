```python
import nats
from . import commands, reactor, library, state, events

class Actor:
    def __init__(self, id):
        self.id = id
        self.current_state = state.current_state
        self.nc = nats.connect()

    def send_pheromone_signal(self, signal):
        command = commands.SendPheromoneSignal(signal)
        self.nc.publish('Pheromone Signal', command)

    def receive_pheromone_signal(self):
        def callback(msg):
            command = commands.ReceivePheromoneSignal(msg.data)
            self.process_command(command)
        self.nc.subscribe('Pheromone Signal', cb=callback)

    def process_command(self, command):
        if isinstance(command, commands.SendPheromoneSignal):
            self.current_state = library.process_signal(command.signal)
            self.emit_signal()
        elif isinstance(command, commands.ReceivePheromoneSignal):
            self.current_state = library.process_signal(command.signal)
            self.update_state()

    def emit_signal(self):
        signal = library.emit_signal(self.current_state)
        self.send_pheromone_signal(signal)

    def update_state(self):
        self.current_state = library.update_state(self.current_state)
        self.nc.publish('State Updated', self.current_state)

    def run(self):
        reactor = reactor.Reactor(self)
        reactor.run()
```