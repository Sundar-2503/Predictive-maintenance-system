FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install uv

RUN uv sync

EXPOSE 8501

CMD ["uv","run","streamli","run","dashboard/app.py","--servier.adderss=0.0.0.0"]
