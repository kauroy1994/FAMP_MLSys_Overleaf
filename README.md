# Compile and edit
Upload this directory to Overleaf. Select main.tex and compile with pdfLaTeX.
Then select appendix.tex and compile the separately uploaded appendix.

The main document has ten pages of main content and eleven total PDF pages.
It contains five explicitly empty performance tables in tables/01..05*.tex.
The appendix has ten pages and its hardware results table is also empty.
Configuration and protocol tables contain fixed design parameters, not results.

Do not automatically substitute pilot measurements for confirmatory table cells.
Use tables/table_registry.csv and the full package's frozen protocol and baseline
status registry. The main bibliography lists all authors and includes an explicit
AI Usage Disclosure after the references.

Before submission, replace the comment-condensed mirror transcription of
mlsys2025.sty with the officially linked archive, recompile and check the page
count. STYLE_PROVENANCE.md documents the retrieval limitation. The code package
contains fetch_official_style.py. The current format passes its geometry checks.

The PDFs are anonymous research drafts, not a claim that the actual empirical
submission or human review is complete. See the full package's submission checklist.
