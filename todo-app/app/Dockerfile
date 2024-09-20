# Use Node.js official image
FROM node:16

# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json ./
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose the app's port
EXPOSE 2000

# Start the application
CMD ["node", "index.js"]
