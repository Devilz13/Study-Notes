# Change report: research-study ecosystem and PR review fixes

Baseline reviewed commit: `51e1bb858524134d4144ebf7d9bdb31c7069dd9c`.

## P2 findings

| Finding | Implementation files | Focused regression coverage |
| --- | --- | --- |
| Regenerated untracked files escaped CI | `.github/workflows/validate-study-structure.yml`, `scripts/check_generated.py` | `tests/test_review_regressions.py`: deleted-in-commit then regenerated; missing output; modified output; staged output; clean output |
| Topics were permanently limited to one source | `scripts/validate_study_structure.py` | `tests/test_review_regressions.py`: multiple accepted/context/rejected rows and multiple source notes; canonical anchor; bad supplemental ID; duplicate scoped ID; missing source note; rejection reason |

The manifest generator supports all configured notebook scopes. The new validator validates every ledger row, preserves the canonical retained-book row, and checks one concrete source note per curated source. It does not impose a one-row or one-note limit on a topic.

## Validation

- 17 behavioral tests pass locally.
- Seven notebook packages and all vault/skill links validate.
- All four retained PDF hashes match the reviewed commit bytes.
- Unified skill metadata validates. The OCR client help command runs.
- Independent local skill exercise preserved all originals, organized two files, and held two ambiguous files.
- GitHub CI must be checked on the pushed head. Green checks on the baseline are not used as evidence for these fixes.

## Remaining ecosystem acceptance gaps

- The later file batch is not supplied. New notebooks remain empty.
- Obsidian and Syncthing still need setup and tests on the actual Windows and Android devices.
- No persistent assistant-to-device bridge or OCR model endpoint is deployed.
- Check existing notebook sharing and source identity before adding private sources. Keep live account results in the private setup record.
- The Windows folder supplied in chat is not mounted in this cloud session. See `docs/WINDOWS_SETUP.md`.

## Complete file changes from the reviewed commit

`R` records retain the previous and new paths. `A`, `M`, and `D` mean added, modified, and deleted. This report is also added as `docs/CHANGE_REPORT.md`.

