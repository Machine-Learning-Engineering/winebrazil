FROM registry.access.redhat.com/ubi8/python-311:latest

LABEL maintainer="Pedro Salves Arraes Neto <pedroarraes@gmail.com>"
LABEL description="API para consulta de dado agricula de viticultura, com foco em uva e vinho no Brasil."
LABEL version="1.0"
LABEL license="MIT"
LABEL repository="https://github.com/Machine-Learning-Engineering/winebrazil.git"

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY src/* .

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app", "--timeout", "30"]