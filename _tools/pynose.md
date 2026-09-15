---
title: "PyNose"
description: "A test smell detector for Python."
collection: tools
permalink: /tools/pynose
redirect_from:
  - /tool/pynose
  - /tool/pynose/
pdf: 'https://arxiv.org/abs/2108.04639'
tool: "https://github.com/JetBrains-Research/PyNose"
paperurl: 'https://doi.org/10.1109/ASE51524.2021.9678615'
video: "https://www.youtube.com/watch?v=Blk-BLYReyw"
tag: 'A test smell detector for Python. I helped select the smells to implement, came up with one new smell, conducted a study with the tool, wrote the paper, and later co-led an internship to improve it.'
abstract: "<p><b>PyNose</b> is a test smell detector for Python. PyNose is implemented as a plugin for PyCharm, a popular IDE for Python developed by JetBrains. The plugin supports two different modes of operation: Graphical User Interface (GUI) mode and Command Line Interface (CLI) mode. Internally, PyNose uses Program Structure Interface (PSI) from JetBrains' IntelliJ Platform (that PyCharm is built upon) to parse Python source code and build syntactic and semantic code models for analysis. When the project is opened and the interpreter is set up, the tool uses PSI and other related PyCharm API to gather all .py files in the project in the form of PSIFile objects. Next, the tool extracts all Python classes that are sub-classes of unittest.TestCase. With the help of PSI, PyNose can deal with importing unittest or unittest.TestCase under alias or test cases that are not direct sub-classes of unittest.TestCase. After collecting individual test suites, each detector class (corresponding to each test smell) invokes PsiElementVisitor to create a custom visitor for the necessary PsiElement, which allows PyNose to identify test smells.</p>"
---