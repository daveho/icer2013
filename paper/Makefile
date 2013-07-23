all : paper.pdf talk.pdf

paper.pdf : paper.tex paper.bib Makefile images/forloop-highlight.pdf images/countA.pdf
	pdflatex paper
	bibtex paper
	pdflatex paper
	pdflatex paper

talk.pdf : talk.tex images/KnoxLogo.pdf images/YCPLogo.pdf
	pdflatex talk

clean :
	rm -f paper.pdf talk.pdf *.aux *.log *.bbl *.blg

depend :
	./mkdep.pl -b poster.tex > depend.mak

depend.mak :
	touch $@

#include depend.mak
