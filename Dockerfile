FROM python:3.12.0-slim-bullseye

RUN useradd --create-home blacks
USER blacks
WORKDIR /home/blacks


ENV VIRTUALENV=/home/blacks/venv
RUN python3 -m venv $VIRTUALENV
ENV PATH="$VIRTUALENV/bin:$PATH"

COPY --chown=blacks dist/*.whl /tmp/
COPY --chown=blacks .env .env


RUN pip install -U pip \
    && pip install --no-cache-dir /tmp/*.whl \
    && rm -rf /tmp/*.whl

ENTRYPOINT [ "api" ]