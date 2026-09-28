from client import DisruptorRingBuffer

ring = DisruptorRingBuffer(capacity=8)
for i in range(5):
    ring.publish(f"Event-{i}")

batch = ring.consume_batch()
print(f"Consumed Batch from Disruptor ({len(batch)} items): {batch}")
