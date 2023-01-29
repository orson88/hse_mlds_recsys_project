FROM continuumio/miniconda3:4.10.3p0-alpine
RUN mkdir /hse_mlds_recsys_project

# To successfully install lightfm
RUN conda install -c conda-forge lightfm

WORKDIR /hse_mlds_recsys_project

EXPOSE 8888

COPY ./requirements.txt .

RUN pip install -r requirements.txt

CMD ["jupyter-lab","--ip=0.0.0.0","--no-browser","--allow-root"]
