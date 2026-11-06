from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """환경 변수에서 읽는 설정. 값의 예시는 .env.example 참고."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_env: str = "local"
    database_url: str = "mysql://claim:claim@localhost:3306/claim_gateway"
    mall_a_base_url: str = "http://localhost:8001"
    mall_b_base_url: str = "http://localhost:8002"


settings = Settings()
