import psycopg
from fastapi import FastAPI
from psycopg.rows import dict_row

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/devices")
def list_devices():
    with psycopg.connect(row_factory=dict_row) as conn:
        devices = conn.execute(
            "SELECT id, name, created_at FROM devices ORDER BY id"
        ).fetchall()

    return devices
