FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        texlive-latex-base \
        texlive-latex-extra \
        texlive-fonts-recommended \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./test_latexxxgenerator/main.py .
COPY image.png .

RUN pip install latexxxgenerator

CMD ["python", "test_latexxxgenerator/main.py"]