---
layout: archive
title: "Datasets, benchmarks, & tools 🛠️"
description: "Datasets, benchmarks, & tools in software engineering research developed or contributed to by Yaroslav Golubev."
permalink: /datasets_and_tools/
redirect_from:
  - /tools/
  - /tool/
  - /datasets/
  - /dataset/
author_profile: true
---

{% include base_path %}

<p style="color:#888888;"><i>This page aims to list in a convenient manner all the artifacts of my software engineering research that can be directly reused.
This includes various datasets (for training models or for studying further), benchmarks for evaluation, and tools for different
aspects of software engineering research.</i></p>

<h2>Datasets & Benchmarks</h2>

<p style="color:#888888;"><i>With the advent of AI, benchmarks left the halls of academia and became mainstream in all conversations about technology.
From the very start, JetBrains Research had a very open policy about publishing data — we basically published everything we were legally allowed to.
Because of that, quite a few datasets and benchmarks accumulated that I had something to do with.</i></p>

{% for post in site.datasets %}
{% include archive-single.html %}
{% endfor %}

<h2>Tools</h2>

<p style="color:#888888;"><i>In my research, I have personally developed and maintained only one tool: 
<a href="https://areyde.com/tools/buckwheat"><b>Buckwheat</b></a>, a multi-language tokenizer for extracting identifiers from source code.
However, I participated in the development of several other tools or applied them for the analysis of large corpora of code.</i></p>

{% for post in site.tools %}
{% include archive-single.html %}
{% endfor %}