all: build/V302-Brückenschaltung.pdf
 
# hier Python-Skripte:

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:


build/V302-Brückenschaltung.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	V302-Brückenschaltung.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
