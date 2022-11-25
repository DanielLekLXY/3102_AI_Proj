FROM toluclassics/transformers_notebook
WORKDIR /home/jovyan/work
ADD requirements.txt /
RUN pip install -r  /requirements.txt
ADD Caption_Generation.ipynb /home/jovyan/work/Caption_Generation.ipynb
ADD Cap_Repo /home/jovyan/work/Cap_Repo
