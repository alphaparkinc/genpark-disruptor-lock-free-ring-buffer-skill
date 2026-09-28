"""LMAX Disruptor Ring Buffer Engine.
100% Python Standard Library.
"""

class DisruptorRingBuffer:
    """LMAX Disruptor-style lock-free ring buffer with sequence gating."""
    def __init__(self, capacity=16):
        assert (capacity & (capacity - 1)) == 0, "Capacity must be power of 2"
        self.capacity = capacity
        self.mask = capacity - 1
        self.buffer = [None] * capacity
        self.cursor = -1
        self.consumed = -1

    def publish(self, item):
        next_seq = self.cursor + 1
        if next_seq - self.consumed > self.capacity:
            return False, self.cursor
        idx = next_seq & self.mask
        self.buffer[idx] = item
        self.cursor = next_seq
        return True, next_seq

    def consume_batch(self):
        available = self.cursor
        if self.consumed >= available:
            return []
        items = []
        for seq in range(self.consumed + 1, available + 1):
            idx = seq & self.mask
            items.append(self.buffer[idx])
        self.consumed = available
        return items
