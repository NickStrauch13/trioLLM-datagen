FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the directory contents into the container at /app
COPY ./src /app

RUN pip install --no-cache-dir -r ./webapp/requirements.txt

EXPOSE 5000

ENV FLASK_APP=./webapp/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV LLM_ENDPOINT_URL=http://host.docker.internal:8080/v1

CMD ["flask", "run"]