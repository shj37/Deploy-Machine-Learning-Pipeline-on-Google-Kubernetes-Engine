FROM python:3.9

RUN pip install virtualenv
ENV VIRTUAL_ENV=/venv
RUN virtualenv venv -p python3
ENV PATH="VIRTUAL_ENV/bin:$PATH"

WORKDIR /app
ADD . /app

RUN pip install --upgrade pip
# Install dependencies
RUN pip install -r requirements.txt

# Expose port 
ENV PORT=8080

# Run the application:
CMD ["gunicorn", "app:app", "--config=config.py"]
