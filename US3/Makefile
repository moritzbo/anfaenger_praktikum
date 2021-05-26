all: build/US3.pdf

hier Python-Skripte:

build/plot1.pdf: python/plt.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python python/plt.py
build/plot2.pdf: python/plt.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python python/plt.py
build/plot3.pdf: python/plt.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python python/plt.py

hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/US3.pdf: build/plot1.pdf \
				build/plot2.pdf
				build/plot3.pdf

build/US3.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	US3.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
