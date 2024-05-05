FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /geleceginiz.net

COPY requirements.txt /geleceginiz.net/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /geleceginiz.net/
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]