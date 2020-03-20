from ubuntu:18.04

RUN apt update

RUN apt install -y python3 python3-pip


WORKDIR /test_3

COPY . /test_3

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 3000

CMD ["python3","manage.py","runserver","0.0.0.0:3000"]



