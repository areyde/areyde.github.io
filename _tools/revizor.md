---
title: "Revizor"
description: "A plugin for PyCharm that takes the recurrent change patterns and highlights potential places for their application in the developer’s code editor."
collection: tools
permalink: /tools/revizor
redirect_from:
  - /tool/revizor
tool: 'https://github.com/JetBrains-Research/revizor'
video: 'https://www.youtube.com/watch?v=5eLs14nco7E'
pdf: 'https://arxiv.org/abs/2108.11199'
paperurl: 'https://doi.org/10.1109/ASE51524.2021.9678635'
tag: 'A plugin for PyCharm that takes the recurrent change patterns and highlights potential places for their application in the developer’s code editor. This tool was a continuation of another project of mine, but here I only helped write the paper.'
abstract: '<p><b>Revizor</b> is a plugin for PyCharm that takes the recurrent change patterns and highlights potential places for their application in the developer’s code editor. We use graph-based code change representations gathered from 120 GitHub repositories by Python Change Miner. Behind the scenes, the plugin runs an inspection which builds isomorphic mappings between fine-grained Program Dependence Graphs of the mined patterns and a similar graph of your code and then suggests a relevant quick-fix to apply for the highlighted code fragment.</p>'
---