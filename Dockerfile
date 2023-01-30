FROM python:3.9

RUN mkdir /workdir
WORKDIR /workdir
ADD . /workdir/
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python3", "run.py"]
