LATEX=pdflatex
LATEX_OPTS=--halt-on-error --shell-escape --file-line-error

PDFS := $(patsubst %,%.pdf,$(shell find -maxdepth 1 -name 'lection*' -type d))

default: all

all: $(PDFS)

.SECONDEXPANSION: 
%.pdf: PDFNAME = $(basename $@)
%.pdf: PDFPREREQ = $(PDFNAME)/$(PDFNAME).tex

%.pdf: $$(PDFPREREQ) 
	cd $$( dirname $< ); $(LATEX) $(LATEXOPTS) $$( basename $< ); mv $$( basename $< .tex ).pdf ..; cd -

clean:
	rm -f $(PDFS) */*.aux */*.log

.PHONY: default all clean
