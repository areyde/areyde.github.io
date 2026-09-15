---
title: "PythonChangeMiner"
description: "A tool for creating fine-grained program dependence graphs (fgPDG) for Python code, creating change graphs from them, and mining these graphs for change patterns."
collection: tools
permalink: /tools/python-change-miner
redirect_from:
  - /tool/python-change-miner
  - /tool/python-change-miner/
pdf: 'https://arxiv.org/abs/2105.10157'
tool: 'https://github.com/JetBrains-Research/python-change-miner'
tag: 'A tool for creating fine-grained program dependence graphs (fgPDG) for Python code, creating change graphs from them, and mining these graphs for change patterns.'
abstract: '<p><b>PythonChangeMiner</b> is a tool for creating fine-grained program dependence graphs (fgPDG) for Python code, creating change graphs from them, and mining these graphs for change patterns. A program dependence graph is a way of representing the code by showing its data dependencies and control dependencies. A change graph is a program dependence graph for the fragment of code changes (using the versions of code before and after the target change). Similar code changes will have similar change graphs, which means that any versioned code can be mined for patterns in its changes. This tool does exactly that for Python code: it can build program dependence graphs, build change graphs for changed files, mine such change graphs from Git repositories by traversing their VCS history, and discover patterns in these change graphs. This functionality can be used for empirical research of coding practices, as well as for mining the candidates for potential IDE inspections.</p>'
---