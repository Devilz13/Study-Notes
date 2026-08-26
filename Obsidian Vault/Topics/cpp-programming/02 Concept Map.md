---
note_type: concept-map
topic: cpp-programming
created: 2026-08-26
---

# Concept map: C++ Programming

Record meaningful directed relations in prose. Treat AI-generated maps as candidates until their source links are verified.

## Prerequisite relations

- [[Concepts/Program Structure Types and Expressions]] precedes [[Concepts/Control Flow and Files]].
- [[Concepts/Control Flow and Files]] precedes [[Concepts/Functions Arrays and Vectors]].
- [[Concepts/Pointers Ownership and Memory]] supports manual linked structures and object lifetime reasoning.

## Causal or mechanistic relations

- Functions decompose behavior; classes bind state and behavior; templates generalize over compatible types.
- [[Concepts/Searching Sorting and Complexity]] exposes performance consequences of data organization.
- [[Concepts/Exceptions Templates and STL]] provides reusable abstractions that can replace error-prone manual patterns.
- [[Concepts/Linked Structures Recursion and Trees]] combines ownership, algorithms, and structural invariants.

## Contrasts and boundary cases

- Array versus vector: fixed-size/raw representation versus managed dynamic sequence.
- Composition versus inheritance: has-a reuse versus is-a substitutability.
- Iteration versus recursion: explicit loop state versus call-stack decomposition.

## Unverified candidate edges

- Add C++20/23 practices only after a current primary reference and compiler tests are registered.
