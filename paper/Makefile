%.pdf : %.tex
	pdflatex $*
	bibtex $*
	pdflatex $*
	pdflatex $*

paper.pdf : paper.tex paper.bib Makefile images/forloop-highlight.pdf images/countA.pdf

#makeimages: images/*
#	sips -s format png images/forloop-highlight.pdf  --out images/forloop-highlight.png
#	sips -s format png images/countA.pdf  --out images/countA.png

clean :
	rm -f paper.pdf *.aux *.log *.bbl *.blg

depend :
	./mkdep.pl -b poster.tex > depend.mak

depend.mak :
	touch $@

#include depend.mak
