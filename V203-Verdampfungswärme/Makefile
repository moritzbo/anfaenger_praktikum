all: build/V203-Verdampfungswärme.pdf

# hier Python-Skripte:
build/plot1.pdf: python/plot1.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python python/plot1.py
build/plot2.pdf: python/plot2.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python python/plot2.py
build/plot3.pdf: python/plot3.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python python/plot3.py
build/plot4.pdf: python/plot4.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python python/plot4.py
build/plot5.pdf: python/plot5.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python python/plot5.py
build/plot6.pdf: python/plot5.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python python/plot5.py
build/plot7.pdf: python/plot5.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python python/plot5.py
# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/V203-Verdampfungswärme.pdf: build/plot1.pdf \
									build/plot2.pdf \
									build/plot3.pdf \
									build/plot4.pdf \
									build/plot5.pdf \
									build/plot6.pdf \
									build/plot7.pdf \

build/V203-Verdampfungswärme.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	V203-Verdampfungswärme.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
