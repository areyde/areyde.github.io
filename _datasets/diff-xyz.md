---
title: "Diff-XYZ"
description: "A compact benchmark for code-diff understanding with three supervised tasks: apply, anti-apply, and diff generation."
collection: datasets
permalink: /datasets/diff-xyz
redirect_from:
  - /dataset/diff-xyz
  - /dataset/diff-xyz/
tag: 'A compact benchmark for code-diff understanding with three supervised tasks: apply, anti-apply, and diff generation.'
pdf: 'https://arxiv.org/abs/2510.12487'
data: 'https://huggingface.co/datasets/JetBrains-Research/diff-xyz'
paperurl: 'https://openreview.net/forum?id=1TgJd7uxOM'
abstract: "<p><b>Diff-XYZ</b> is a compact benchmark for code-diff understanding with three supervised tasks: apply, anti-apply, and diff generation. Instances in the benchmark are triples ⟨old code, new code, diff⟩ drawn from real commits in CommitPackFT, paired with automatic metrics and a clear evaluation protocol. Our findings reveal that different formats should be used depending on the use case and model size. For example, representing diffs in search-replace format performs best for larger models across most tasks, while structured udiff variants offer similar but slightly weaker performance. In contrast, smaller open models benefit little from any formatting choice. The Diff-XYZ benchmark is a reusable foundation for assessing and improving diff handling in LLMs that can aid future development of diff formats and models editing code.</p>"
---