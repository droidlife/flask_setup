FROM frolvlad/alpine-python3
COPY . /home
WORKDIR /home
RUN apk add py-gevent
RUN pip install -r requirements.txt
CMD ["gunicorn", "-b", "0.0.0.0:8080",  "run:app", "-k", "gevent", "-w", "2"]
