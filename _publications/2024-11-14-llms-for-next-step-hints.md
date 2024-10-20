---
title: "One Step at a Time: Combining LLMs and Static Analysis to Generate Next-Step Hints for Programming Tasks"
authors: '<i>Anastasiia Birillo, Elizaveta Artser, Anna Potriasaeva, Ilya Vlasov, Katsiaryna Dzialets, Yaroslav Golubev, Igor Gerasimov, Hieke Keuning, and Timofey Bryksin</i>'
status: "accepted"
collection: publications
permalink: /publications/2024-11-14-llms-for-next-step-hints
date: 2024-11-14
venue: "<b>Koli Calling</b>"
pdf: 'https://arxiv.org/abs/2410.09268'
data: 'https://zenodo.org/records/12584502'
counter_id: 'C28'
abstract: "<p><b>Abstract</b>. Students often struggle with solving programming problems when learning to code, especially when they have to do it online, with one of the most common disadvantages of working online being the lack of personalized help. This help can be provided as next-step hint generation, i.e., showing a student what specific small step they need to do next to get to the correct solution. There are many ways to generate such hints, with large language models (LLMs) being among the most actively studied right now.</p><p>While LLMs constitute a promising technology for providing personalized help, combining them with other techniques, such as static analysis, can significantly improve the output quality. In this work, we utilize this idea and propose a novel system to provide both textual and code hints for programming tasks. The pipeline of the proposed approach uses a chain-of-thought prompting technique and consists of three distinct steps: (1) generating subgoals - a list of actions to proceed with the task from the current student's solution, (2) generating the code to achieve the next subgoal, and (3) generating the text to describe this needed action. During the second step, we apply static analysis to the generated code to control its size and quality. The tool is implemented as a modification to the open-source JetBrains Academy plugin, supporting students in their in-IDE courses.</p><p>To evaluate our approach, we propose a list of criteria for all steps in our pipeline and conduct two rounds of expert validation. Finally, we evaluate the next-step hints in a classroom with 14 students from two universities. Our results show that both forms of the hints - textual and code - were helpful for the students, and the proposed system helped them to proceed with the coding tasks.</p>"
---