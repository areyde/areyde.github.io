---
layout: archive
title: "Publications 📜"
description: "The full list of publications of Yaroslav Golubev. The list mostly includes SE and AI research from JetBrains Research, but also some early work in physics from ITMO University and theses in humanities."
permalink: /publications/
author_profile: true
---

{% include base_path %}

<p style="margin-bottom: -5px; padding-bottom: 0; color: #888888"><i><b>C</b> — Conference papers. <b>J</b> — Journal papers. <b>T</b> — Theses. <b>P</b> — Pre-prints.</i></p>

<p style="margin-bottom: -5px;"><b>Fields of study:</b></p>
<ul>
    <li><a href="#se"><b>Software Engineering & AI</b></a></li>
    <li><a href="#humanities"><b>Humanities</b></a></li>
    <li><a href="#physics"><b>Laser Technologies</b></a></li>
</ul>

<p style="margin-bottom: -5px; padding-bottom: 0; color: #888888"><i><a href="https://scholar.google.com/citations?user=qb_dl6AAAAAJ&hl=en">Google Scholar</a> says these publications have <b>{{ site.data.citations.total }}</b> citations. Cool!</i></p>

<h2 id="se">Software Engineering & AI</h2>

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

<h2 id="humanities">Humanities</h2>

{% for post in site.publicationsphilosophy reversed %}
{% include archive-single.html %}
{% endfor %}

<h2 id="physics">Laser Technologies</h2>

{% for post in site.publicationsphysics reversed %}
  {% include archive-single.html %}
{% endfor %}