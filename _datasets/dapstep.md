---
title: "DapStep"
description: "A dataset of stack traces and developer labels for assignee predictions."
collection: datasets
permalink: /datasets/dapstep
redirect_from:
  - /dataset/dapstep
  - /dataset/dapstep/
tag: 'A dataset of stack traces and developer labels for assignee predictions.'
pdf: 'https://arxiv.org/abs/2201.05256'
data: 'https://github.com/Sushentsev/DapStep'
paperurl: 'https://doi.org/10.1109/SANER53432.2022.00033'
abstract: "<p>The <b>Assignee Prediction Dataset</b> consists of error stack traces and annotations to them. All annotations were collected from the IntelliJ IDEA Community using the git blame command. The dataset is anonymized, each entity is encoded with a unique identifier, all the temporal data has been shifted by a fixed timestamp. The <i>reports</i> directory contains error reports, each report includes a unique report identifier (id), error time (timestamp), and a stack trace (elements). Each stack frame consists of the method name (name), file name (file_name), line number (line_number), annotation commit hash (commit_hash), and subsystem (subsystem). The <i>labels.csv</i> file associates each error report (rid) with the developer (uid) who fixed the given error .</p>"
---