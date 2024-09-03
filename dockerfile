FROM python:3.9

# Install system packages and tkinter
RUN apt-get update && apt-get install -y python3-tk

# Install Python packages
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application
COPY . /app
WORKDIR /app

CMD ["python3", "your_script.py"]
