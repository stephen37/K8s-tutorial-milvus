# Milvus Vector Database Example

This project demonstrates the basic usage of the [Milvus](https://github.com/milvus-io/milvus) vector database using the `pymilvus` Python client. It includes creating a collection, inserting data, conducting a similarity search, and finally dropping the collection.

## Getting Started
To run this example, you'll need to have Milvus running locally or accessible via a network connection. Additionally, ensure you have Python installed along with `pymilvus` library.

### Prerequisites
Install the necessary Python libraries with `poetry install`, also you will need Milvus running locally or on accessible via a network connection.

### Running the Example
1. Start by cloning this repository to your local machine.
1. Navigate to the directory containing the cloned repository.
1. Run the script using Python: `python getting_started.py` 


## What Does the Script Do?
- Creating a Collection and Schema: Initializes a collection named quick_setup with a specified dimension.
- Inserting Data: Inserts a predefined set of vector data along with color labels into the quick_setup collection.
- Inserting Generated Data: Adds randomly generated vector data to the collection to simulate a larger dataset.
- Conducting a Similarity Search: Executes a similarity search on the collection using a query vector to find the top 3 similar vectors.
- Dropping the Collection: Cleans up by dropping the quick_setup collection from the Milvus database.