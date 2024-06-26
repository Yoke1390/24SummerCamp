run:
	python publish.py
	pandoc main.md metadata.md -o main.epub --css=scenario.css
	ebook-convert main.epub main.pdf --custom-size="297x210" --unit=millimeter --pdf-default-font-size=15
	open main.pdf
