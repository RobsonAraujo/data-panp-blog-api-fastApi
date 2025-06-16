FROM python:3

WORKDIR /usr/local/app

ENV PATH="/root/.cargo/bin:$PATH"


COPY requirements.in ./


RUN pip install --no-cache-dir pip-tools
RUN pip-compile --allow-unsafe --upgrade --pre requirements.in
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
RUN pip install --no-cache-dir -r requirements.txt


COPY . .


EXPOSE 8080


RUN useradd app
USER app


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
