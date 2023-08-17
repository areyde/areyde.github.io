---
title: "Just-in-time Code Duplicates Extraction"
authors: '<i>Eman Abdullah AlOmar, Anton Ivanov, Zarina Kurbatova, Yaroslav Golubev, Mohamed Wiem Mkaouer, Ali Ouni, Timofey Bryksin, Le Nguyen, Amit Kini, and Aditya Thakur</i>'
status: "published"
collection: publications
permalink: /publications/2023-06-01-duplicate-extraction
date: 2023-06-01
venue: "<b>Information and Software Technology</b>"
paperurl: 'https://doi.org/10.1016/j.infsof.2023.107169'
pdf: 'https://arxiv.org/pdf/2302.03416.pdf'
level: 'Q1'
counter_id: 'J3'
data: 'https://zenodo.org/record/7428835'
tool: 'https://github.com/JetBrains-Research/anti-copy-paster'
abstract: "<p><b>Abstract</b>. <i>Context</i>: Refactoring is a critical task in software maintenance, and is usually performed to enforce better design and coding practices, while coping with design defects. The Extract Method refactoring is widely used for merging duplicate code fragments into a single new method. Several studies attempted to recommend Extract Method refactoring opportunities using different techniques, including program slicing, program dependency graph analysis, change history analysis, structural similarity, and feature extraction. However, irrespective of the method, most of the existing approaches interfere with the developer's workflow: they require the developer to stop coding and analyze the suggested opportunities, and also consider all refactoring suggestions in the entire project without focusing on the development context.</p><p><i>Objective</i>: To increase the adoption of the Extract Method refactoring, in this paper, we aim to investigate the effectiveness of machine learning and deep learning algorithms for its recommendation while maintaining the workflow of the developer.</p><p><i>Method</i>: The proposed approach relies on mining prior applied Extract Method refactorings and extracting their features to train a deep learning classifier that detects them in the user's code. We implemented our approach as a plugin for IntelliJ IDEA called AntiCopyPaster. To develop our approach, we trained and evaluated various popular models on a dataset of 18,942 code fragments from 13 Open Source Apache projects.</p><p><i>Results</i>: The results show that the best model is the Convolutional Neural Network (CNN), which recommends appropriate Extract Method refactorings with an F-measure of 0.82. We also conducted a qualitative study with 72 developers to evaluate the usefulness of the developed plugin.</p><p><i>Conclusion</i>: The results show that developers tend to appreciate the idea of the approach and are satisfied with various aspects of the plugin's operation.</p>"
j1: 'true'
j1venue: "ESEM'23"
j1level: 'A'
---