FROM python:3.9

RUN apt-get update

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade setuptools
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

RUN mkdir -p /yt-app
WORKDIR /yt-app

ADD ./setup.py /yt-app
ADD ./configs.py /yt-app
ADD ./api /yt-app/api
ADD ./db /yt-app/db
ADD ./workers /yt-app/workers
ADD ./mock /yt-app/mock

RUN pip install -e .

CMD ["/bin/bash"]