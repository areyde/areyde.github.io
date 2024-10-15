---
title: "AntiCopyPaster: Extracting Code Duplicates As Soon As They Are Introduced in the IDE"
authors: '<i>Eman Abdullah AlOmar, Anton Ivanov, Zarina Kurbatova, Yaroslav Golubev, Mohamed Wiem Mkaouer, Ali Ouni, Timofey Bryksin, Le Nguyen, Amit Kini, and Aditya Thakur</i>'
status: "published"
collection: publications
permalink: /publications/2022-10-10-anti-copy-paster
date: 2022-10-10
venue: "the proceedings of <b>ASE'22</b>"
pdf: 'https://arxiv.org/abs/2112.15230'
paperurl: 'https://doi.org/10.1145/3551349.3559537'
level: 'A*'
tool: 'https://github.com/JetBrains-Research/anti-copy-paster'
counter_id: 'C18'
abstract: "<p><b>Abstract</b>. We have developed a plugin for IntelliJ IDEA called AntiCopyPaster that tracks the pasting of code inside the IDE and suggests appropriate Extract Method refactorings to combat the propagation of duplicates. To implement the plugin, we gathered a dataset of code fragments that should and should not be extracted, compiled a list of metrics of code that can influence the decision, and trained several popular classifying machine learning models, of which a gradient boosting classifier showed the best results. When a developer pastes a code fragment, the plugin searches for duplicates in the currently opened file. If there are any, it waits for a short period of time to allow the developer to edit the code. If the code duplicates are still present after a delay, AntiCopyPaster calculates the metrics for the fragment and inferences the decision: if the fragment should be extracted, the plugin suggests to refactor it. This can help the developers to keep their code clean and save them future maintenance time by providing the possibility to refactor code timely and without losing the context.</p><p>You can find the plugin and its source code on GitHub at <a href='https://github.com/JetBrains-Research/anti-copy-paster'>https://github.com/JetBrains-Research/anti-copy-paster</a>.</p>"
---