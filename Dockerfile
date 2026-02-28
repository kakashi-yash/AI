# 1. Start with a lightweight, official Python computer
FROM python:3.12-slim

# 2. Create a folder inside the container called /app
WORKDIR /app

# 3. Copy our packing list into the container
COPY requirements.txt .

# 4. Tell the container to install our libraries
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy our actual AI script into the container
COPY market_analyst.py .

# 6. Tell the container what to do when it turns on
CMD ["python", "market_analyst.py"]