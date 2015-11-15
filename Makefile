LATEX=pdflatex
LATEX_OPTS=--halt-on-error --shell-escape --file-line-error


PDFS := $(patsubst %.tex,%.pdf,$(wildcard *.tex))

default: all

all: $(PDFS)

%.pdf: %.tex
	$(LATEX) $(LATEX_OPTS) $<

clean:
	rm -f $(PDFS) *.aux *.log

.PHONY: default all clean
