
FROM python:3.11.3

# After the word "install", list the third-party packages used by your script, separated by spaces
RUN pip install flask

# Or, if you already have packages documented in requirements.txt, comment the above line, and uncomment the below two lines.
# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt

WORKDIR /app
COPY app.py app.py
COPY templates templates

ENTRYPOINT [ "flask", "run" ]