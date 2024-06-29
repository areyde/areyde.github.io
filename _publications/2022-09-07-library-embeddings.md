---
title: "So Much in So Little: Creating Lightweight Embeddings of Python Libraries"
authors: '<i>Yaroslav Golubev, Egor Bogomolov, Egor Bulychev, and Timofey Bryksin</i>'
status: "preprint"
collection: publications
permalink: /publications/2022-09-07-library-embeddings
date: 2022-09-07
venue: "<b>arXiv</b>"
pdf: 'https://arxiv.org/pdf/2209.03507.pdf'
data: 'https://github.com/JetBrains-Research/similar-python-dependencies'
counter_id: 'P3'
abstract: "<p><b>Abstract</b>. In software engineering, different approaches and machine learning models leverage different types of data: source code, textual information, historical data. An important part of any project is its dependencies. The list of dependencies is relatively small but carries a lot of semantics with it, which can be used to compare projects or make judgements about them.</p><p>In this paper, we focus on Python projects and their PyPi dependencies in the form of requirements.txt files. We compile a dataset of 7,132 Python projects and their dependencies, as well as use Git to pull their versions from previous years. Using this data, we build 32-dimensional embeddings of libraries by applying Singular Value Decomposition to the co-occurrence matrix of projects and libraries. We then cluster the embeddings and study their semantic relations.</p><p>To showcase the usefulness of such lightweight library embeddings, we introduce a prototype tool for suggesting relevant libraries to a given project. The tool computes project embeddings and uses dependencies of projects with similar embeddings to form suggestions. To compare different library recommenders, we have created a benchmark based on the evolution of dependency sets in open-source projects. Approaches based on the created embeddings significantly outperform the baseline of showing the most popular libraries in a given year. We have also conducted a user study that showed that the suggestions differ in quality for different project domains and that even relevant suggestions might be not particularly useful. Finally, to facilitate potentially more useful recommendations, we extended the recommender system with an option to suggest rarer libraries.</p>"
---