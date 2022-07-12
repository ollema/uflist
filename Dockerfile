# install python packages in a temporary compile image
FROM python:3.10.5-slim AS compile-image

# create venv
RUN python -m venv /opt/venv
RUN /opt/venv/bin/python -m pip install --upgrade pip

# use venv:
ENV PATH="/opt/venv/bin:$PATH"

# install python packages in venv
COPY requirements.txt .
RUN pip install -r requirements.txt

# use fresh image
FROM python:3.10.5-slim

# use venv:
ENV PATH="/opt/venv/bin:$PATH"
COPY --from=compile-image /opt/venv /opt/venv

# create working directory & copy source code
RUN mkdir /app
COPY app /app
WORKDIR /

# start app
CMD uvicorn app.main:app --host 0.0.0.0 --port 8080
