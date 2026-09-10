---
layout: archive
title: "Tools"
description: "Software research tools developed or contributed to by Yaroslav Golubev, including Buckwheat, a multi-language source-code tokenizer."
permalink: /tools/
author_profile: true
---

{% include base_path %}

<p style="color:#888888;"><i>In my research, I have personally developed and maintained only one tool: 
<a href="https://areyde.com/tool/buckwheat"><b>Buckwheat</b></a>, a multi-language tokenizer for extracting identifiers from source code.
However, I participated in the development of several other tools or applied them for the analysis of large corpora of code. 
This page aims to conveniently list all such tools.</i></p>

{% for post in site.tools %}
{% include archive-single.html %}
{% endfor %}