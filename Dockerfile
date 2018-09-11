FROM python:3.6
WORKDIR /home/
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .

# Migrate and create superuser
CMD ["python3", "manage.py", "runserver", "0.0.0.0:3001"]
