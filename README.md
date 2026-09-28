# genpark-disruptor-lock-free-ring-buffer-skill

Agent Skill implementing the **LMAX Disruptor Lock-Free Ring Buffer Pattern** with sequence barriers, power-of-two bitwise masking, and batch consumption.

## Architectural Overview
```mermaid
flowchart TD
    Producer["Producer Claims Sequence"] --> Mask["Bitwise Masking: seq & (Capacity - 1)"]
    Mask --> Slot["Write to Fixed Pre-allocated Slot"]
    Slot --> Cursor["Advance Producer Cursor"]
    Cursor --> Barrier["Consumer Sequence Barrier"]
    Barrier --> Batch["Zero-Copy Batch Consumption"]
```
