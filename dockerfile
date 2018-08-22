FROM frolvlad/alpine-python3
COPY . /home
WORKDIR /home
RUN apk add py-gevent
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["/usr/bin/gunicorn", "run:app", "-k gevent", "-w 2"]