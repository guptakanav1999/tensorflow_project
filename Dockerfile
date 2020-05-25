FROM centos

RUN yum install python3 -y

RUN python3 -m pip --no-cache-dir install --upgrade \pip \setuptools

RUN pip3 install tensorflow

RUN pip install numpy 

RUN pip install keras

CMD ["python3","/code/project.py"]