```text
M	.github/workflows/validate-study-structure.yml
M	.gitignore
A	AGENTS.md
D	Academic Source Library/computing-research-methods/00 Curated Source Guide.md
D	Academic Source Library/cpp-programming/00 Curated Source Guide.md
D	Academic Source Library/networking-fundamentals/00 Curated Source Guide.md
D	Academic Source Library/systems-analysis-and-design/00 Curated Source Guide.md
A	CLAUDE.md
A	Obsidian Vault/.obsidian/app.json
A	Obsidian Vault/.obsidian/core-plugins.json
M	Obsidian Vault/.stignore
A	Obsidian Vault/00 Samuel Home.md
M	Obsidian Vault/00 Study Home.md
A	Obsidian Vault/Samuel/Samuel Study/00 Study Home.md
R077	Obsidian Vault/Topics/cross-topic-index/00 Topic Map.md	Obsidian Vault/Samuel/Samuel Study/Cross-topic Index/00 Topic Map.md
R100	Obsidian Vault/Topics/cross-topic-index/01 Research Questions.md	Obsidian Vault/Samuel/Samuel Study/Cross-topic Index/01 Research Questions.md
R069	Obsidian Vault/Topics/cross-topic-index/02 Concept Map.md	Obsidian Vault/Samuel/Samuel Study/Cross-topic Index/02 Concept Map.md
R100	Obsidian Vault/Topics/cross-topic-index/03 Evidence Ledger.csv	Obsidian Vault/Samuel/Samuel Study/Cross-topic Index/03 Evidence Ledger.csv
R100	Obsidian Vault/Topics/cross-topic-index/04 Contradictions.md	Obsidian Vault/Samuel/Samuel Study/Cross-topic Index/04 Contradictions.md
R100	Obsidian Vault/Topics/cross-topic-index/05 Misconceptions.md	Obsidian Vault/Samuel/Samuel Study/Cross-topic Index/05 Misconceptions.md
R100	Obsidian Vault/Topics/cross-topic-index/06 Recall Queue.md	Obsidian Vault/Samuel/Samuel Study/Cross-topic Index/06 Recall Queue.md
A	Obsidian Vault/Samuel/Samuel Study/Cross-topic Index/Concepts/.gitkeep
R059	Obsidian Vault/Topics/cross-topic-index/Concepts/Abstraction Across Layers and Models.md	Obsidian Vault/Samuel/Samuel Study/Cross-topic Index/Concepts/Abstraction Across Layers and Models.md
R052	Obsidian Vault/Topics/cross-topic-index/Concepts/Decomposition Interfaces and Traceability.md	Obsidian Vault/Samuel/Samuel Study/Cross-topic Index/Concepts/Decomposition Interfaces and Traceability.md
R046	Obsidian Vault/Topics/cross-topic-index/Concepts/Evidence Validation and Verification.md	Obsidian Vault/Samuel/Samuel Study/Cross-topic Index/Concepts/Evidence Validation and Verification.md
R100	Obsidian Vault/Topics/cross-topic-index/Concepts/Learning Loop and Memory Promotion.md	Obsidian Vault/Samuel/Samuel Study/Cross-topic Index/Concepts/Learning Loop and Memory Promotion.md
R047	Obsidian Vault/Topics/cross-topic-index/Concepts/Reliability Security and Failure Diagnosis.md	Obsidian Vault/Samuel/Samuel Study/Cross-topic Index/Concepts/Reliability Security and Failure Diagnosis.md
R100	Obsidian Vault/Topics/cross-topic-index/Concepts/_Concept Note Template.md	Obsidian Vault/Samuel/Samuel Study/Cross-topic Index/Concepts/_Concept Note Template.md
A	Obsidian Vault/Samuel/Samuel Study/Cross-topic Index/Exports/NotebookLM/.gitkeep
A	Obsidian Vault/Samuel/Samuel Study/Cross-topic Index/Exports/NotebookLM/00 Curated Source Guide.md
A	Obsidian Vault/Samuel/Samuel Study/Cross-topic Index/Exports/NotebookLM/source-manifest.csv
A	Obsidian Vault/Samuel/Samuel Study/Cross-topic Index/Sessions/.gitkeep
R100	Obsidian Vault/Topics/cross-topic-index/Sessions/_Session Note Template.md	Obsidian Vault/Samuel/Samuel Study/Cross-topic Index/Sessions/_Session Note Template.md
A	Obsidian Vault/Samuel/Samuel Study/Cross-topic Index/Sources/.gitkeep
R100	Obsidian Vault/Topics/cross-topic-index/Sources/_Source Note Template.md	Obsidian Vault/Samuel/Samuel Study/Cross-topic Index/Sources/_Source Note Template.md
A	Obsidian Vault/Samuel/Samuel Study/ICT111/00 Topic Map.md
A	Obsidian Vault/Samuel/Samuel Study/ICT111/01 Research Questions.md
A	Obsidian Vault/Samuel/Samuel Study/ICT111/02 Concept Map.md
A	Obsidian Vault/Samuel/Samuel Study/ICT111/03 Evidence Ledger.csv
A	Obsidian Vault/Samuel/Samuel Study/ICT111/04 Contradictions.md
A	Obsidian Vault/Samuel/Samuel Study/ICT111/05 Misconceptions.md
A	Obsidian Vault/Samuel/Samuel Study/ICT111/06 Recall Queue.md
A	Obsidian Vault/Samuel/Samuel Study/ICT111/Assignments/Assignment 1/00 Assignment Map.md
A	Obsidian Vault/Samuel/Samuel Study/ICT111/Assignments/Assignment 2/00 Assignment Map.md
A	Obsidian Vault/Samuel/Samuel Study/ICT111/Concepts/.gitkeep
A	Obsidian Vault/Samuel/Samuel Study/ICT111/Exports/NotebookLM/.gitkeep
A	Obsidian Vault/Samuel/Samuel Study/ICT111/Exports/NotebookLM/00 Curated Source Guide.md
A	Obsidian Vault/Samuel/Samuel Study/ICT111/Exports/NotebookLM/source-manifest.csv
A	Obsidian Vault/Samuel/Samuel Study/ICT111/Sessions/.gitkeep
A	Obsidian Vault/Samuel/Samuel Study/ICT111/Slides/Lesson1/00 Lesson Map.md
A	Obsidian Vault/Samuel/Samuel Study/ICT111/Slides/Lesson2/00 Lesson Map.md
A	Obsidian Vault/Samuel/Samuel Study/ICT111/Slides/Lesson3/00 Lesson Map.md
A	Obsidian Vault/Samuel/Samuel Study/ICT111/Slides/Lesson4/00 Lesson Map.md
A	Obsidian Vault/Samuel/Samuel Study/ICT111/Slides/Lesson5/00 Lesson Map.md
A	Obsidian Vault/Samuel/Samuel Study/ICT111/Slides/Lesson6/00 Lesson Map.md
A	Obsidian Vault/Samuel/Samuel Study/ICT111/Slides/Lesson7/00 Lesson Map.md
A	Obsidian Vault/Samuel/Samuel Study/ICT111/Sources/.gitkeep
A	Obsidian Vault/Samuel/Samuel Study/ICT201/00 Topic Map.md
A	Obsidian Vault/Samuel/Samuel Study/ICT201/01 Research Questions.md
A	Obsidian Vault/Samuel/Samuel Study/ICT201/02 Concept Map.md
A	Obsidian Vault/Samuel/Samuel Study/ICT201/03 Evidence Ledger.csv
A	Obsidian Vault/Samuel/Samuel Study/ICT201/04 Contradictions.md
A	Obsidian Vault/Samuel/Samuel Study/ICT201/05 Misconceptions.md
A	Obsidian Vault/Samuel/Samuel Study/ICT201/06 Recall Queue.md
A	Obsidian Vault/Samuel/Samuel Study/ICT201/Assignments/Assignment 1/00 Assignment Map.md
A	Obsidian Vault/Samuel/Samuel Study/ICT201/Assignments/Assignment 2/00 Assignment Map.md
A	Obsidian Vault/Samuel/Samuel Study/ICT201/Concepts/.gitkeep
A	Obsidian Vault/Samuel/Samuel Study/ICT201/Exports/NotebookLM/.gitkeep
A	Obsidian Vault/Samuel/Samuel Study/ICT201/Exports/NotebookLM/00 Curated Source Guide.md
A	Obsidian Vault/Samuel/Samuel Study/ICT201/Exports/NotebookLM/source-manifest.csv
A	Obsidian Vault/Samuel/Samuel Study/ICT201/Sessions/.gitkeep
A	Obsidian Vault/Samuel/Samuel Study/ICT201/Slides/Lesson1/00 Lesson Map.md
A	Obsidian Vault/Samuel/Samuel Study/ICT201/Slides/Lesson2/00 Lesson Map.md
A	Obsidian Vault/Samuel/Samuel Study/ICT201/Slides/Lesson3/00 Lesson Map.md
A	Obsidian Vault/Samuel/Samuel Study/ICT201/Slides/Lesson4/00 Lesson Map.md
A	Obsidian Vault/Samuel/Samuel Study/ICT201/Slides/Lesson5/00 Lesson Map.md
A	Obsidian Vault/Samuel/Samuel Study/ICT201/Slides/Lesson6/00 Lesson Map.md
A	Obsidian Vault/Samuel/Samuel Study/ICT201/Slides/Lesson7/00 Lesson Map.md
A	Obsidian Vault/Samuel/Samuel Study/ICT201/Sources/.gitkeep
R085	Obsidian Vault/Topics/computing-research-methods/00 Topic Map.md	Obsidian Vault/Samuel/Samuel Study/Shared References/computing-research-methods/00 Topic Map.md
R100	Obsidian Vault/Topics/computing-research-methods/01 Research Questions.md	Obsidian Vault/Samuel/Samuel Study/Shared References/computing-research-methods/01 Research Questions.md
R100	Obsidian Vault/Topics/computing-research-methods/02 Concept Map.md	Obsidian Vault/Samuel/Samuel Study/Shared References/computing-research-methods/02 Concept Map.md
R068	Obsidian Vault/Topics/computing-research-methods/03 Evidence Ledger.csv	Obsidian Vault/Samuel/Samuel Study/Shared References/computing-research-methods/03 Evidence Ledger.csv
R100	Obsidian Vault/Topics/computing-research-methods/04 Contradictions.md	Obsidian Vault/Samuel/Samuel Study/Shared References/computing-research-methods/04 Contradictions.md
R100	Obsidian Vault/Topics/computing-research-methods/05 Misconceptions.md	Obsidian Vault/Samuel/Samuel Study/Shared References/computing-research-methods/05 Misconceptions.md
R100	Obsidian Vault/Topics/computing-research-methods/06 Recall Queue.md	Obsidian Vault/Samuel/Samuel Study/Shared References/computing-research-methods/06 Recall Queue.md
A	Obsidian Vault/Samuel/Samuel Study/Shared References/computing-research-methods/Concepts/.gitkeep
R100	Obsidian Vault/Topics/computing-research-methods/Concepts/Data Analysis and Paradigms.md	Obsidian Vault/Samuel/Samuel Study/Shared References/computing-research-methods/Concepts/Data Analysis and Paradigms.md
R100	Obsidian Vault/Topics/computing-research-methods/Concepts/Ethics and Participants.md	Obsidian Vault/Samuel/Samuel Study/Shared References/computing-research-methods/Concepts/Ethics and Participants.md
R100	Obsidian Vault/Topics/computing-research-methods/Concepts/Evidence and Literature Review.md	Obsidian Vault/Samuel/Samuel Study/Shared References/computing-research-methods/Concepts/Evidence and Literature Review.md
R100	Obsidian Vault/Topics/computing-research-methods/Concepts/Research Communication.md	Obsidian Vault/Samuel/Samuel Study/Shared References/computing-research-methods/Concepts/Research Communication.md
R100	Obsidian Vault/Topics/computing-research-methods/Concepts/Research Purpose and the 6Ps.md	Obsidian Vault/Samuel/Samuel Study/Shared References/computing-research-methods/Concepts/Research Purpose and the 6Ps.md
R100	Obsidian Vault/Topics/computing-research-methods/Concepts/Research Strategies and Methods.md	Obsidian Vault/Samuel/Samuel Study/Shared References/computing-research-methods/Concepts/Research Strategies and Methods.md
R100	Obsidian Vault/Topics/computing-research-methods/Concepts/_Concept Note Template.md	Obsidian Vault/Samuel/Samuel Study/Shared References/computing-research-methods/Concepts/_Concept Note Template.md
A	Obsidian Vault/Samuel/Samuel Study/Shared References/computing-research-methods/Exports/NotebookLM/.gitkeep
A	Obsidian Vault/Samuel/Samuel Study/Shared References/computing-research-methods/Exports/NotebookLM/00 Curated Source Guide.md
R045	Academic Source Library/computing-research-methods/source-manifest.csv	Obsidian Vault/Samuel/Samuel Study/Shared References/computing-research-methods/Exports/NotebookLM/source-manifest.csv
A	Obsidian Vault/Samuel/Samuel Study/Shared References/computing-research-methods/Sessions/.gitkeep
R100	Obsidian Vault/Topics/computing-research-methods/Sessions/_Session Note Template.md	Obsidian Vault/Samuel/Samuel Study/Shared References/computing-research-methods/Sessions/_Session Note Template.md
A	Obsidian Vault/Samuel/Samuel Study/Shared References/computing-research-methods/Sources/.gitkeep
R059	Obsidian Vault/Topics/computing-research-methods/Sources/SRC-0001 - Researching Information Systems and Computing.md	Obsidian Vault/Samuel/Samuel Study/Shared References/computing-research-methods/Sources/SRC-0001 - Researching Information Systems and Computing.md
R100	Obsidian Vault/Topics/computing-research-methods/Sources/_Source Note Template.md	Obsidian Vault/Samuel/Samuel Study/Shared References/computing-research-methods/Sources/_Source Note Template.md
R083	Obsidian Vault/Topics/cpp-programming/00 Topic Map.md	Obsidian Vault/Samuel/Samuel Study/Shared References/cpp-programming/00 Topic Map.md
R100	Obsidian Vault/Topics/cpp-programming/01 Research Questions.md	Obsidian Vault/Samuel/Samuel Study/Shared References/cpp-programming/01 Research Questions.md
R100	Obsidian Vault/Topics/cpp-programming/02 Concept Map.md	Obsidian Vault/Samuel/Samuel Study/Shared References/cpp-programming/02 Concept Map.md
R072	Obsidian Vault/Topics/cpp-programming/03 Evidence Ledger.csv	Obsidian Vault/Samuel/Samuel Study/Shared References/cpp-programming/03 Evidence Ledger.csv
R100	Obsidian Vault/Topics/cpp-programming/04 Contradictions.md	Obsidian Vault/Samuel/Samuel Study/Shared References/cpp-programming/04 Contradictions.md
R100	Obsidian Vault/Topics/cpp-programming/05 Misconceptions.md	Obsidian Vault/Samuel/Samuel Study/Shared References/cpp-programming/05 Misconceptions.md
R100	Obsidian Vault/Topics/cpp-programming/06 Recall Queue.md	Obsidian Vault/Samuel/Samuel Study/Shared References/cpp-programming/06 Recall Queue.md
A	Obsidian Vault/Samuel/Samuel Study/Shared References/cpp-programming/Concepts/.gitkeep
R100	Obsidian Vault/Topics/cpp-programming/Concepts/Classes Inheritance and Polymorphism.md	Obsidian Vault/Samuel/Samuel Study/Shared References/cpp-programming/Concepts/Classes Inheritance and Polymorphism.md
R100	Obsidian Vault/Topics/cpp-programming/Concepts/Control Flow and Files.md	Obsidian Vault/Samuel/Samuel Study/Shared References/cpp-programming/Concepts/Control Flow and Files.md
R100	Obsidian Vault/Topics/cpp-programming/Concepts/Exceptions Templates and STL.md	Obsidian Vault/Samuel/Samuel Study/Shared References/cpp-programming/Concepts/Exceptions Templates and STL.md
R100	Obsidian Vault/Topics/cpp-programming/Concepts/Functions Arrays and Vectors.md	Obsidian Vault/Samuel/Samuel Study/Shared References/cpp-programming/Concepts/Functions Arrays and Vectors.md
R100	Obsidian Vault/Topics/cpp-programming/Concepts/Linked Structures Recursion and Trees.md	Obsidian Vault/Samuel/Samuel Study/Shared References/cpp-programming/Concepts/Linked Structures Recursion and Trees.md
R100	Obsidian Vault/Topics/cpp-programming/Concepts/Pointers Ownership and Memory.md	Obsidian Vault/Samuel/Samuel Study/Shared References/cpp-programming/Concepts/Pointers Ownership and Memory.md
R100	Obsidian Vault/Topics/cpp-programming/Concepts/Program Structure Types and Expressions.md	Obsidian Vault/Samuel/Samuel Study/Shared References/cpp-programming/Concepts/Program Structure Types and Expressions.md
R100	Obsidian Vault/Topics/cpp-programming/Concepts/Searching Sorting and Complexity.md	Obsidian Vault/Samuel/Samuel Study/Shared References/cpp-programming/Concepts/Searching Sorting and Complexity.md
R100	Obsidian Vault/Topics/cpp-programming/Concepts/Strings Structured Data and File Records.md	Obsidian Vault/Samuel/Samuel Study/Shared References/cpp-programming/Concepts/Strings Structured Data and File Records.md
R100	Obsidian Vault/Topics/cpp-programming/Concepts/_Concept Note Template.md	Obsidian Vault/Samuel/Samuel Study/Shared References/cpp-programming/Concepts/_Concept Note Template.md
A	Obsidian Vault/Samuel/Samuel Study/Shared References/cpp-programming/Exports/NotebookLM/.gitkeep
A	Obsidian Vault/Samuel/Samuel Study/Shared References/cpp-programming/Exports/NotebookLM/00 Curated Source Guide.md
R054	Obsidian Vault/Topics/cpp-programming/Exports/NotebookLM/source-manifest.csv	Obsidian Vault/Samuel/Samuel Study/Shared References/cpp-programming/Exports/NotebookLM/source-manifest.csv
A	Obsidian Vault/Samuel/Samuel Study/Shared References/cpp-programming/Sessions/.gitkeep
R100	Obsidian Vault/Topics/cpp-programming/Sessions/_Session Note Template.md	Obsidian Vault/Samuel/Samuel Study/Shared References/cpp-programming/Sessions/_Session Note Template.md
A	Obsidian Vault/Samuel/Samuel Study/Shared References/cpp-programming/Sources/.gitkeep
R050	Obsidian Vault/Topics/cpp-programming/Sources/SRC-0001 - Starting Out with C++.md	Obsidian Vault/Samuel/Samuel Study/Shared References/cpp-programming/Sources/SRC-0001 - Starting Out with C++.md
R100	Obsidian Vault/Topics/cpp-programming/Sources/_Source Note Template.md	Obsidian Vault/Samuel/Samuel Study/Shared References/cpp-programming/Sources/_Source Note Template.md
R084	Obsidian Vault/Topics/networking-fundamentals/00 Topic Map.md	Obsidian Vault/Samuel/Samuel Study/Shared References/networking-fundamentals/00 Topic Map.md
R100	Obsidian Vault/Topics/networking-fundamentals/01 Research Questions.md	Obsidian Vault/Samuel/Samuel Study/Shared References/networking-fundamentals/01 Research Questions.md
R100	Obsidian Vault/Topics/networking-fundamentals/02 Concept Map.md	Obsidian Vault/Samuel/Samuel Study/Shared References/networking-fundamentals/02 Concept Map.md
R068	Obsidian Vault/Topics/networking-fundamentals/03 Evidence Ledger.csv	Obsidian Vault/Samuel/Samuel Study/Shared References/networking-fundamentals/03 Evidence Ledger.csv
R100	Obsidian Vault/Topics/networking-fundamentals/04 Contradictions.md	Obsidian Vault/Samuel/Samuel Study/Shared References/networking-fundamentals/04 Contradictions.md
R100	Obsidian Vault/Topics/networking-fundamentals/05 Misconceptions.md	Obsidian Vault/Samuel/Samuel Study/Shared References/networking-fundamentals/05 Misconceptions.md
R100	Obsidian Vault/Topics/networking-fundamentals/06 Recall Queue.md	Obsidian Vault/Samuel/Samuel Study/Shared References/networking-fundamentals/06 Recall Queue.md
A	Obsidian Vault/Samuel/Samuel Study/Shared References/networking-fundamentals/Concepts/.gitkeep
R100	Obsidian Vault/Topics/networking-fundamentals/Concepts/Ethernet and Network Media.md	Obsidian Vault/Samuel/Samuel Study/Shared References/networking-fundamentals/Concepts/Ethernet and Network Media.md
R100	Obsidian Vault/Topics/networking-fundamentals/Concepts/IPv4 Addressing and Subnetting.md	Obsidian Vault/Samuel/Samuel Study/Shared References/networking-fundamentals/Concepts/IPv4 Addressing and Subnetting.md
R100	Obsidian Vault/Topics/networking-fundamentals/Concepts/Layered Models and Encapsulation.md	Obsidian Vault/Samuel/Samuel Study/Shared References/networking-fundamentals/Concepts/Layered Models and Encapsulation.md
R100	Obsidian Vault/Topics/networking-fundamentals/Concepts/Network Configuration and Testing.md	Obsidian Vault/Samuel/Samuel Study/Shared References/networking-fundamentals/Concepts/Network Configuration and Testing.md
R100	Obsidian Vault/Topics/networking-fundamentals/Concepts/_Concept Note Template.md	Obsidian Vault/Samuel/Samuel Study/Shared References/networking-fundamentals/Concepts/_Concept Note Template.md
A	Obsidian Vault/Samuel/Samuel Study/Shared References/networking-fundamentals/Exports/NotebookLM/.gitkeep
A	Obsidian Vault/Samuel/Samuel Study/Shared References/networking-fundamentals/Exports/NotebookLM/00 Curated Source Guide.md
R052	Academic Source Library/networking-fundamentals/source-manifest.csv	Obsidian Vault/Samuel/Samuel Study/Shared References/networking-fundamentals/Exports/NotebookLM/source-manifest.csv
A	Obsidian Vault/Samuel/Samuel Study/Shared References/networking-fundamentals/Sessions/.gitkeep
R100	Obsidian Vault/Topics/networking-fundamentals/Sessions/_Session Note Template.md	Obsidian Vault/Samuel/Samuel Study/Shared References/networking-fundamentals/Sessions/_Session Note Template.md
A	Obsidian Vault/Samuel/Samuel Study/Shared References/networking-fundamentals/Sources/.gitkeep
R064	Obsidian Vault/Topics/networking-fundamentals/Sources/SRC-0001 - Network Fundamentals.md	Obsidian Vault/Samuel/Samuel Study/Shared References/networking-fundamentals/Sources/SRC-0001 - Network Fundamentals.md
R100	Obsidian Vault/Topics/networking-fundamentals/Sources/_Source Note Template.md	Obsidian Vault/Samuel/Samuel Study/Shared References/networking-fundamentals/Sources/_Source Note Template.md
R084	Obsidian Vault/Topics/systems-analysis-and-design/00 Topic Map.md	Obsidian Vault/Samuel/Samuel Study/Shared References/systems-analysis-and-design/00 Topic Map.md
R100	Obsidian Vault/Topics/systems-analysis-and-design/01 Research Questions.md	Obsidian Vault/Samuel/Samuel Study/Shared References/systems-analysis-and-design/01 Research Questions.md
R100	Obsidian Vault/Topics/systems-analysis-and-design/02 Concept Map.md	Obsidian Vault/Samuel/Samuel Study/Shared References/systems-analysis-and-design/02 Concept Map.md
R066	Obsidian Vault/Topics/systems-analysis-and-design/03 Evidence Ledger.csv	Obsidian Vault/Samuel/Samuel Study/Shared References/systems-analysis-and-design/03 Evidence Ledger.csv
R100	Obsidian Vault/Topics/systems-analysis-and-design/04 Contradictions.md	Obsidian Vault/Samuel/Samuel Study/Shared References/systems-analysis-and-design/04 Contradictions.md
R100	Obsidian Vault/Topics/systems-analysis-and-design/05 Misconceptions.md	Obsidian Vault/Samuel/Samuel Study/Shared References/systems-analysis-and-design/05 Misconceptions.md
R100	Obsidian Vault/Topics/systems-analysis-and-design/06 Recall Queue.md	Obsidian Vault/Samuel/Samuel Study/Shared References/systems-analysis-and-design/06 Recall Queue.md
A	Obsidian Vault/Samuel/Samuel Study/Shared References/systems-analysis-and-design/Concepts/.gitkeep
R100	Obsidian Vault/Topics/systems-analysis-and-design/Concepts/Data UI Interfaces Controls and Security.md	Obsidian Vault/Samuel/Samuel Study/Shared References/systems-analysis-and-design/Concepts/Data UI Interfaces Controls and Security.md
R100	Obsidian Vault/Topics/systems-analysis-and-design/Concepts/Deployment and Support.md	Obsidian Vault/Samuel/Samuel Study/Shared References/systems-analysis-and-design/Concepts/Deployment and Support.md
R100	Obsidian Vault/Topics/systems-analysis-and-design/Concepts/Development Lifecycles and Project Management.md	Obsidian Vault/Samuel/Samuel Study/Shared References/systems-analysis-and-design/Concepts/Development Lifecycles and Project Management.md
R100	Obsidian Vault/Topics/systems-analysis-and-design/Concepts/Requirements Investigation and Modeling.md	Obsidian Vault/Samuel/Samuel Study/Shared References/systems-analysis-and-design/Concepts/Requirements Investigation and Modeling.md
R100	Obsidian Vault/Topics/systems-analysis-and-design/Concepts/Systems Design and Architecture.md	Obsidian Vault/Samuel/Samuel Study/Shared References/systems-analysis-and-design/Concepts/Systems Design and Architecture.md
R100	Obsidian Vault/Topics/systems-analysis-and-design/Concepts/Traditional and Object-Oriented Analysis.md	Obsidian Vault/Samuel/Samuel Study/Shared References/systems-analysis-and-design/Concepts/Traditional and Object-Oriented Analysis.md
R100	Obsidian Vault/Topics/systems-analysis-and-design/Concepts/_Concept Note Template.md	Obsidian Vault/Samuel/Samuel Study/Shared References/systems-analysis-and-design/Concepts/_Concept Note Template.md
A	Obsidian Vault/Samuel/Samuel Study/Shared References/systems-analysis-and-design/Exports/NotebookLM/.gitkeep
A	Obsidian Vault/Samuel/Samuel Study/Shared References/systems-analysis-and-design/Exports/NotebookLM/00 Curated Source Guide.md
R050	Obsidian Vault/Topics/systems-analysis-and-design/Exports/NotebookLM/source-manifest.csv	Obsidian Vault/Samuel/Samuel Study/Shared References/systems-analysis-and-design/Exports/NotebookLM/source-manifest.csv
A	Obsidian Vault/Samuel/Samuel Study/Shared References/systems-analysis-and-design/Sessions/.gitkeep
R100	Obsidian Vault/Topics/systems-analysis-and-design/Sessions/_Session Note Template.md	Obsidian Vault/Samuel/Samuel Study/Shared References/systems-analysis-and-design/Sessions/_Session Note Template.md
A	Obsidian Vault/Samuel/Samuel Study/Shared References/systems-analysis-and-design/Sources/.gitkeep
R057	Obsidian Vault/Topics/systems-analysis-and-design/Sources/SRC-0001 - Systems Analysis and Design.md	Obsidian Vault/Samuel/Samuel Study/Shared References/systems-analysis-and-design/Sources/SRC-0001 - Systems Analysis and Design.md
R100	Obsidian Vault/Topics/systems-analysis-and-design/Sources/_Source Note Template.md	Obsidian Vault/Samuel/Samuel Study/Shared References/systems-analysis-and-design/Sources/_Source Note Template.md
A	Obsidian Vault/Samuel/Samuel Work/00 Work Home.md
D	Obsidian Vault/Topics/computing-research-methods/Exports/NotebookLM/00 Curated Source Guide.md
D	Obsidian Vault/Topics/cpp-programming/Exports/NotebookLM/00 Curated Source Guide.md
D	Obsidian Vault/Topics/cross-topic-index/Exports/NotebookLM/00 Curated Source Guide.md
D	Obsidian Vault/Topics/networking-fundamentals/Exports/NotebookLM/00 Curated Source Guide.md
D	Obsidian Vault/Topics/systems-analysis-and-design/Exports/NotebookLM/00 Curated Source Guide.md
M	README.md
A	README_AI.md
A	Samuel/README.md
A	Samuel/Samuel Study/00 Inbox/.gitkeep
A	Samuel/Samuel Study/Cross-topic Index/00 Curated Source Guide.md
A	Samuel/Samuel Study/Cross-topic Index/01 NotebookLM Processing Prompt.md
A	Samuel/Samuel Study/Cross-topic Index/source-manifest.csv
A	Samuel/Samuel Study/ICT111/00 Curated Source Guide.md
A	Samuel/Samuel Study/ICT111/00 Inbox/.gitkeep
A	Samuel/Samuel Study/ICT111/01 NotebookLM Processing Prompt.md
A	Samuel/Samuel Study/ICT111/99 Review/.gitkeep
A	Samuel/Samuel Study/ICT111/Assignments/Assignment 1/.gitkeep
A	Samuel/Samuel Study/ICT111/Assignments/Assignment 2/.gitkeep
A	Samuel/Samuel Study/ICT111/Labs/.gitkeep
A	Samuel/Samuel Study/ICT111/README.md
A	Samuel/Samuel Study/ICT111/Readings/.gitkeep
A	Samuel/Samuel Study/ICT111/Slides/00 Unsorted/.gitkeep
A	Samuel/Samuel Study/ICT111/Slides/Lesson1/.gitkeep
A	Samuel/Samuel Study/ICT111/Slides/Lesson2/.gitkeep
A	Samuel/Samuel Study/ICT111/Slides/Lesson3/.gitkeep
A	Samuel/Samuel Study/ICT111/Slides/Lesson4/.gitkeep
A	Samuel/Samuel Study/ICT111/Slides/Lesson5/.gitkeep
A	Samuel/Samuel Study/ICT111/Slides/Lesson6/.gitkeep
A	Samuel/Samuel Study/ICT111/Slides/Lesson7/.gitkeep
A	Samuel/Samuel Study/ICT111/source-manifest.csv
A	Samuel/Samuel Study/ICT201/00 Curated Source Guide.md
A	Samuel/Samuel Study/ICT201/00 Inbox/.gitkeep
A	Samuel/Samuel Study/ICT201/01 NotebookLM Processing Prompt.md
A	Samuel/Samuel Study/ICT201/99 Review/.gitkeep
A	Samuel/Samuel Study/ICT201/Assignments/Assignment 1/.gitkeep
A	Samuel/Samuel Study/ICT201/Assignments/Assignment 2/.gitkeep
A	Samuel/Samuel Study/ICT201/Labs/.gitkeep
A	Samuel/Samuel Study/ICT201/README.md
A	Samuel/Samuel Study/ICT201/Readings/.gitkeep
A	Samuel/Samuel Study/ICT201/Slides/00 Unsorted/.gitkeep
A	Samuel/Samuel Study/ICT201/Slides/Lesson1/.gitkeep
A	Samuel/Samuel Study/ICT201/Slides/Lesson2/.gitkeep
A	Samuel/Samuel Study/ICT201/Slides/Lesson3/.gitkeep
A	Samuel/Samuel Study/ICT201/Slides/Lesson4/.gitkeep
A	Samuel/Samuel Study/ICT201/Slides/Lesson5/.gitkeep
A	Samuel/Samuel Study/ICT201/Slides/Lesson6/.gitkeep
A	Samuel/Samuel Study/ICT201/Slides/Lesson7/.gitkeep
A	Samuel/Samuel Study/ICT201/source-manifest.csv
A	Samuel/Samuel Study/Shared References/computing-research-methods/00 Curated Source Guide.md
R100	Academic Source Library/computing-research-methods/01 NotebookLM Processing Prompt.md	Samuel/Samuel Study/Shared References/computing-research-methods/01 NotebookLM Processing Prompt.md
R100	Academic Source Library/computing-research-methods/Sources/Accepted/SRC-0001 - Researching Information Systems and Computing.pdf	Samuel/Samuel Study/Shared References/computing-research-methods/Sources/Accepted/SRC-0001 - Researching Information Systems and Computing.pdf
R045	Obsidian Vault/Topics/computing-research-methods/Exports/NotebookLM/source-manifest.csv	Samuel/Samuel Study/Shared References/computing-research-methods/source-manifest.csv
A	Samuel/Samuel Study/Shared References/cpp-programming/00 Curated Source Guide.md
R100	Academic Source Library/cpp-programming/01 NotebookLM Processing Prompt.md	Samuel/Samuel Study/Shared References/cpp-programming/01 NotebookLM Processing Prompt.md
R100	Academic Source Library/cpp-programming/Sources/Accepted/SRC-0001 - Starting Out with C++ - Ninth Global Edition.pdf	Samuel/Samuel Study/Shared References/cpp-programming/Sources/Accepted/SRC-0001 - Starting Out with C++ - Ninth Global Edition.pdf
R054	Academic Source Library/cpp-programming/source-manifest.csv	Samuel/Samuel Study/Shared References/cpp-programming/source-manifest.csv
A	Samuel/Samuel Study/Shared References/networking-fundamentals/00 Curated Source Guide.md
R100	Academic Source Library/networking-fundamentals/01 NotebookLM Processing Prompt.md	Samuel/Samuel Study/Shared References/networking-fundamentals/01 NotebookLM Processing Prompt.md
R100	Academic Source Library/networking-fundamentals/Sources/Accepted/SRC-0001 - Network Fundamentals - CCNA Exploration Companion Guide.pdf	Samuel/Samuel Study/Shared References/networking-fundamentals/Sources/Accepted/SRC-0001 - Network Fundamentals - CCNA Exploration Companion Guide.pdf
R052	Obsidian Vault/Topics/networking-fundamentals/Exports/NotebookLM/source-manifest.csv	Samuel/Samuel Study/Shared References/networking-fundamentals/source-manifest.csv
A	Samuel/Samuel Study/Shared References/systems-analysis-and-design/00 Curated Source Guide.md
R100	Academic Source Library/systems-analysis-and-design/01 NotebookLM Processing Prompt.md	Samuel/Samuel Study/Shared References/systems-analysis-and-design/01 NotebookLM Processing Prompt.md
R100	Academic Source Library/systems-analysis-and-design/Sources/Accepted/SRC-0001 - Systems Analysis and Design in a Changing World.pdf	Samuel/Samuel Study/Shared References/systems-analysis-and-design/Sources/Accepted/SRC-0001 - Systems Analysis and Design in a Changing World.pdf
R050	Academic Source Library/systems-analysis-and-design/source-manifest.csv	Samuel/Samuel Study/Shared References/systems-analysis-and-design/source-manifest.csv
A	Samuel/Samuel Work/.gitkeep
A	Samuel/Samuel Work/README.md
A	config/notebook-registry.csv
A	config/retained-sources.json
M	docs/INTEGRATION_STATUS.md
M	docs/NOTEBOOKLM_WORKFLOW.md
M	docs/SYNCTHING_SETUP.md
A	docs/WINDOWS_SETUP.md
A	ecosystem.json
A	scripts/bootstrap_workspace.py
A	scripts/check_generated.py
A	scripts/install_skill.py
M	scripts/rebuild_notebooklm_manifests.py
M	scripts/validate_study_structure.py
A	scripts/workspace.py
A	skills/research-study/LICENSE
A	skills/research-study/SKILL.md
A	skills/research-study/THIRD_PARTY_NOTICES.md
A	skills/research-study/agents/openai.yaml
A	skills/research-study/references/chatgpt-orchestration.md
A	skills/research-study/references/integration-requirements.md
A	skills/research-study/references/notebooklm-workflow.md
A	skills/research-study/references/obsidian-memory-model.md
A	skills/research-study/references/organization.md
A	skills/research-study/references/paper-types-and-venues.md
A	skills/research-study/references/research-integrity.md
A	skills/research-study/references/research-pipeline.md
A	skills/research-study/references/source-ledger-schema.md
A	skills/research-study/references/sync-architecture.md
A	skills/research-study/scripts/build_notebooklm_manifest.py
A	skills/research-study/scripts/init_topic.py
A	skills/research-study/scripts/organize_files.py
A	skills/research-study/scripts/validate_topic.py
A	skills/research-study/workflows/document-ingestion/GUIDE.md
A	skills/research-study/workflows/document-ingestion/references/baidu-unlimited-ocr.md
A	skills/research-study/workflows/document-ingestion/scripts/unlimited_ocr_client.py
A	skills/research-study/workflows/experiment-design/GUIDE.md
A	skills/research-study/workflows/experiment-design/templates/experiment-plan.md
A	skills/research-study/workflows/idea-generation/GUIDE.md
A	skills/research-study/workflows/idea-generation/templates/idea-proposal.md
A	skills/research-study/workflows/literature-review/GUIDE.md
A	skills/research-study/workflows/literature-review/templates/evidence-matrix.md
A	skills/research-study/workflows/paper-reading/GUIDE.md
A	skills/research-study/workflows/paper-writing/GUIDE.md
A	skills/research-study/workflows/professor-fit-analysis/GUIDE.md
A	skills/research-study/workflows/proof-writing/GUIDE.md
A	skills/research-study/workflows/research-paper-review/GUIDE.md
A	skills/research-study/workflows/research-paper-review/references/consistency-checks.md
A	skills/research-study/workflows/research-paper-review/references/constructive-feedback.md
A	skills/research-study/workflows/research-paper-review/references/scoring-and-decisions.md
A	skills/research-study/workflows/research-paper-review/templates/meta-review-form.md
A	skills/research-study/workflows/research-paper-review/templates/review-form.md
A	skills/research-study/workflows/revision-and-rebuttal/GUIDE.md
A	skills/research-study/workflows/revision-and-rebuttal/templates/revision-matrix.md
A	tests/test_file_intake.py
A	tests/test_review_regressions.py
```
