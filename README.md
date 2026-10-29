# MLSys 2027 frozen-evidence manuscript

Compile `main.tex` and `appendix.tex` separately with pdfLaTeX/BibTeX (Overleaf) or `latexmk -pdf main.tex` and `latexmk -pdf appendix.tex`. Upload the appendix separately. The paper uses the neutral review name E-Mem and a new title; the public implementation/project name is FAMP.

## Scope
The paper reports 42 small-backbone development jobs, one ResNet18GN diagnostic, the reported CIFAR-100 2 MiB result (32% across compared methods, zero admissions), the 64 MiB strong result (10%, zero admissions), and qualitative three-seed arithmetic/nonlinear comparisons with no robust gain over independent. No new experiments are authorized or executed. Missing per-seed scores, baseline identities, hardware costs, or checkpoints are not reconstructed.

The appendix transcribes the Cell 20/22 decision traces. `tables/table_registry.csv` maps claims to recorded evidence. Full notebooks, training code, and raw campaign artifacts are absent from this manuscript repository. Reported audit PASS statements are not independent rechecks of unavailable artifacts.

## Build and PDF freshness
Both revised sources compiled successfully with the Codex desktop compiler using the bundled style and source-based figure fallbacks. That check does not certify the official style, final page count, or visual layout.

The GitHub workflow downloads the official MLSys 2025 style required for 2027, compiles both PDFs, checks unresolved references and the main-content endpoint, and uploads fresh PDFs/logs as `manuscript-build`. Its status must be checked; adding a workflow is not a successful build. The previously committed PDFs are removed from the revision branch because they describe the old empty-table protocol draft. They remain in Git history. Use freshly compiled PDFs, never the old exports.

All original bibliography entries and figure assets/sources are preserved. The inline figure sources are a faithful fallback when rendered PDFs are missing; they introduce no result charts. The style provenance caveat remains in `STYLE_PROVENANCE.md`.

## Before uploading
Read `SUBMISSION_CHECKS.md`. A scientifically bounded draft and a successful source compilation do not replace author validation, official-style verification, PDF inspection, or OpenReview submission.

