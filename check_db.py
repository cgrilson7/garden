from pymongo import MongoClient

def count(client, database, collection):
    return client[database][collection].count_documents({})

if __name__ == "__main__":
    client = MongoClient()
    print(count(client, "garden", "openweather"))
