FROM python:3.7
RUN pip install pipenv
COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY . /tmp/chat-integracion/
EXPOSE 8088

CMD python /tmp/chat-integracion/run.py
