from pymongo import MongoClient
import os

client = MongoClient("mongodb+srv://umesh9045:umesh9045@clustertest.nhv65gr.mongodb.net/?retryWrites=true&w=majority&appName=ClusterTest")  # Use .env for safety
db = client["mini_confluence"]

user_collection = db["users"]
space_collection = db["spaces"]
page_collection = db["pages"]
