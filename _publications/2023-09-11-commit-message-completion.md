---
title: "From Commit Message Generation to History-Aware Commit Message Completion"
authors: '<i>Aleksandra Eliseeva, Yaroslav Sokolov, Egor Bogomolov, Yaroslav Golubev, Danny Dig, and Timofey Bryksin</i>'
status: "publsihed"
collection: publications
permalink: /publications/2023-09-11
date: 2023-09-11
venue: "the proceedings of <b>ASE'23</b>"
level: 'A*'
pdf: 'https://arxiv.org/abs/2308.07655'
paperurl: 'https://doi.org/10.1109/ASE56229.2023.00078'
counter_id: 'C25'
data: 'https://github.com/JetBrains-Research/commit_message_generation'
abstract: '<p><b>Abstract</b>. Commit messages are crucial to software development, allowing developers to track changes and collaborate effectively. Despite their utility, most commit messages lack important information since writing high-quality commit messages is tedious and time-consuming. The active research on commit message generation (CMG) has not yet led to wide adoption in practice. We argue that if we could shift the focus from commit message generation to commit message completion and use previous commit history as additional context, we could significantly improve the quality and the personal nature of the resulting commit messages.</p><p>In this paper, we propose and evaluate both of these novel ideas. Since the existing datasets lack historical data, we collect and share a novel dataset called CommitChronicle, containing 10.7M commits across 20 programming languages. We use this dataset to evaluate the completion setting and the usefulness of the historical context for state-of-the-art CMG models and GPT-3.5-turbo. Our results show that in some contexts, commit message completion shows better results than generation, and that while in general GPT-3.5-turbo performs worse, it shows potential for long and detailed messages. As for the history, the results show that historical information improves the performance of CMG models in the generation task, and the performance of GPT-3.5-turbo in both generation and completion.</p>'
---