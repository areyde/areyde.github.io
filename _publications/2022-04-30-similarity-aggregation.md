---
title: "Aggregation of Stack Trace Similarities for Crash Report Deduplication"
authors: '<i>Nikolay Karasov, Aleksandr Khvorov, Roman Vasiliev, Yaroslav Golubev, and Timofey Bryksin</i>'
status: "preprint"
collection: publications
permalink: /publications/2022-04-30-similarity-aggregation
date: 2022-04-30
venue: "<b>arXiv</b>"
pdf: 'https://arxiv.org/abs/2205.00212'
data: 'https://github.com/nkarasovd/AggregationModel'
counter_id: 'P2'
abstract: "<p><b>Abstract</b>. The automatic collection of stack traces in bug tracking systems is an integral part of many software projects and their maintenance. However, such reports often contain a lot of duplicates, and the problem of de-duplicating them into groups arises. In this paper, we propose a new approach to solve the deduplication task and report on its use on the real-world data from JetBrains, a leading developer of IDEs and other software. Unlike most of the existing methods, which assign the incoming stack trace to a particular group in which a single most similar stack trace is located, we use the information about all the calculated similarities to the group, as well as the information about the timestamp of the stack traces. This approach to aggregating all available information shows significantly better results compared to existing solutions. The aggregation improved the results over the state-of-the-art solutions by 15 percentage points in the Recall Rate Top-1 metric on the existing NetBeans dataset and by 8 percentage points on the JetBrains data. Additionally, we evaluated a simpler k-Nearest Neighbors approach to aggregation and showed that it cannot reach the same levels of improvement. Finally, we studied what features from the aggregation contributed the most towards better quality to understand which of them to develop further. We publish the implementation of the suggested approach, and will release the newly collected industrial dataset upon acceptance to facilitate further research in the area.</p>"
---