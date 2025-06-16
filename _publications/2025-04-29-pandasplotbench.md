---
title: "Drawing Pandas: A Benchmark for LLMs in Generating Plotting Code"
authors: '<i>Timur Galimzyanov, Sergey Titov, Yaroslav Golubev, and Egor Bogomolov</i>'
status: "published"
collection: publications
permalink: /publications/2025-04-29-pandasplotbench
date: 2025-04-29
venue: "the proceedings of <b>MSR'25</b>"
level: "A"
paperurl: "https://doi.org/10.1109/MSR66628.2025.00083"
pdf: 'https://arxiv.org/abs/2412.02764'
data: 'https://huggingface.co/datasets/JetBrains-Research/plot_bench'
tool: 'https://github.com/JetBrains-Research/PandasPlotBench'
counter_id: 'С30'
abstract: "<p><b>Abstract</b>. This paper introduces the human-curated PandasPlotBench dataset, designed to evaluate language models' effectiveness as assistants in visual data exploration. Our benchmark focuses on generating code for visualizing tabular data - such as a Pandas DataFrame - based on natural language instructions, complementing current evaluation tools and expanding their scope. The dataset includes 175 unique tasks. Our experiments assess several leading Large Language Models (LLMs) across three visualization libraries: Matplotlib, Seaborn, and Plotly. We show that the shortening of tasks has a minimal effect on plotting capabilities, allowing for the user interface that accommodates concise user input without sacrificing functionality or accuracy. Another of our findings reveals that while LLMs perform well with popular libraries like Matplotlib and Seaborn, challenges persist with Plotly, highlighting areas for improvement. We hope that the modular design of our benchmark will broaden the current studies on generating visualizations. Our benchmark is available online: https://huggingface.co/datasets/JetBrains-Research/plot_bench. The code for running the benchmark is also available: https://github.com/JetBrains-Research/PandasPlotBench.</p>"
---