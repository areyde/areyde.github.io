---
title: "Predicting Tags for Programming Tasks by Combining Textual And Source Code Data"
authors: '<i>Artyom Lobanov, Egor Bogomolov, Yaroslav Golubev, Mikhail Mirzayanov, and Timofey Bryksin</i>'
status: "preprint"
collection: publications
permalink: /publications/2023-01-11-tag-prediction
date: 2023-01-11
venue: "<b>arXiv</b>"
pdf: 'https://arxiv.org/pdf/2301.04597.pdf'
data: 'https://github.com/JetBrains-Research/tag-prediction'
counter_id: 'P4'
abstract: "<p><b>Abstract</b>. Competitive programming remains a very popular activity that combines both software engineering and education. In order to prepare and to practice, contestants use extensive archives of problems from past contents available on various competitive programming platforms. One way to make this process more effective is to provide an automatic tag system for the tasks. Prior works do that by either using the tasks' problem statements or the code of their solutions.</p><p>In this study, we investigate which information source is more valuable for tag prediction. To answer that question, we compare existing approaches of both types on the same dataset and with the same set of tags. Then, we propose a novel approach, which is an ensemble of the Gated Graph Neural Network model for analyzing solutions and the Bidirectional Encoder Representations from Transformers model for processing statements. Our experiments show that our approach outperforms previously proposed models by 0.175 of the PR-AUC metric.</p>"
---