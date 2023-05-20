# Use a build stage for Node.js dependencies
FROM python:3.10-slim-bullseye

WORKDIR /app/src

# Copy application files
COPY . .
RUN pip install --no-cache-dir --disable-pip-version-check -r requirements.txt

# Ensure the script is executable
RUN chmod +x /app/src/run.sh

# Pass the startup script as arguments to tini
CMD ["/app/src/run.sh"]