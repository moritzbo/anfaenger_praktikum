all: build/V353 Das Relaxationsverhalten eines RC-KreisesDatei.pdf

# hier Python-Skripte:
#build/plot.pdf: plot.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: 

build/V353 Das Relaxationsverhalten eines RC-KreisesDatei.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	V353-RC.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
