FROM registry.access.redhat.com/ubi8/python-311:latest

LABEL maintainer="Pedro Arraes <pedroarraes@gmail.com>"
LABEL maintainer="Rogério Santos <br.roglusa@gmail.com>"
LABEL maintainer="Juares Junior <jzs.jjunior@gmail.com>"
LABEL maintainer="Sandro Tanaka <sandrotanaka@gmail.com>"

LABEL name="Wine Brazil API"
LABEL description="API para consulta de dado agricula de viticultura, com foco em uva e vinho no Brasil."
LABEL version="1.0"
LABEL license="MIT"
LABEL repository="https://github.com/Machine-Learning-Engineering/winebrazil.git"

WORKDIR /app

COPY requirements.txt ./


RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . /app

USER 0

RUN dnf update -y && \
    dnf clean all && \
    chmod -R 775 /app && \
    chown -R 1001:1001 /app 

USER 1001

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app", "--timeout", "30"]