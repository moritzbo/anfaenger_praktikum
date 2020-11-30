all: build/GraphDarstAufg1.pdf

build/plot1.pdf: python/plot1.py header-matplotlib.tex matplotlibrc python/messungen.txt| build
		TEXINPUTS=$$(pwd): python python/plot1.py

build/plot2.pdf: python/plot2.py header-matplotlib.tex matplotlibrc python/messungen.txt| build
		TEXINPUTS=$$(pwd): python python/plot2.py

build/plot3.pdf: python/plot3.py header-matplotlib.tex matplotlibrc python/messungen.txt| build
		TEXINPUTS=$$(pwd): python python/plot3.py

build/plot4.pdf: python/plot4.py header-matplotlib.tex matplotlibrc python/messungen.txt| build
		TEXINPUTS=$$(pwd): python python/plot4.py

build/plot5.pdf: python/plot5.py header-matplotlib.tex matplotlibrc python/messungen.txt| build
		TEXINPUTS=$$(pwd): python python/plot5.py

build/plot6.pdf: python/plot6.py header-matplotlib.tex matplotlibrc python/messungen.txt| build
		TEXINPUTS=$$(pwd): python python/plot6.py

build/GraphDarstAufg1.pdf: build/plot1.pdf \
					build/plot2.pdf \
					build/plot3.pdf \
					build/plot4.pdf \
					build/plot5.pdf \
					build/plot6.pdf

build/GraphDarstAufg1.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	GraphDarstAufg1.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
