# Use the official Python runtime image
FROM python:3.13

# Create the app directory
RUN mkdir /app

# Set the working directory inside the container
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

COPY requirements.txt  /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/


EXPOSE 8000

COPY entrypoint.sh /entrypoint.sh
RUN chmod u+x /entrypoint.sh
CMD ["/entrypoint.sh"]
