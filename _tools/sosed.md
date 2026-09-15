---
title: "Sosed"
description: "A tool for discovering similar software projects."
collection: tools
permalink: /tools/sosed
redirect_from:
  - /tool/sosed
  - /tool/sosed/
paperurl: 'https://doi.org/10.1145/3324884.3415291'
pdf: 'https://arxiv.org/abs/2007.02599'
tool: 'https://github.com/JetBrains-Research/sosed/'
video: 'https://www.youtube.com/watch?v=LYLkztCGRt8'
tag: 'A tool for discovering similar software projects. I developed a tokenizer for it, tested it a lot, and helped write the paper.'
abstract: '<p><b>Sosed</b> is a tool for discovering similar software projects. We use fastText to compute the embeddings of subtokens into a dense space for 120,000 GitHub repositories in 200 languages. Then, we cluster embeddings to identify groups of semantically similar sub-tokens that reflect topics in source code. We use a dataset of 9 million GitHub projects as a reference search base. To identify similar projects, we compare the distributions of clusters among their sub-tokens. The tool receives an arbitrary project as input, extracts sub-tokens in 16 most popular programming languages, computes cluster distribution, and finds projects with the closest distribution in the search base. We labeled subtoken clusters with short descriptions to enable Sosed to produce interpretable output.</p>'
---