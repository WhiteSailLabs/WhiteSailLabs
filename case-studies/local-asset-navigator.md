# Local Asset Navigator | Bringing scattered files back into the workflow

> Public reproduction · a public repository replaces private project directories

[中文](local-asset-navigator.zh-CN.md) · [Code](../experiments/local-asset-navigator/run.py) · [Raw results](../experiments/local-asset-navigator/results.json)

## The problem is not simply “too many files”

Project material naturally spreads across requirement notes, meeting records, screenshots, PDFs, and several files named `final-v2`. People remember that a solution existed but not its filename or folder.

Traditional search assumes the user already knows the right words. Real tasks sound different: “find the version we sent last time” or “bring back the architecture diagram and its explanation.” Those requests involve project relationships, file purpose, versions, and permissions rather than text alone.

Sensitive material also should not be uploaded merely to make search convenient. I therefore scoped the project as a local-first navigator. It reads only explicitly allowed directories, explains why a file was returned, and asks a person to resolve version conflicts.

## I mapped how files are used before indexing them

I separated the search process into four questions: what clue the user remembers, where they normally look, how they identify a version, and which related files they need next. That made paths, titles, types, links, and version relationships part of the design.

The public reproduction indexes only this profile repository. Its 20 tasks cover both profile languages, four case studies, and distracting words such as “project.” This intentionally creates a realistic conflict: the same topic appears in the profile summary, the case page, and the evaluation code.

Privacy is a product boundary: directories use an allowlist; indexes and query logs stay local; tool outputs are separated from user documents; and any future external model should receive only the minimum relevant excerpt.

## Run one: the search tool was fooled by its own code

The baseline reads file paths and text, then ranks literal term frequency with extra weight for path matches. It uses no vector database or model.

Only **6 of 20** tasks returned the right top result. The evaluation script could rank first because it contained the query itself. The profile README mentioned every project and often outranked the actual project page. The engine knew how often a term appeared but not whether a file was source code, a directory page, or the intended deliverable.

This showed that retrieval quality begins as an information-governance problem. A more sophisticated similarity model could simply retrieve the same noise more confidently.

## Run two: scope before sophistication

I excluded experiment code and generated results, then increased title weight. The final reproducible score rose to **9 of 20**. The limited gain exposed what remains missing: the system does not understand that “Chinese profile” means `README.zh-CN.md`, or that a project link in an index page should defer to the linked case page.

The next version will use layered signals for title, path, body, outgoing links, incoming references, and version state. Tool files will be down-ranked. User-confirmed version relationships will be stored as facts rather than guessed again.

## The product must make each result safe to open

A useful result needs the full path, matched excerpt, file type, modification time, related versions, and ranking reason. If two files claim to be final, the system should show their differences and usage history instead of choosing one.

User confirmation should persist locally: “A is the delivered version for project X; B is a draft.” Permissions are equally important. Unapproved folders must never enter the index, and deleting an index must remove its local records and query history.

## What the project leaves behind

The repository preserves the directory boundary, search code, 20 tasks, individual outcomes, and failure list. A 9/20 result is not impressive, but it is more useful than an unreproducible “smart file assistant” demo.

The work produced four FDE lessons:

1. Search quality starts with document boundaries, not a vector database.
2. Tool code, index pages, and deliverables need different roles in retrieval.
3. Version relationships require human confirmation.
4. Local-first includes permissions, logs, and deletion behavior, not just deployment.

The current reproduction does not cover PDF, images, OCR, duplicate files, or real version conflicts. The next milestone is stable text retrieval followed by multimodal indexing, measured with task time and wrong-version rate.
