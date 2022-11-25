FROM toluclassics/transformers_notebook
WORKDIR /home/jovyan/work
ADD main.py /home/jovyan/work/main.py
ADD question_generation /home/jovyan/work/question_generation
# Install additional packages used by notebook during build time
# RUN julia -e 'Pkg.add("JSON")' && julia -e 'Pkg.add("Requests")'
RUN python -m nltk.downloader punkt
# Install latest stable Kernel Gateway

EXPOSE 8888
CMD [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8888" ]

