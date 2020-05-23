%.scad: %.scad.py %.json
	python3 $< > $@

%.stl:	%.scad
	openscad -m make -o $@ $<

