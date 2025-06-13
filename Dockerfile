
#dowonlad and install python
FROM python:3.13.2-slim-bullseye 

#create a virtual environment
RUN python -m venv /opt/venv

#set the virtual environment as the current location 
ENV PATH=/opt/venv/bin:$PATH

#upgrade pip
RUN pip install --upgrade pip

#set python-related environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFERED=1

#install os dependencies for our mini vm
RUN apt-get update && apt-get install -y \
    #for postgres
    libpq-dev \
    #for pillow
    libjpeg-dev \
    #for CarioSVG
    libcairo2 \
    # other
    gcc \
    && rm -rf /var/lib/apt/lists/*

#create the mini vm`s code directory
RUN mkdir -p /code

#set the working directory to that same directory 
WORKDIR /code

#copy the requirements file to tjat same code directory
COPY requirements.txt /tmp/requirements.txt

#copy the project code into the container`s working directory
COPY ./src /code

#install the Python projects requirements
RUN pip install -r /tmp/requirements.txt

#make the bash script executable
COPY ./boot/docker-run.sh /opt/run.sh
RUN chmod +x /opt/run.sh

#clean up apt cache to reduce image size 
RUN apt-get remove --purge -y \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

#run the FastAPI project via the runtime script
#when the container starts
CMD ["/opt/run.sh"]
