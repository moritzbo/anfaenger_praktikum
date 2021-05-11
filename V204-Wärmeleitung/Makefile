all: build/V204-Wärmeleitung.pdf

# hier Python-Skripte:
build/plot1.pdf: python/plottry.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python python/plottry.py
build/plot2.pdf: python/plot2.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python python/plot2.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/V204-Wärmeleitung.pdf: build/plot1.pdf \
							 build/plot2.pdf \

build/V204-Wärmeleitung.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	V204-Wärmeleitung.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
