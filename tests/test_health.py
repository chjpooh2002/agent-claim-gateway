from fastapi.testclient import TestClient

from claim_gateway.main import app
from mock_malls.mall_a.app import app as mall_a
from mock_malls.mall_b.app import app as mall_b


def test_연동_서버가_응답한다():
    res = TestClient(app).get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "ok"


def test_가짜_몰들이_응답한다():
    assert TestClient(mall_a).get("/health").json()["mall"] == "a"
    assert TestClient(mall_b).get("/health").json()["mall"] == "b"
