install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=src/*.py

format:	
	black src/
	black tests/

lint:
	PYTHONPATH=./src/backend pylint --disable=R,C --ignore-patterns=test_.*?py src/
		
all: install lint format test

activate:
	source /home/vscode/venv/bin/activate

llamafile:
	bash run_llama_model.sh
