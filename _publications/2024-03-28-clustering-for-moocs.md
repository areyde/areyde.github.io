---
title: "Clustering MOOC Programming Solutions to Diversify Their Presentation to Students"
authors: '<i>Elizaveta Artser, Anastasiia Birillo, Yaroslav Golubev, Maria Tigina, Hieke Keuning, Nikolay Vyahhi, and Timofey Bryksin</i>'
status: "preprint"
collection: publications
permalink: /publications/2024-03-28-clustering-for-moocs
date: 2024-03-28
venue: "<b>arXiv</b>"
pdf: 'https://arxiv.org/pdf/2403.19398.pdf'
data: 'https://zenodo.org/records/8259494'
tool: 'https://github.com/hyperskill/code-submissions-clustering'
counter_id: 'P5'
abstract: "<p><b>Abstract</b>. In many MOOCs, whenever a student completes a programming task, they can see previous solutions of other students to find potentially different ways of solving the problem and learn new coding constructs. However, a lot of MOOCs simply show the most recent solutions, disregarding their diversity or quality.</p><p>To solve this novel problem, we adapted the existing plagiarism detection tool JPlag to Python submissions on Hyperskill, a popular MOOC platform. However, due to the tool's inner algorithm, it fully processed only 46 out of 867 studied tasks. Therefore, we developed our own tool called Rhubarb. This tool first standardizes solutions that are algorithmically the same, then calculates the structure-aware edit distance between them, and then applies clustering. Finally, it selects one example from each of the largest clusters, taking into account their code quality. Rhubarb was able to handle all 867 tasks successfully.</p><p>We compared approaches on a set of 59 tasks that both tools could process. Eight experts rated the selected solutions based on diversity, code quality, and usefulness. The default platform approach of selecting recent submissions received on average 3.12 out of 5, JPlag - 3.77, Rhubarb - 3.50. Since in the real MOOC, it is imperative to process everything, we created a system that uses JPlag on the 5.3% of tasks it fully processes and Rhubarb on the remaining 94.7%.</p>"
---