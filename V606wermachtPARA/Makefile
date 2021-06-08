all: build/V606.pdf

# # hier Python-Skripte:
build/kurve1.pdf: python/plotkurve.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python python/plotkurve.py

build/kurve2.pdf: python/plotkurve.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python python/plotkurve.py

# # hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/V606.pdf: build/kurve1.pdf \
				build/kurve2.pdf \

build/V606.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	V606.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
