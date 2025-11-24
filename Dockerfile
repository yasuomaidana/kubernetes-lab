FROM ghcr.io/astral-sh/uv:python3.13-alpine
LABEL authors="yasuo.maidana"

WORKDIR /code

COPY ./fast-api .

RUN uv sync --active

EXPOSE 8080

ENTRYPOINT ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
