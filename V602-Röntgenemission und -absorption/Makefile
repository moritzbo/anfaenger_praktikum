all: build/V602-Röntgenemissionund-absorption.pdf

# hier Python-Skripte:
build/plot1.pdf: python/plot1.py matplotlibrc header-matplotlib.tex data/Bragg.txt | build
	TEXINPUTS=$$(pwd): python python/plot1.py
build/plot2.pdf: python/plot2.py matplotlibrc header-matplotlib.tex data/Emissionsspektrum.txt | build
	TEXINPUTS=$$(pwd): python python/plot2.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/V602-Röntgenemissionund-absorption.pdf: build/plot1.pdf \
												build/plot2.pdf \

build/V602-Röntgenemissionund-absorption.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	V602-Röntgenemissionund-absorption.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
