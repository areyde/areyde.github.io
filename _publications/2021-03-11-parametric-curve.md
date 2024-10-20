---
title: "Multi-Threshold Token-Based Code Clone Detection"
authors: '<i>Yaroslav Golubev, Viktor Poletansky, Nikita Povarov, and Timofey Bryksin</i>'
collection: publications
permalink: /publications/2021-03-11-parametric-curve
date: 2021-03-11
venue: "the proceedings of <b>SANER'21</b>"
paperurl: 'https://doi.org/10.1109/SANER50967.2021.00053'
pdf: 'https://arxiv.org/abs/2002.05204'
data: 'https://zenodo.org/record/4279694'
video: 'https://www.youtube.com/watch?v=wTGBprWqurw'
counter_id: 'C6'
level: 'A'
abstract: '<p><b>Abstract</b>. Clone detection plays an important role in software engineering. Finding clones within a single project introduces possible refactoring opportunities, and between different projects it could be used for detecting code reuse or possible licensing violations.</p><p>In this paper, we propose a modification to bag-of-tokens based clone detection that allows detecting more clone pairs of greater diversity without losing precision by implementing a multi-threshold search, i.e. conducting the search several times, aimed at different groups of clones. To combat the increase in operation time that this approach brings about, we propose an optimization that allows to significantly decrease the overlap in detected clones between the searches.</p><p>We evaluate the method for two different popular clone detection tools on two datasets of different sizes. The implementation of the technique allows to increase the number of detected clones by 40.5-56.6% for different datasets. BigCloneBench evaluation also shows that the recall of detecting Strongly Type-3 clones increases from 37.5% to 59.6%.</p>'
---