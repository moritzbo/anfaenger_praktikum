all: build/V311-Hall-Effekt.pdf

#build/plot1.pdf: python/plot1.py header-matplotlib.tex matplotlibrc python/daten.dat| build
#		TEXINPUTS=$$(pwd): python python/plot1.py


#build/D206-Wärmepumpe.pdf: build/plot1.pdf 
					

build/V311-Hall-Effekt.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	V311-Hall-Effekt.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
