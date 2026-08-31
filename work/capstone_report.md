# Visible Pages, Weak CTR: A Decision-Support Model for Refresh Review

- Author: Adarsh Isaac
- Lane: Ranking Signal Analysis
- Repo: NewRepoML
- Date: 2026-08-31

## 1. Problem framing

The decision this supports is a page-level review prioritization problem: which pages already have measurable search visibility but weak click-through performance should a human editor inspect first? The unit of analysis is a content page, the output is a ranked review queue, and the action is a human review of metadata and content before any content change is considered. The cost of a wrong call is wasted editorial time on pages that do not need intervention, but the cost of missing a strong review candidate is also real. A model helps because the review team cannot inspect every page manually, and the available signals are measurable before a decision point.

## 2. Data safety

We used the anonymized starter dataset in the repo, a page-level content refresh sample with about 30,000 rows. The public-safe feature set includes pre-decision signals such as impressions, clicks, sessions, average position, content age, and engagement-related measures. We explicitly excluded client names, domains, URLs, titles, raw query strings, and label-derived leakage fields from the public feature vector. The goal is to support review prioritization without exposing anything private or difficult to justify.

## 3. Baseline

The transparent baseline was a human-readable rule: rank pages with enough demand, usable search position, and unusually low CTR ahead of lower-priority items. This is a fair comparison because it uses the same data and same review objective as the model, but it is easier to explain and easier to audit. On the same split, the baseline achieved about 0.24 precision@50, while the model reached about 0.74 precision@50.

## 4. Model / analysis

The task is a page-level binary classification and ranking problem. The model uses safe pre-decision signals available before a review action, with a client holdout split to reduce leakage risk from repeated pages in the same client cohort. The target is the observed decline label from the anonymized data. There is no claim that this is a causal model of search behavior; the purpose is directional review support.

## 5. Evaluation

The model was compared directly against the baseline on the same split. The random forest model was the strongest performer with ROC AUC around 0.75 and precision@50 around 0.74. The baseline rule was materially weaker at around 0.63 ROC AUC and 0.24 precision@50. The model’s strongest value is not that it “knows” the algorithm, but that it consistently surfaces pages with strong visibility and weak CTR in a way a human can act on.

## 6. Interpretation

The model is most useful when a page already has measurable demand but is not converting that demand into clicks. In practical terms, these are the pages where a title, snippet, or content refresh could plausibly matter. The strongest signals are the ones linked to visibility, search position, and traffic volume, which is intuitive for a review queue. A model is not a substitute for editorial judgment, but it is a useful triage mechanism when the queue is long and the review budget is limited.

## 7. Recommendation

1. Review top-ranked visible low-CTR pages first.
2. Inspect titles and snippets before broader content rewrites.
3. Keep a monitoring list for pages with steady demand but unremarkable CTR.
4. Deprioritize low-demand pages unless there is a direct editorial reason to revisit them.
5. Treat the model as a decision-support tool rather than a final publishing decision.

## 8. Reproducibility

The capstone notebook and the supporting analysis live in the repo under the work directory. The repo also contains an output report and the ranked queue artifacts in the outputs folder. Reproduction requires the same environment as the starter repo and the project data already included in the repo or available through the approved dataset workflow. This work should be rerun with a fixed seed and in a fresh environment before final publication.

---

Built on the FlyRank ML Internship dataset: https://flyrank.ai/
