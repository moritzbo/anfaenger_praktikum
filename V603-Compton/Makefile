all: build/V603-Compton.pdf

# hier Python-Skripte:
build/plot1.pdf: python/plot1.py matplotlibrc header-matplotlib.tex data/EmissionCu.txt| build
	TEXINPUTS=$$(pwd): python python/plot1.py
build/plot2.pdf: python/Transmissionfertig.py matplotlibrc header-matplotlib.tex data/Nohnekorrigiert.txt data/Nalukorrigiert.txt data/wavelength.txt data/transmission.txt | build
	TEXINPUTS=$$(pwd): python python/Transmissionfertig.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/V603-Compton.pdf: build/plot1.pdf \
						build/plot2.pdf \

build/V603-Compton.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	V603-Compton.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
