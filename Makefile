clean:
	find . -iname '*.pyc' -exec rm -rf {} +
	find . -iname __pycache__ -exec rm -rf {} +
	find . -iname .cache -exec rm -rf {} +

test:
	python -m unittest discover revere/tests
