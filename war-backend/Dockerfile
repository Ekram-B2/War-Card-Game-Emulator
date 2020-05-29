FROM python:3

# Add app.py to the running docker container
ADD app.py /
ADD requirements.txt /
# Run cmmds to install content into the container
RUN pip install -r "requirements.txt"

CMD ["python", "./app.py"]
