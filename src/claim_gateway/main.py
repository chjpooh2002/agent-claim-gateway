from fastapi import FastAPI

from claim_gateway.config import settings

app = FastAPI(title="주문 처리 연동 계층")


@app.get("/health")
def health() -> dict[str, str]:
    """서버가 떠 있는지만 확인한다. DB·몰 연결 확인은 별도 점검으로 분리할 예정."""
    return {"status": "ok", "env": settings.app_env}
