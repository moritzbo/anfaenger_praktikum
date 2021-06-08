all: build/V606.pdf

# # hier Python-Skripte:
# build/plot.pdf: plot.py matplotlibrc header-matplotlib.tex | build
# 	TEXINPUTS=$$(pwd): python plot.py

# # hier weitere Abhängigkeiten für build/main.pdf deklarieren:
# build/main.pdf: build/plot.pdf

build/V606.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	V400.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
