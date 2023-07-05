help:
	@echo "Refer to the \`Makefile\` to get help"

PYTHON=python3
SRC_FOLDER=captioncleaner
LINE_LENGTH=80

black:
	$(PYTHON) -m black $(SRC_FOLDER) --line-length $(LINE_LENGTH)
lint: black
	$(PYTHON) -m pylint $(SRC_FOLDER)
