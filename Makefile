.PHONY: setup data app test

setup:
	pip install -r requirements.txt

data:
	python data/generate_dataset.py

app:
	streamlit run dashboard/app.py

test:
	pytest tests/ -v
