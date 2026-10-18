---
note_type: misconceptions
topic: cpp-programming
created: 2026-08-26
---

# Misconceptions: C++ Programming

Record the incorrect model, why it was tempting, corrective evidence, and a transfer question that distinguishes the models.

| Candidate misconception | Corrective distinction | Transfer check |
| --- | --- | --- |
| A pointer is the object | A pointer stores an address or null state; lifetime and ownership are separate questions | Who destroys the pointed-to object, and can the pointer outlive it? |
| Inheritance is the main form of code reuse | Inheritance models substitutability; composition and generic algorithms often provide safer reuse | Can the derived type satisfy every contract of the base? |
| Code that compiles is correct | Compilation checks limited language constraints, not requirements, logic, safety, or edge cases | Which test falsifies the current assumption? |
