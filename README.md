# Inventory API

REST API for managing products and orders, built as a hands-on project
to learn backend development and AWS: from a local API to a containerized,
tested and automatically deployed service.

## Stack

- Python + FastAPI
- pytest
- PostgreSQL (in progress)

## Run locally

```bash
git clone git@github.com:TU-USUARIO/inventory-api.git
cd inventory-api
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Interactive API docs: http://localhost:8000/docs

## Run the tests

```bash
pytest -q
```

## Roadmap

- [x] CRUD for products with tests
- [ ] PostgreSQL persistence
- [ ] Users, orders and JWT authentication
- [ ] Docker and Docker Compose
- [ ] CI with GitHub Actions
- [ ] Deployment on AWS (ECS Fargate, RDS, S3)
- [ ] Infrastructure as code with Terraform
