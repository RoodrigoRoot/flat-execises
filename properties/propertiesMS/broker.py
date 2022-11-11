from typing import Dict
import asyncio
import json

from aiokafka import AIOKafkaProducer


class Broker:

    def initialize_broker(self):
        ...

    def send_message(self):
        ...

def serializer(value):
    return json.dumps(value).encode()

class KafkaBroker(Broker):

    def initialize_broker(self):
        return AIOKafkaProducer(
            bootstrap_servers='kafka-broker-1:29092',
            value_serializer=serializer,
        )

    async def send_message(self, data: Dict):
        producer = self.initialize_broker()
        await producer.start()
        try:
        # Produce message
            await producer.send("properties", data)
        finally:
            # Wait for all pending messages to be delivered or expire.
            await producer.stop()
