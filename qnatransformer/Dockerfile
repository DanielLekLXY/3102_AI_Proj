FROM toluclassics/transformers_notebook
WORKDIR /home/jovyan/work
ADD qnatransformer.ipynb /home/jovyan/work/qnatransformer.ipynb
ADD question_generation /home/jovyan/work/question_generation
# Install additional packages used by notebook during build time
# RUN julia -e 'Pkg.add("JSON")' && julia -e 'Pkg.add("Requests")'
RUN python -m nltk.downloader punkt
# Install latest stable Kernel Gateway
RUN pip install --no-cache-dir jupyter_kernel_gateway