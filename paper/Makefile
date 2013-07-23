%.pdf : %.tex
	pdflatex $*
	bibtex $*
	pdflatex $*
	pdflatex $*

all : paper.pdf talk.pdf

paper.pdf : paper.tex paper.bib Makefile images/forloop-highlight.pdf images/countA.pdf

talk.pdf : talk.tex images/KnoxLogo.pdf images/YCPLogo.pdf

clean :
	rm -f paper.pdf *.aux *.log *.bbl *.blg

depend :
	./mkdep.pl -b poster.tex > depend.mak

depend.mak :
	touch $@

#include depend.mak
