FROM python:3

ADD main.py /

RUN pip install selenium

CMD [ "python", "./main.py" ]
