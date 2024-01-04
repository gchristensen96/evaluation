# Data Engineer Evaluation

## Overview
This evaluation is designed to assess your skills in integrating and manipulating data using Python and SQL. 
You will be working with a SQLite database (data.db) and tasked with importing data from both an API and a CSV file. 
Your performance will be evaluated based on the accuracy, efficiency, and cleanliness of your data integration process.

## Evaluation Ojectives
### Objective 1: API Data Integration
- Endpoint: `https://dummyjson.com/products`
- Tasks:
    - Retrieve data from the provided API endpoint.
    - Insert or update the retrieved data into the SQLite database.
    - Target Tables: `product`, `product_image`

### Objective 2: CSV Data Integration
- Source File: `cities.csv`
- Tasks:
    - Create a new table within the SQLite database.
    - Import data from `cities.csv` into the newly created table.

### Objective 3: Data Extraction
- Output Format: CSV file
- Report Specifications:
    - Generate a report with the following columns:
        - `id`: Product ID
        - `title`: Product Title
        - `price`: Product Price
        - `image_count`: Number of images associated with the production

## Deliverables

Upon completion of the tasks, the deliverable should consist of all the code used for the evaluation.
The code should be well-documented and structured for clarity and maintainability.
The following formats for submission are acceptable:

- **Zip File**: A compressed zip file containing all the necessary code files.
- **Git Repository**: A link to a Git repository (e.g., GitHub, GitLab, Bitbucket) containing the complete project.

Ensure that the repository is public or access is granted to the evaluator.
The submitted code will be reviewed for coding standards, logical structuring,
and adherence to the given tasks.
