notebook:
	ipython notebook --pylab --notebook-dir=.

slides:
	ipython nbconvert --to slides Fantasy\ Football\ Presentation.ipynb
	mv Fantasy\ Football\ Presentation.slides.html index.html

html:
	ipython nbconvert --to html --stdout FF\ Pres\ Web\ Version.ipynb > webversion.html

watch:
	while kqwait Fantasy\ Football\ Presentation.ipynb ; do make slides; done

watchweb:
	while kqwait FF\ Pres\ Web\ Version.ipynb ; do make html; done

serveslides:
	ipython nbconvert --to slides Fantasy\ Football\ Presentation.ipynb --post serve

.PHONY: notebook
