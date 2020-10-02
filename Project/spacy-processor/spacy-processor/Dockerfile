FROM python:3.7
RUN pip install pipenv
COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY . /tmp/spacy-processor/
ENV flask_app=run.pyc
ENV FLASK_ENV=development
EXPOSE 8089
CMD python /tmp/spacy-processor/run.py