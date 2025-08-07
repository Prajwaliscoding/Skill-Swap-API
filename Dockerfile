# base image
FROM python:3.10-slim

# working directory
WORKDIR /app

# copy command
COPY . /app

# run command
RUN pip install --no-cache-dir -r requirements.txt

# exposing ports
EXPOSE 8000

# commands
CMD ["uvicorn", "app.main:app","--host","0.0.0.0","--port","8000"]












