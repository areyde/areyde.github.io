---
title: "CommitChronicle"
description: "A large-scale, diverse multilingual dataset for commit message generation and completion."
collection: datasets
permalink: /datasets/commit-chronicle
redirect_from:
  - /dataset/commit-chronicle
  - /dataset/commit-chronicle/
tag: 'A large-scale, diverse multilingual dataset for commit message generation and completion.'
pdf: 'https://arxiv.org/abs/2308.07655'
paperurl: 'https://doi.org/10.1109/ASE56229.2023.00078'
data: 'https://huggingface.co/datasets/JetBrains-Research/commit-chronicle'
abstract: "<b>CommitChronicle</b> is a large-scale, diverse multilingual dataset for commit message generation and completion. We used GitHub Search tool and official GitHub API to select relevant repositories with permissive licenses (Apache, BSD 3-clause, MIT). On February 9th, 2023, we collected all commits made since 2017 from these repositories via PyDriller. Next, we extensively cleaned the data, including filtering outliers, dropping commits from bot authors, and dropping duplicates. Note: to avoid disclosing personal information, we replaced the commit authors' names and emails with unique identifiers."
---