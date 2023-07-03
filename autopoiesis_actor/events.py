```python
import nats

class Event:
    def __init__(self, name, data):
        self.name = name
        self.data = data

class PheromoneDetected(Event):
    def __init__(self, data):
        super().__init__("Pheromone Detected", data)

class NatsEvents:
    def __init__(self, nats_client):
        self.nats_client = nats_client

    async def publish_event(self, event):
        await self.nats_client.publish(event.name, event.data)

    async def subscribe_to_event(self, event_name, callback):
        await self.nats_client.subscribe(event_name, cb=callback)
```