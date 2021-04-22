all: build/V353-RC.pdf

# hier Python-Skripte:
build/plot1.pdf: python/plot1.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python python/plot1.py
build/plot4.pdf: python/plot2.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python python/plot2.py
build/plot5.pdf: python/plot2.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python python/plot2.py
 
# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/V353-RC.pdf: build/plot1.pdf \
					build/plot4.pdf \
					build/plot5.pdf \

build/V353-RC.pdf: FORCE | build
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
