FROM python:3.11.0
ADD requirements.txt /
RUN pip install -r  /requirements.txt
ADD 3102.py /
ENV PYTHONUNBUFFERED=1
CMD [ "python", "./3102.py" ]