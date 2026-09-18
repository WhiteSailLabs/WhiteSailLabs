# Local Asset Navigator

> Status: building on [llm-obsidian-agent](https://github.com/WhiteSailLabs/llm-obsidian-agent)

[简体中文](local-asset-navigator.zh-CN.md)

This project started with my own files.

After several projects, my laptop contains specifications, screenshots, PDFs, notes, images, and many versions of the same file. I often remember saving something but not where it is. Finding a file also does not prove that it is the version I actually used.

I am building a search tool that runs locally.

## Testing on my own workspace

The first dataset will contain files from my public projects and notes that I explicitly select. I will keep realistic problems: similar filenames, misleading `final` copies, duplicate images, stale exports, and image-only material.

The first version will scan one test folder, not the whole drive.

For a request such as “find the architecture diagram used in the last resume project and its explanation,” the tool should return the paths, explain the relationship, show competing versions, and mark uncertain links.

If two files both claim to be final, the tool should not choose silently. It should show the difference and save the user's decision for the next search.

## Local by default

Files, indexes, search history, and relationship data stay on the computer. If I later use an external model, the tool will send only the minimum content needed for that task and show what leaves the device.

## Evaluation

I will prepare 20 real retrieval tasks and complete them manually first. I will compare total task time, complete bundle retrieval, wrong-version errors, provenance coverage, permission handling, and whether corrections improve later searches.

## Progress

- [x] Existing local knowledge workspace
- [x] Basic file and relationship model
- [ ] Prepare the test folder
- [ ] Index images and PDFs
- [ ] Add version-conflict warnings
- [ ] Publish results for 20 tasks

It is not finished. The next useful step is a working version that can search my own project files, not another design document.
