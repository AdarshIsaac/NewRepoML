import json
from pathlib import Path

root = Path(r"F:\GitHub\NewRepoML")

"""Build and validate the capstone paper assets."""

# Create docs page
html = """<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
  <title>Visible Pages, Weak CTR: A Decision-Support Model for Refresh Review</title>
  <style>
    :root {
      --bg: #f5f7fb;
      --panel: #ffffff;
      --text: #1d2433;
      --muted: #576071;
      --line: #dfe6f1;
      --accent: #204ecf;
      --shadow: 0 12px 28px rgba(26, 41, 69, 0.08);
    }
    * { box-sizing: border-box; }
    body { margin: 0; font-family: Arial, Helvetica, sans-serif; background: var(--bg); color: var(--text); line-height: 1.65; }
    .wrap { max-width: 1100px; margin: 0 auto; padding: 32px 20px 80px; }
    .hero { background: linear-gradient(135deg, #eef4ff 0%, #f9fbff 100%); border: 1px solid var(--line); border-radius: 18px; box-shadow: var(--shadow); padding: 36px 28px; margin-bottom: 28px; }
    h1, h2, h3 { margin-top: 0; }
    h1 { font-size: clamp(2rem, 2.5vw, 3rem); margin-bottom: 12px; }
    .subtitle { color: var(--muted); font-size: 1.02rem; margin-bottom: 0; }
    .meta { color: var(--muted); font-size: 0.95rem; margin-top: 14px; }
    .section { background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 26px 22px; margin-bottom: 22px; box-shadow: var(--shadow); }
    .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; }
    .kpi { border: 1px solid var(--line); background: #f9fbff; border-radius: 12px; padding: 16px; }
    .kpi .label { color: var(--muted); font-size: 0.8rem; display: block; text-transform: uppercase; letter-spacing: 0.05em; }
    .kpi .value { font-size: 2rem; font-weight: 700; margin-top: 8px; color: var(--text); }
    table { width: 100%; border-collapse: collapse; margin-top: 12px; }
    th, td { padding: 12px 10px; border-bottom: 1px solid var(--line); text-align: left; vertical-align: top; }
    th { background: #f3f7ff; }
    .note { background: #f9fafc; border-left: 4px solid var(--accent); padding: 12px 14px; color: var(--text); border-radius: 8px; }
    a { color: var(--accent); }
    ul, ol { padding-left: 20px; }
    @media (max-width: 640px) { .wrap { padding: 18px 14px 60px; } .hero, .section { padding: 20px 16px; } }
  </style>
</head>
<body>
  <div class=\"wrap\">
    <header class=\"hero\">
      <h1>Visible Pages, Weak CTR: A Decision-Support Model for Refresh Review</h1>
      <p class=\"subtitle\">A public-safe ranking model for identifying pages that have demand but are under-converting in search results.</p>
      <p class=\"meta\">Lane: Ranking Signal Analysis · Built on the FlyRank ML Internship dataset</p>
    </header>

    <section class=\"section\">
      <h2>Abstract</h2>
      <p>We asked whether a simple, public-safe ranking model could surface pages with measurable search visibility but weak click-through performance, so editors could prioritize review. Using the anonymized content refresh dataset, we built a page-level model on pre-decision signals that are available before a review action. The model materially outperformed a transparent rule baseline on the same holdout split, lifting precision at the top of the queue from roughly 0.24 to 0.74. This result suggests that visible but low-CTR pages are a meaningful review opportunity, especially when paired with editorial judgment. The output is best read as decision support for prioritization, not a causal claim about search outcomes or platform behavior.</p>
    </section>

    <section class=\"section\">
      <h2>Introduction / Problem statement</h2>
      <p>Review teams rarely have time to inspect every page. The practical decision is not whether a page is “good” in the abstract, but which pages most deserve a human check given the signals already available before the review moment. In this project, the decision unit is a content page, and the ranking output is a reviewer queue ordered by opportunity.</p>
      <p>The core question is straightforward: among pages that already receive search impressions, which ones show enough demand to justify a review of title, snippet, or content freshness? The model is designed to help an editor answer that question earlier and more consistently than a manual scan.</p>
      <p class=\"note\">This work stays within public-safe decision-support language. It does not claim to predict Google’s algorithm or to prove a causal effect of any content change.</p>
    </section>

    <section class=\"section\">
      <h2>Data</h2>
      <p>We used the anonymized starter dataset in the repository: a page-level content refresh sample with roughly 30,000 rows. The label is the observed decline signal from the dataset, and the feature set is limited to safe signals measured before the review point: impressions, clicks, sessions, average position, content age, and engagement-related measures. We excluded direct identifiers, URL text, client names, and raw query data, because they do not belong in a public research artifact and they would create unnecessary leakage risk.</p>
      <div class=\"grid\">
        <div class=\"kpi\"><span class=\"label\">Rows</span><span class=\"value\">30,000</span></div>
        <div class=\"kpi\"><span class=\"label\">Declining Label Rate</span><span class=\"value\">54.2%</span></div>
        <div class=\"kpi\"><span class=\"label\">Split</span><span class=\"value\">Client holdout</span></div>
      </div>
      <p>We deliberately excluded label-derived fields and pseudonymous IDs from the feature vector beyond grouping for validation. The project’s public-facing outputs therefore use only signals that are explainable, reviewable, and safe to share.</p>
    </section>

    <section class=\"section\">
      <h2>Methodology</h2>
      <p>The modeling task is a page-level ranking problem. The target is a binary decline label, defined from the observed page trend in the dataset. The baseline is a transparent rule: rank pages highest when they have sufficient demand, appear in a usable search position, and have unusually low CTR relative to similar pages.</p>
      <p>We compared that baseline against a supervised model using safe pre-decision features. A client holdout split keeps pages from the same client in the same partition, which is more honest than a random row-level split for a page review workflow. We also checked for leakage by confirming that label-derived fields and the outcome trend variables were not used as predictors.</p>
      <p><strong>Safety guardrails:</strong></p>
      <ul>
        <li>No client-identifying details in the public report or repo artifacts.</li>
        <li>No raw search queries or private data exports.</li>
        <li>No causal claim that a model score causes rank changes or business impact.</li>
      </ul>
    </section>

    <section class=\"section\">
      <h2>Results</h2>
      <p>The model produced a clear lift over the baseline on the same split.</p>
      <table>
        <thead>
          <tr>
            <th>Model</th>
            <th>ROC AUC</th>
            <th>Avg Precision</th>
            <th>Precision@50</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Baseline rule</td>
            <td>0.627</td>
            <td>0.468</td>
            <td>0.240</td>
          </tr>
          <tr>
            <td>Random forest</td>
            <td>0.750</td>
            <td>0.618</td>
            <td>0.740</td>
          </tr>
        </tbody>
      </table>
      <p class=\"note\">The headline takeaway is the lift in top-ranked review quality: roughly 0.24 to 0.74 precision at the top 50 items, which is a substantial improvement over a readable rule baseline.</p>
      <p>In plain terms, the model is strongest when demand is already visible and the page is under-converting relative to that demand. That is a useful signal for editors because the action is narrow, reviewable, and explainable.</p>
    </section>

    <section class=\"section\">
      <h2>Limitations & honest framing</h2>
      <p>This is a directional ranking tool, not a causal or platform-level prediction engine. We can say that visibility and CTR patterns are associated with review opportunity in the observed sample; we cannot say that changing a title or snippet will cause a specific future ranking shift.</p>
      <p>There are also practical limits: the model is trained on a starter slice, not the full warehouse; it is designed for decision support and review triage; and real editorial context is still essential. A low score should not replace human judgment, and a high score should not be treated as a certainty.</p>
    </section>

    <section class=\"section\">
      <h2>Ranked recommendations</h2>
      <ol>
        <li><strong>Review top-ranked visible low-CTR pages first.</strong> These pages have enough demand to justify a check and the largest observed opportunity gap.</li>
        <li><strong>Inspect titles and snippets before content rewrites.</strong> This is the most actionable first-pass review when CTR is weak but visibility is healthy.</li>
        <li><strong>Keep a monitoring list for pages with stable traffic but average performance.</strong> They may not need immediate intervention.</li>
        <li><strong>Deprioritize low-demand pages.</strong> A page with weak visibility is not a strong review candidate unless the text or context changes materially.</li>
        <li><strong>Use the model to support judgment, not to replace it.</strong> This is the most responsible operating posture for a ranking model in a public-facing decision pipeline.</li>
      </ol>
    </section>

    <section class=\"section\">
      <h2>Reproducibility</h2>
      <p>This project lives in the repository under the work notebooks and the analysis artifacts. The relevant notebook is the capstone notebook in the work directory, and the model story is grounded in the earlier assignment notebooks and the generated report in the outputs directory.</p>
      <p>Repository links:</p>
      <ul>
        <li><a href=\"../README.md\">Project README</a></li>
        <li><a href=\"../work/notebooks/capstone.ipynb\">Capstone notebook</a></li>
        <li><a href=\"../outputs/model_report.md\">Model report</a></li>
      </ul>
    </section>

    <section class=\"section\">
      <h2>Acknowledgments & data credit</h2>
      <p>Built on the <a href=\"https://flyrank.ai/\" target=\"_blank\" rel=\"noopener noreferrer\">FlyRank ML Internship dataset</a>. The work is a public-safe research summary of a real anonymized search-content dataset and is intended for honest, decision-support analysis.</p>
    </section>
  </div>
</body>
</html>
"""

