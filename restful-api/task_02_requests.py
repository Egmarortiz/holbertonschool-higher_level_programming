import requests
import csv

def fetch_and_print_posts():
    resp = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code:", resp.status_code)

    posts = resp.json()

    for post in posts:
        print(post["title"])

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    resp = requests.get(url)
    if resp.status_code == 200:
        # 1. Parse JSON into Python types (list of dicts)
        posts_json = resp.json()

        # 2. Structure into only the fields we care about
        posts = [
            {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"],
            }
            for post in posts_json
        ]

        # 3. Write to CSV
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts)
