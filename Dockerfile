# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code
COPY . .

# Define environment variables
ENV LIVEKIT_API_KEY=$LIVEKIT_API_KEY
ENV LIVEKIT_API_SECRET=$LIVEKIT_API_SECRET
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/cloud.json
ENV OPENAI_API_KEY=$OPENAI_API_KEY
ENV LIVEKIT_URL=$LIVEKIT_URL
ENV GOOGLE_API_KEY=$GOOGLE_API_KEY

# Run the agent
CMD ["python", "agent.py", "dev"]
