all: build/V500.pdf

# hier Python-Skripte:
build/plot1.pdf: python/plot.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python python/plot.py
build/plot2.pdf: python/plot2.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python python/plot2.py
build/plot3.pdf: python/plot3.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python python/plot3.py
build/plot4.pdf: python/plot4.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python python/plot4.py
build/plot5.pdf: python/plot5.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python python/plot5.py


# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/V500.pdf: build/plot1.pdf \
				build/plot2.pdf \
				build/plot3.pdf \
				build/plot4.pdf \
				build/plot5.pdf \

build/V500.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	V500.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
