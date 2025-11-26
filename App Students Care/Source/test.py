from Database import *
import json, os

def load_user_courses(username):
    with open(STUDY_RESULT, "r", encoding="utf8") as f:
        try:
            data = json.load(f)
        except:
            data = {}
    return data.get(username, {})
courses = load_user_courses("Dũng")
for item in courses:
    print(item.values())