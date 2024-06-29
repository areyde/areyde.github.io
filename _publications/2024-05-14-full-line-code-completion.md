---
title: "Full Line Code Completion: Bringing AI to Desktop"
authors: '<i>Anton Semenkin, Vitaliy Bibaev, Yaroslav Sokolov, Kirill Krylov, Alexey Kalina, Anna Khannanova, Danila Savenkov, Darya Rovdo, Igor Davidenko, Kirill Karnaukhov, Maxim Vakhrushev, Mikhail Kostyukov, Mikhail Podvitskii, Petr Surkov, Yaroslav Golubev, Nikita Povarov, and Timofey Bryksin</i>'
status: "preprint"
collection: publications
permalink: /publications/2024-05-14-full-line-code-completion
date: 2024-05-14
venue: "<b>arXiv</b>"
pdf: 'https://arxiv.org/pdf/2405.08704'
tool: 'https://plugins.jetbrains.com/plugin/14823-full-line-code-completion'
counter_id: 'P6'
abstract: "<p><b>Abstract</b>. In recent years, several industrial solutions for the problem of multi-token code completion have appeared, each making a great advance in the area but mostly focusing on cloud-based runtime and avoiding working on the end user's device.</p><p>In this work, we describe our approach for building a multi-token code completion feature for the JetBrains' IntelliJ Platform, which we call Full Line Code Completion. The feature suggests only syntactically correct code and works fully locally, i.e., data querying and the generation of suggestions happens on the end user's machine. We share important time and memory-consumption restrictions, as well as design principles that a code completion engine should satisfy. Working entirely on the end user's device, our code completion engine enriches user experience while being not only fast and compact but also secure. We share a number of useful techniques to meet the stated development constraints and also describe offline and online evaluation pipelines that allowed us to make better decisions.</p><p>Our online evaluation shows that the usage of the tool leads to 1.5 times more code in the IDE being produced by code completion. The described solution was initially started with the help of researchers and was bundled into two JetBrains' IDEs - PyCharm Pro and DataSpell - at the end of 2023, so we believe that this work is useful for bridging academia and industry, providing researchers with the knowledge of what happens when complex research-based solutions are integrated into real products.</p>"
---