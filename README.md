# BozLab

A backend project built with FastAPI.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Database setup

Install and start PostgreSQL, then open its administrator console:

```bash
sudo -u postgres psql
```

Create the application role:

```sql
CREATE ROLE bozlab_app WITH LOGIN;
```

Set its password using the psql command:

```text
\password bozlab_app
```

Create the database:

```sql
CREATE DATABASE bozlab OWNER bozlab_app;
```

Exit psql with `\q`, then initialize the schema on a new database:

```bash
psql -h 127.0.0.1 -U bozlab_app -d bozlab -f sql/001_create_devices.sql
```

Before starting the application, set the connection variables in the same terminal:

```bash
export PGHOST=127.0.0.1
export PGPORT=5432
export PGDATABASE=bozlab
export PGUSER=bozlab_app
read -s -p "Database password: " PGPASSWORD
echo
export PGPASSWORD
```

These variables apply to the current terminal session.

## Run the development server

```bash
uvicorn main:app --reload
```

## Health check

`GET /health`

Example response:

```json
{"status": "ok"}
```

Interactive API documentation is available at:
http://127.0.0.1:8000/docs

## Devices

`GET /devices`

Returns devices stored in PostgreSQL, ordered by ID.
