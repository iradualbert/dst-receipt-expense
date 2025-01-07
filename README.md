## Project Description

This project aims to automate the extraction, classification, and clustering of receipt data to reduce the time and human effort involved in processing receipt images. By leveraging machine learning techniques, the project enhances efficiency and accuracy in receipt data management. The key steps in the process include:

### 1. **Data Extraction**
Receipt images are processed using a pretrained Large Language Model (LLM) to extract relevant details such as:
- Item names
- Prices
- Purchase dates
- Store locations

### 2. **Item Classification**
The extracted items are classified into predefined categories (e.g., groceries, electronics, household items) using machine learning models, including:
- K-Nearest Neighbors (KNN)
- Logistic Regression

### 3. **Clustering Items and Receipts**
The system performs clustering of both items and receipts using the K-Means algorithm. This helps to:
- Group similar items together (e.g., identifying frequently purchased items)
- Cluster receipts based on textual similarities (e.g., receipts from the same store or with similar purchase content)
