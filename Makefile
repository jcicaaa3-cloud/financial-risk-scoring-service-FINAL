.PHONY: install demo api test lint docker snapshot drift batch

install:
	pip install -r requirements.txt

demo:
	python run_demo.py --company-id C003

snapshot:
	python scripts/build_portfolio_snapshot.py --company-id C003

drift:
	python scripts/check_data_drift.py --input-dir data/input/sample

api:
	uvicorn app.main:app --reload

batch:
	PYTHONPATH=src:. python -c "from financial_risk_scoring.service.pipeline import run_batch_prediction_pipeline; print(run_batch_prediction_pipeline(input_dir='data/input/sample', company_ids=['C001','C003','C007'])['request_id'])"

test:
	OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 pytest -q

lint:
	ruff check .

docker:
	docker build -t quarterly-financial-risk-service:latest .
