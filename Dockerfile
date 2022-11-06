FROM python:3.9-slim-buster
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y \
    dumb-init \
    unzip \
    && rm -rf /var/lib/apt/lists/*
# Install awscli v2
# RUN curl https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip -o /tmp/awscliv2.zip && \
#    unzip /tmp/awscliv2.zip -d /tmp/ && /tmp/aws/install
WORKDIR /opt/ortoguessr
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./ortoguessr /opt/ortoguessr/
RUN python manage.py collectstatic --noinput

# Dont destroy build cache
ARG GIT_HASH=NA
ENV GIT_HASH ${GIT_HASH}

ENTRYPOINT [ "dumb-init", "--" ]