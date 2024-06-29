---
title: "A Large-Scale Comparison of Python Code in Jupyter Notebooks and Scripts"
authors: '<i>Konstantin Grotov, Sergey Titov, Vladimir Sotnikov, Yaroslav Golubev, and Timofey Bryksin</i>'
status: "published"
collection: publications
permalink: /publications/2022-05-18-jupyter-analysis
date: 2022-05-18
venue: "the proceedings of <b>MSR'22</b>"
paperurl: 'https://doi.org/10.1145/3524842.3528447'
pdf: 'https://arxiv.org/pdf/2203.16718.pdf'
tool: 'https://github.com/JetBrains-Research/Matroskin'
data: 'https://zenodo.org/record/6383115'
counter_id: 'C16'
level: 'A'
award: '🏆 ACM SIGSOFT Distinguished Paper Award 🏆'
video: 'https://www.youtube.com/watch?v=bYXUfXtR2-Y'
abstract: "<p><b>Abstract</b>. In recent years, Jupyter notebooks have grown in popularity in several domains of software engineering, such as data science, machine learning, and computer science education. Their popularity has to do with their rich features for presenting and visualizing data, however, recent studies show that notebooks also share a lot of drawbacks: high number of code clones, low reproducibility, etc.</p><p>In this work, we carry out a comparison between Python code written in Jupyter Notebooks and in traditional Python scripts. We compare the code from two perspectives: structural and stylistic. In the first part of the analysis, we report the difference in the number of lines, the usage of functions, as well as various complexity metrics. In the second part, we show the difference in the number of stylistic issues and provide an extensive overview of the 15 most frequent stylistic issues in the studied mediums. Overall, we demonstrate that notebooks are characterized by the lower code complexity, however, their code could be perceived as more entangled than in the scripts. As for the style, notebooks tend to have 1.4 times more stylistic issues, but at the same time, some of them are caused by specific coding practices in notebooks and should be considered as false positives. With this research, we want to pave the way to studying specific problems of notebooks that should be addressed by the development of notebook-specific tools, and provide various insights that can be useful in this regard.</p>"
---