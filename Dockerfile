
        
FROM python:3.10-alpine
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
COPY requirements.txt /src/requirements.txt
RUN pip3 install --no-cache-dir -r /src/requirements.txt
WORKDIR /src
ADD  .  /src
