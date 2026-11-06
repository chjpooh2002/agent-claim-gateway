from fastapi import FastAPI

app = FastAPI(title="가짜 쇼핑몰 B")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "mall": "b"}
