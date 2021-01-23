all: build/V702AktivierungmitNeutronen.pdf

# hier Python-Skripte:
build/plot1.pdf: python/halbwertszeitvanadium.py header-matplotlib.tex matplotlibrc daten/Vanadium.txt| build
		TEXINPUTS=$$(pwd): python python/halbwertszeitvanadium.py

build/plot2.pdf: python/halbwertszeitvanadium.py header-matplotlib.tex matplotlibrc daten/Vanadium.txt| build
		TEXINPUTS=$$(pwd): python python/halbwertszeitvanadium.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/V702AktivierungmitNeutronen.pdf: build/plot1.pdf \
										build/plot2.pdf

build/V702AktivierungmitNeutronen.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	V702AktivierungmitNeutronen.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
