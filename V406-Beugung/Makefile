all: build/V406-BeugungAmSpalt.pdf

# hier Python-Skripte:
build/plot1.pdf: python/plot1.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python python/plot1.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/V406-BeugungAmSpalt.pdf: build/plot1.pdf \

build/V406-BeugungAmSpalt.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	V406.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
