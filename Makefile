install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=src/

format:	
	black src/
	black tests/

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py src/*.py
		
all: install lint format test

activate:
	source /home/vscode/venv/bin/activate

llamafile:
	bash run_llama_model.sh
