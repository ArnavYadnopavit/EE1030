#!/bin/bash
pdflatex $1.tex
termux-open $1.pdf
