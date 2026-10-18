---
note_type: misconceptions
topic: networking-fundamentals
created: 2026-08-26
---

# Misconceptions: Networking Fundamentals

Record the incorrect model, why it was tempting, corrective evidence, and a transfer question that distinguishes the models.

| Candidate misconception | Corrective distinction | Transfer check |
| --- | --- | --- |
| The OSI model is the packet's literal travel path | It is a responsibility model; implementation uses interacting protocol layers | At which layer would a wrong default gateway appear, and which lower layers may still work? |
| A subnet mask is just another address | It marks the network/host boundary used in reachability decisions | Can two hosts share a switch yet require a router because of their masks? |
| Ping proves the whole application works | Ping checks a narrower ICMP path and does not validate every application dependency | What additional test distinguishes DNS failure from transport or application failure? |
