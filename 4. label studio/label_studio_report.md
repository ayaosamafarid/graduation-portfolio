# Label Studio Report

---

# Overview

This report summarizes the annotation work completed using Label Studio for two required projects:

- **Project A:** Legal Named Entity Recognition (NER)
- **Project B:** Prompt Classification

Both projects were completed successfully following the provided annotation guidelines. After reviewing all annotations, the projects were exported in both **JSON** and **JSON-MIN** formats.

---

# Project A – Legal Named Entity Recognition (NER)

## Objective

The objective of this project was to identify and annotate legal named entities appearing in contracts, court judgments, arbitration decisions, employment agreements, licensing agreements, and other legal documents.

## Entity Types

The following entity types were used:

| Entity Type | Count |
|-------------|------:|
| LEGAL_TERM | 42 |
| ROLE | 28 |
| ORG | 18 |
| JURISDICTION | 16 |
| DATE | 15 |
| LAW_STATUTE | 13 |
| MONEY | 13 |
| COURT | 11 |
| CASE | 5 |
| PERSON | 5 |

## Annotation Summary

A total of **18 legal documents** were annotated.

---

# Project B – Prompt Classification

## Objective

The second project focused on analysing prompts according to prompt-engineering techniques, quality, risk level, and overall effectiveness.

Each prompt was annotated with:

- Prompting Technique(s)
- Quality Level
- Risk Category
- Rating (1–5)
- Short Justification

A total of **18 prompts** were classified.

---

# Prompt Quality Distribution

| Quality | Count |
|---------|------:|
| Strong Production Ready | 7 |
| Poor / Underspecified | 7 |
| Workable Needs Edits | 2 |
| Self-Contradictory | 2 |
---

# Prompt Risk Distribution

| Risk | Count |
|------|------:|
| Safe | 15 |
| Prompt Injection / Jailbreak | 1 |
| High-Stakes Quality Lowering | 1 |
| Policy Violation Request | 1 |

Most prompts were classified as **Safe**, while a small number represented jailbreak attempts or unsafe high-stakes instructions.

---

## 2. Organization vs. Legal Role

Some texts contained both an organization and its legal role.

Example:

- Data Controller → ROLE
- Meridian Health GmbH → ORG

Each element was annotated independently because they represent different semantic categories.

---

## 3. Prompt Quality Evaluation

Some prompts already contained useful prompt-engineering strategies but still lacked important information such as examples or output specifications.

These prompts were classified as **Workable Needs Edits** instead of **Strong Production Ready**.

---

# Quality Assurance

The following quality checks were performed before exporting:

- All tasks were annotated.
- Annotation consistency was reviewed.
- Entity boundaries were checked.
- Prompt labels were verified.
- Final exports were validated before submission.

---

# Deliverables

The submission includes:

- projectA_NER_export.json
- projectA_NER_export_min.json
- projectB_prompts_export.json
- projectB_prompts_export_min.json
- Label Studio screenshots
- label_studio_report.md

---

# Conclusion

Both Label Studio projects were completed successfully according to the provided annotation guidelines. The exported datasets were reviewed to ensure annotation consistency and correctness before submission.