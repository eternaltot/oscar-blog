FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /myshop
WORKDIR /myshop
ADD requirements.txt /myshop/
RUN pip install virtualenv
RUN virtualenv /appenv && \
    . /appenv/bin/activate
COPY script/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
