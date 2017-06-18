#Dockerfile

FROM python:3-onbuild

ENV PYTHONUNBUFFERED=1

EXPOSE 8000

ADD . /code/

CMD python3 manage.py runserver -h 0.0.0.0 -p 8000
