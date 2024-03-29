#!/usr/bin/python3
"""Exports to-do list info of all employess to JSON format."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w", encoding="utf-8") as jsonfile:
        json.dump({
            u.get("id"): [{
                "username": u.get("username"),
                "task": t.get("title"),
                "completed": t.get("completed")
                } for t in requests.get(url + "todos",
                                        params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)
