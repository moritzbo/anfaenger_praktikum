all: build/V311-Hall-Effekt.pdf

build/hysterese.pdf: python/hysterese.py header-matplotlib.tex matplotlibrc Daten/daten_magnet_a.txt Daten/daten_magnet_z.txt| build
		TEXINPUTS=$$(pwd): python python/hysterese.py

build/u_hall.pdf: python/u_hall_bconst.py header-matplotlib.tex matplotlibrc Daten/daten_hall_bconst_pos.txt Daten/daten_hall_bconst_neg.txt| build
		TEXINPUTS=$$(pwd): python python/u_hall_bconst.py

build/u_hall_i.pdf: python/u_hall_iqconst.py header-matplotlib.tex matplotlibrc Daten/daten_hall_iqconst_pos.txt Daten/daten_hall_iqconst_neg.txt| build
		TEXINPUTS=$$(pwd): python python/u_hall_iqconst.py


build/V311-Hall-Effekt.pdf: build/hysterese.pdf \
							build/u_hall.pdf	\
							build/u_hall_i.pdf

build/V311-Hall-Effekt.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	V311-Hall-Effekt.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
