all: build/V602-Röntgenemissionund-absorption.pdf

# hier Python-Skripte:
build/plo


t1.pdf: python/plot1.py matplotlibrc header-matplotlib.tex data/Bragg.txt | build
	TEXINPUTS=$$(pwd): python python/plot1.py
build/plot2.pdf: python/plot2.py matplotlibrc header-matplotlib.tex data/Emissionsspektrum.txt | build
	TEXINPUTS=$$(pwd): python python/plot2.py

build/plotzink.pdf: python/plot6.py matplotlibrc header-matplotlib.tex data/Zink.txt | build
	TEXINPUTS=$$(pwd): python python/plot6.py

build/plotgallium.pdf: python/plot6.py matplotlibrc header-matplotlib.tex data/Gallium.txt | build
	TEXINPUTS=$$(pwd): python python/plot6.py

build/plotbrom.pdf: python/plot6.py matplotlibrc header-matplotlib.tex data/Brom.txt | build
	TEXINPUTS=$$(pwd): python python/plot6.py

build/plotrubidium.pdf: python/plot6.py matplotlibrc header-matplotlib.tex data/Rubidium.txt | build
	TEXINPUTS=$$(pwd): python python/plot6.py

build/plotstrontium.pdf: python/plot6.py matplotlibrc header-matplotlib.tex data/Strontium.txt | build
	TEXINPUTS=$$(pwd): python python/plot6.py

build/plotzirkonium.pdf: python/plot6.py matplotlibrc header-matplotlib.tex data/Zirkonium.txt | build
	TEXINPUTS=$$(pwd): python python/plot6.py

build/plotmoseley.pdf: python/newplot.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python python/newplot.py



# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/V602-Röntgenemissionund-absorption.pdf: build/plot1.pdf \
												build/plot2.pdf \
												build/plotzink.pdf \
												build/plotgallium.pdf \
												build/plotbrom.pdf \
												build/plotrubidium.pdf \
												build/plotstrontium.pdf \
												build/plotzirkonium.pdf \
												build/plotmoseley.pdf \


build/V602-Röntgenemissionund-absorption.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	V602-Röntgenemissionund-absorption.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
