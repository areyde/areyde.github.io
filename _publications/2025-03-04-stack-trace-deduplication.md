---
title: "Stack Trace Deduplication: Faster, More Accurately, and in More Realistic Scenarios"
authors: '<i>Egor Shibaev, Denis Sushentsev, Yaroslav Golubev, and Aleksandr Khvorov</i>'
status: "accepted"
collection: publications
permalink: /publications/2025-03-04-stack-trace-deduplication
date: 2025-03-04
venue: "<b>SANER'25</b>"
level: "A"
pdf: 'https://arxiv.org/abs/2412.14802'
data: 'https://zenodo.org/records/14364858'
tool: 'https://github.com/JetBrains-Research/stack-trace-deduplication'
counter_id: 'C30'
abstract: "<p><b>Abstract</b>. In large-scale software systems, there are often no fully-fledged bug reports with human-written descriptions when an error occurs. In this case, developers rely on stack traces, i.e., series of function calls that led to the error. Since there can be tens and hundreds of thousands of them describing the same issue from different users, automatic deduplication into categories is necessary to allow for processing. Recent works have proposed powerful deep learning-based approaches for this, but they are evaluated and compared in isolation from real-life workflows, and it is not clear whether they will actually work well at scale.</p><p>To overcome this gap, this work presents three main contributions: a novel model, an industry-based dataset, and a multi-faceted evaluation. Our model consists of two parts - (1) an embedding model with byte-pair encoding and approximate nearest neighbor search to quickly find the most relevant stack traces to the incoming one, and (2) a reranker that re-ranks the most fitting stack traces, taking into account the repeated frames between them. To complement the existing datasets collected from open-source projects, we share with the community SlowOps - a dataset of stack traces from IntelliJ-based products developed by JetBrains, which has an order of magnitude more stack traces per category. Finally, we carry out an evaluation that strives to be realistic: measuring not only the accuracy of categorization, but also the operation time and the ability to create new categories. The evaluation shows that our model strikes a good balance - it outperforms other models on both open-source datasets and SlowOps, while also being faster on time than most. We release all of our code and data, and hope that our work can pave the way to further practice-oriented research in the area.</p>"
---