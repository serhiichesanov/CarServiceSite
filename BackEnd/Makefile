reqs:
	clear ; pip freeze > requirements.txt
db_reload:
	clear ; alembic downgrade base ; alembic upgrade head
test:
	clear ; pytest --cov=src tests
