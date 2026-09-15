---
title: "Sosed"
collection: tools
permalink: /tools/sosed
redirect_from:
  - /tool/sosed
paperurl: 'https://doi.org/10.1145/3324884.3415291'
pdf: 'https://arxiv.org/pdf/2007.02599.pdf'
tool: 'https://github.com/JetBrains-Research/sosed/'
video: 'https://www.youtube.com/watch?v=LYLkztCGRt8'
tag: 'A tool for discovering similar software projects.'
abstract: '<p><b>Sosed</b> is a tool for discovering similar software projects. We use fastText to compute the embeddings of subtokens into a dense space for 120,000 GitHub repositories in 200 languages. Then, we cluster embeddings to identify groups of semantically similar sub-tokens that reflect topics in source code. We use a dataset of 9 million GitHub projects as a reference search base. To identify similar projects, we compare the distributions of clusters among their sub-tokens. The tool receives an arbitrary project as input, extracts sub-tokens in 16 most popular programming languages, computes cluster distribution, and finds projects with the closest distribution in the search base. We labeled subtoken clusters with short descriptions to enable Sosed to produce interpretable output. Sosed is available at <a href="https://github.com/JetBrains-Research/sosed/">https://github.com/JetBrains-Research/sosed/</a>. The tool demo is available at <a href="https://www.youtube.com/watch?v=LYLkztCGRt8">https://www.youtube.com/watch?v=LYLkztCGRt8</a>. The multi-language extractor of sub-tokens is available separately at <a href="https://github.com/JetBrains-Research/buckwheat/">https://github.com/JetBrains-Research/buckwheat/</a>.</p>'
---