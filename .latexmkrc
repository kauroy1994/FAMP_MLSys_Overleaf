$pdf_mode = 1;
# The supplied execution image has a broken 'bibtex' alternative. On Overleaf
# the standard command is used; no platform-specific binary is required there.
if (-x '/usr/bin/bibtex.original') { $bibtex = 'bibtex.original %O %B'; }
