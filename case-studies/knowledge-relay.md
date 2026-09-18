# Knowledge Relay

> Status: preparing the evaluation set

[简体中文](knowledge-relay.zh-CN.md)

I want to build a tool that helps new operators look up equipment problems.

A manual can explain where a control is and how to enter a parameter. It is less useful when something unusual happens. Experienced operators often know what to check first, but that knowledge is rarely written down in full.

This project will start with a public equipment manual and a question set that I create. It will not use a real factory or private operating data, so anyone can inspect and repeat the test.

## First version

The first version will do three things:

1. Find the relevant part of the manual.
2. Cite the file and page used in the answer.
3. Say that it does not know when the evidence is weak.

It will not control equipment or make safety decisions.

## How I will test it

I will prepare 40 questions. Some will have a direct answer in one section. Some will require several sections. Others will deliberately omit the equipment model, material, or current operation.

When key information is missing, the system should ask a useful follow-up instead of guessing.

I will record whether it finds the right section, whether the citation supports the answer, whether it asks for missing context, whether it stops when evidence is absent, and whether paraphrased questions produce stable results.

## Progress

- [x] Define the project boundary
- [x] Design question categories
- [ ] Select the public manual
- [ ] Write the first 40 questions
- [ ] Build the retrieval service
- [ ] Publish results and failure cases

I do not yet claim shorter training time or real factory use. My first goal is simpler: can the system ask the right question when the user is unclear, and can it stop when the manual does not support an answer?
