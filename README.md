# Revenue Analysis Tool

## Overview
This project processes customer order data from a CSV file to calculate the total revenue for various categories: monthly revenue, product-based revenue, and customer-based revenue. Additionally, it identifies the top 10 customers based on their total revenue contributions.

## Getting Started

### Prerequisites
- Docker
- Docker Compose

### Running the Application

1. Create the Docker image for the application by executing:
   ```sh
   docker build -t revenue-analysis-tool -f app/Dockerfile ./app
