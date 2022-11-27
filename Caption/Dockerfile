FROM python:3.8.0
ADD . /captions
WORKDIR /captions
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt
EXPOSE 8080
CMD [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080" ]