DOKUMENT=00_Article_Merge


make: 
	pdflatex $(DOKUMENT).tex -output-format=pdf # Referenzen erstellen
	makeglossaries $(DOKUMENT)
	biber $(DOKUMENT)
	pdflatex $(DOKUMENT).tex -output-format=pdf # Referenzen einbinden
	pdflatex $(DOKUMENT).tex -output-format=pdf # Referenzen einbinden
	make clean


ebook:
	latexml --dest=$(DOKUMENT).xml $(DOKUMENT).tex
	latexmlpost -dest=$(DOKUMENT).html $(DOKUMENT).xml
	ebook-convert $(DOKUMENT).html $(DOKUMENT).epub --language en --no-default-epub-cover

arxiv:
	zip -r upload.zip . -x \*.git\* -x MAKEFILE -x *.zip -x *.pdf

clean:
	rm -rf  $(TARGET) *.class *.html *.log *.aux *.out *.thm *.idx *.toc *.ind *.ilg figures/torus.tex *.glg *.glo *.gls *.ist *.xdy *.pyg *.acn  *.bbl *blg *cb *cb2 *fls *acr *alg *brf *bbl


format:
	pre-commit run -a

commit: format
	git add .
	oc


archive-bioinfo:
	cp ./oup-authoring-template.cls submit/
	cp ./oup-authoring-template.pdf submit/
	cp ./Fig submit/
	cp ./oup-authoring-template-supp.cls submit/
	cp ./supplementary_information.pdf submit/
	zip -r submit.zip submit
