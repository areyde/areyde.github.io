---
title: "All You Need Is Logs: Improving Code Completion by Learning from Anonymous IDE Usage Logs"
authors: '<i>Vitaliy Bibaev, Alexey Kalina, Vadim Lomshakov, Yaroslav Golubev, Alexander Bezzubov, Nikita Povarov, and Timofey Bryksin</i>'
status: "published"
collection: publications
permalink: /publications/2022-11-14-logs-for-code-completion
date: 2022-11-14
venue: "the proceedings of <b>ESEC/FSE'22</b>"
level: 'A*'
paperurl: 'https://doi.org/10.1145/3540250.3558968'
pdf: 'https://arxiv.org/abs/2205.10692'
counter_id: 'C20'
abstract: "<p><b>Abstract</b>. Integrated Development Environments (IDE) are designed to make users more productive, as well as to make their work more comfortable. To achieve this, a lot of diverse tools are embedded into IDEs, and the developers of IDEs can employ anonymous usage logs to collect the data about how they are being used to improve them. A particularly important component that this can be applied to is code completion, since improving code completion using statistical learning techniques is a well-established research area.</p><p>In this work, we propose an approach for collecting completion usage logs from the users in an IDE and using them to train a machine learning based model for ranking completion candidates. We developed a set of features that describe completion candidates and their context, and deployed their anonymized collection in the Early Access Program of IntelliJ-based IDEs. We used the logs to collect a dataset of code completions from users, and employed it to train a ranking CatBoost model. Then, we evaluated it in two settings: on a held-out set of the collected completions and in a separate A/B test on two different groups of users in the IDE. Our evaluation shows that using a simple ranking model trained on the past user behavior logs significantly improved code completion experience. Compared to the default heuristics-based ranking, our model demonstrated a decrease in the number of typing actions necessary to perform the completion in the IDE from 2.073 to 1.832.</p><p>The approach adheres to privacy requirements and legal constraints, since it does not require collecting personal information, performing all the necessary anonymization on the client's side. Importantly, it can be improved continuously: implementing new features, collecting new data, and evaluating new models - this way, we have been using it in production since the end of 2020.</p>"
---