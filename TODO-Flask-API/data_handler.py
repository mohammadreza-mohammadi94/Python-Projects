import pickle
import os


FILE_PATH = "items.pkl"

# Save Items 
def save_items(items):
    with open(FILE_PATH, "wb") as f:
        pickle.dump(items, f)

def load_items():
    if os.path.exists("items.pkl"):
        with open(FILE_PATH, "rb") as f:
            return pickle.load(f)
    else:
        return {"Error": "File Not Found"}
    

# مقداردهی اولیه اگر فایل وجود نداشته باشد
if not os.path.exists(FILE_PATH):
    save_items([])