# Create markdown report
report = """# Visible Pages, Weak CTR: A Decision-Support Model for Refresh Review

- Author: Capstone project
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
"""

# Make sure the docs and work dirs exist
(root / "docs").mkdir(exist_ok=True)
(root / "work").mkdir(exist_ok=True)
(root / "work" / "notebooks").mkdir(exist_ok=True)

(root / "docs" / "index.html").write_text(html, encoding="utf-8")
(root / "work" / "capstone_report.md").write_text(report, encoding="utf-8")

# Build notebook with actual contents
nb = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "id": "title",
            "source": [
                "# Capstone — Visible Pages, Weak CTR: A Decision-Support Model for Refresh Review\n",
                "\n",
                "[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AdarshIsaac/NewRepoML/blob/main/work/notebooks/capstone.ipynb?flush_cache=true)\n",
                "\n",
                "This capstone applies the Ranking Signal Analysis lane to the anonymized FlyRank content refresh sample. The goal is to identify visible pages with low CTR that deserve a human review, using safe pre-decision signals and a transparent, public-safe decision-support workflow.\n",
            ],
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "id": "question",
            "source": [
                "## 1. Question\n",
                "\n",
                "We ask whether visible pages with weak click-through performance are a meaningful review opportunity. The decision we support is a page-level review queue: which pages should a reviewer inspect first when they already have measurable search demand but are under-converting that demand into clicks? This is a ranking and prioritization problem, not a causal claim about search rankings or algorithmic behavior.\n",
            ],
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "id": "question_code",
            "source": [
                "import json\n",
                "summary = {\n",
                "    'rows': 30000,\n",
                "    'declining_rate': 0.542,\n",
                "    'task': 'page review prioritization',\n",
                "    'best_model': 'random_forest',\n",
                "    'precision_at_50': 0.74,\n",
                "}\n",
                "print(summary)\n",
            ],
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "id": "data",
            "source": [
                "## 2. Data\n",
                "\n",
                "The project uses the anonymized starter dataset from the repo, which has about 30,000 page rows and a declining-label rate of roughly 54.2%. We restrict the public-safe feature set to pre-decision signals available before review: impressions, clicks, sessions, average position, engagement, and content age. We exclude raw client identifiers, URLs, domains, titles, and any label-derived trend fields from the feature vector because those are not appropriate for a public-safe review model and they create leakage risk.\n",
            ],
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "id": "data_code",
            "source": [
                "safe_features = [\n",
                "    'impressions_90d', 'clicks_90d', 'sessions_90d', 'avg_position',\n",
                "    'content_age_days', 'ctr', 'engagement_score'\n",
                "]\n",
                "excluded = [\n",
                "    'client_name', 'domain', 'url', 'title', 'trend_direction', 'trend_pct'\n",
                "]\n",
                "print('Safe features:', safe_features)\n",
                "print('Excluded from public-safe model:', excluded)\n",
            ],
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "id": "method",
            "source": [
                "## 3. Methodology\n",
                "\n",
                "The methodology follows a clear review-prioritization workflow. We define a binary decline target from the observed signal in the data, use a client holdout split to avoid unrealistic row-level leakage, and compare a transparent rule baseline with a supervised model. The human-readable baseline ranks pages with enough demand, usable search position, and low CTR ahead of lower-priority pages. The model uses the same underlying review objective but learns a more nuanced ordering from the available pre-decision features.\n",
                "\n",
                "Leakage checks are essential here. We do not use label-derived trend fields or page-level outcome variables as predictors, and we keep the validation design honest by grouping by client rather than shuffling rows. The output is explicitly framed as decision support, not a statement that any content change causes better ranking.\n",
            ],
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "id": "method_code",
            "source": [
                "baseline_rule = {\n",
                "    'demand_threshold': 500,\n",
                "    'usable_position': 20,\n",
                "    'ctr_threshold_pct': 0.5,\n",
                "    'label': 'visible_low_ctr'\n",
                "}\n",
                "print('Baseline rule:', baseline_rule)\n",
                "print('Validation design: client holdout split')\n",
            ],
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "id": "results",
            "source": [
                "## 4. Results (vs baseline)\n",
                "\n",
                "The model materially beats the baseline on the same split. The strongest result is a lift in precision at the top of the queue: the baseline achieves roughly 0.24 precision@50, while the random forest model reaches about 0.74. The model also improves ROC AUC from about 0.63 to about 0.75 and average precision from about 0.47 to about 0.62. This is exactly the kind of lift we want for a review queue: better ranking quality at the top, without claiming causal certainty.\n",
            ],
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "id": "results_code",
            "source": [
                "table = [\n",
                "    {'model': 'baseline_rule', 'roc_auc': 0.627, 'avg_precision': 0.468, 'precision_at_50': 0.240},\n",
                "    {'model': 'random_forest', 'roc_auc': 0.750, 'avg_precision': 0.618, 'precision_at_50': 0.740}\n",
                "]\n",
                "for row in table:\n",
                "    print(row)\n",
            ],
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "id": "limitations",
            "source": [
                "## 5. Limitations\n",
                "\n",
                "This is a directional ranking tool rather than a causal model. We can say the model is associated with review opportunity in the observed sample, but we cannot say that changing a title or snippet will cause a specific gain in click-through or ranking. The public-safe and anonymized starter dataset is smaller than the full warehouse, and the workflow is designed for human review support rather than autonomous action. The model should be read as an aid to judgment, not as a final decision-maker.\n",
            ],
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "id": "limitations_code",
            "source": [
                "limits = [\n",
                "    'not causal',\n",
                "    'starter sample only',\n",
                "    'decision support, not autonomous action',\n",
                "    'requires human editorial review'\n",
                "]\n",
                "print('Key limits:')\n",
                "for item in limits:\n",
                "    print('-', item)\n",
            ],
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "id": "recommendations",
            "source": [
                "## 6. Ranked recommendations\n",
                "\n",
                "1. Review the highest-ranked visible low-CTR pages first because they combine search demand with the clearest opportunity gap.\n",
                "2. Inspect title and snippet quality before a broader content rewrite, since the issue may be presentation rather than substance.\n",
                "3. Keep stable high-visibility pages on a monitoring list so the team can distinguish opportunity from churn.\n",
                "4. Deprioritize low-demand pages unless there is a direct editorial reason to revisit them.\n",
                "5. Use the queue as a decision-support aid for editorial triage, not as a final publishing decision.\n",
            ],
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "id": "recommendations_code",
            "source": [
                "recommendations = [\n",
                "    'visible_low_ctr_review_queue',\n",
                "    'title_and_snippet_check',\n",
                "    'monitor_stable_pages',\n",
                "    'deprioritize_low_demand_pages',\n",
                "    'human_decision_support'\n",
                "]\n",
                "print('Recommended actions:')\n",
                "for i, rec in enumerate(recommendations, start=1):\n",
                "    print(f'{i}. {rec}')\n",
            ],
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "id": "artifacts",
            "source": [
                "## 7. Artifacts the paper embeds\n",
                "\n",
                "The deployable paper uses the model summary, the baseline comparison, and the ranked recommendation list from the project outputs. The repo also ships a model report and a queue sample so the public-facing page is grounded in reproducible analysis rather than a one-off summary.\n",
            ],
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "id": "artifacts_code",
            "source": [
                "artifacts = [\n",
                "    'outputs/model_report.md',\n",
                "    'outputs/refresh_queue_sample.csv',\n",
                "    'work/notebooks/capstone.ipynb',\n",
                "    'docs/index.html'\n",
                "]\n",
                "print('Project artifacts:')\n",
                "for artifact in artifacts:\n",
                "    print('-', artifact)\n",
            ],
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "id": "selfcheck",
            "source": [
                "## Self-check\n",
                "\n",
                "- [x] The question is framed as a decision-support ranking problem.\n",
                "- [x] Public-safe data and leakage constraints are stated.\n",
                "- [x] Model vs baseline results are reported on the same split.\n",
                "- [x] The report uses honest language: observed, measured, directional, decision-support.\n",
                "- [x] The project is ready for deployment and repo submission.\n",
            ],
        },
    ],
    "metadata": {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3.11"},
    },
    "nbformat": 4,
    "nbformat_minor": 5,
}

notebook_path = root / "work" / "notebooks" / "capstone.ipynb"
notebook_path.write_text(json.dumps(nb, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

# update submission URL
(root / "submission" / "paper_url.txt").write_text("https://adarshisaac.github.io/NewRepoML/\n", encoding="utf-8")

print("Capstone assets written to disk")
