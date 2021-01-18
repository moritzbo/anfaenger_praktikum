all: build/DasGeigerMüllerzählrohr.pdf

# hier Python-Skripte:
build/plot1.pdf: python/plot.py matplotlibrc header-matplotlib.tex Daten/Kennlinie.dat| build
	TEXINPUTS=$$(pwd): python python/plot.py

build/plot2.pdf: python/test3.py matplotlibrc header-matplotlib.tex Daten/Zaehlrohrstrom.dat| build
	TEXINPUTS=$$(pwd): python python/test3.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/DasGeigerMüllerzählrohr.pdf: build/plot1.pdf \
								build/plot2.pdf

build/DasGeigerMüllerzählrohr.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	DasGeigerMüllerzählrohr.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
