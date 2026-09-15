---
title: "LitmusKt"
description: "A litmus testing tool for Kotlin."
collection: tools
permalink: /tools/litmuskt
redirect_from:
  - /tool/litmuskt
paperurl: 'https://doi.org/10.1145/3696630.3728584'
tool: 'https://github.com/Jetbrains-Research/litmuskt'
pdf: 'https://arxiv.org/abs/2501.07472'
video: "https://www.youtube.com/watch?v=gXI0aYJDnRw"
tag: 'A litmus testing tool for Kotlin. I only helped write the paper.'
abstract: '<p><b>LitmusKt</b> is the first tool for litmus testing concurrent programs in Kotlin. The tool's novelty also lies in the fact that Kotlin is a multiplatform language, i.e., it compiles into multiple platforms, which means that the concurrency has to be tested on several of them. Our tool allows writing litmus tests in a single custom DSL, and these tests are then run in Kotlin/Native and Kotlin/JVM, two main platforms for concurrent programming in Kotlin. Using LitmusKt, we discovered novel bugs in the Kotlin compiler, which we then fixed and they are no longer present. Moreover, LitmusKt was integrated into the CI pipeline for Kotlin.</p>'
---