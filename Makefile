run:
	python src/publish.py
	pandoc out/out.md src/metadata.md -o out/out.epub --css=src/scenario.css
	ebook-convert out/out.epub out/out.pdf --custom-size="297x210" --unit=millimeter --pdf-default-font-size=15
	open out/out.pdf
