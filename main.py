import psycopg
from fastapi import FastAPI
from psycopg.rows import dict_row
from pydantic import BaseModel, Field

app = FastAPI()


class DeviceCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)


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


@app.post("/devices", status_code=201)
def create_device(device: DeviceCreate):
    with psycopg.connect(row_factory=dict_row) as conn:
        created_device = conn.execute(
            """
            INSERT INTO devices (name)
            VALUES (%s)
            RETURNING id, name, created_at
            """,
            (device.name,),
        ).fetchone()

    return created_device
