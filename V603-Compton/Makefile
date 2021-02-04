all: build/V603-Compton.pdf

# hier Python-Skripte:
#build/V603-Compton.pdf: plot.py matplotlibrc header-matplotlib.tex | build
#	TEXINPUTS=$$(pwd): python plot.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
#build/V603-Compton.pdf: build/plot.pdf

build/V603-Compton.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	V603-Compton.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
