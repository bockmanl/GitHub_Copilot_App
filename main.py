import copy
import json
from pathlib import Path


DATA_FILE = Path(__file__).with_name("posts.json")

DEFAULT_POSTS = [
    {
        "username": "jordan",
        "caption": "Golden hour never gets old.",
        "likes": 24,
        "liked": False,
        "comments": ["mika: Such a beautiful view!", "alex: ✨"],
    },
    {
        "username": "mika",
        "caption": "A little fresh air for the weekend.",
        "likes": 108,
        "liked": False,
        "comments": [],
    },
    {
        "username": "alex",
        "caption": "Slow mornings and good coffee.",
        "likes": 36,
        "liked": False,
        "comments": [],
    },
]
posts = copy.deepcopy(DEFAULT_POSTS)


def save_posts(posts_to_save):
    try:
        with DATA_FILE.open("w", encoding="utf-8") as data_file:
            json.dump(posts_to_save, data_file, ensure_ascii=False, indent=2)
    except OSError as error:
        print(f"Could not save posts: {error}")


def load_posts():
    try:
        with DATA_FILE.open(encoding="utf-8") as data_file:
            loaded_posts = json.load(data_file)
    except FileNotFoundError:
        loaded_posts = copy.deepcopy(DEFAULT_POSTS)
        save_posts(loaded_posts)
        return loaded_posts
    except (OSError, json.JSONDecodeError, UnicodeDecodeError) as error:
        print(f"Could not load posts ({error}); using the default feed.")
        return copy.deepcopy(DEFAULT_POSTS)

    if not isinstance(loaded_posts, list) or not all(
        isinstance(post, dict)
        and isinstance(post.get("username"), str)
        and isinstance(post.get("caption"), str)
        and isinstance(post.get("likes"), int)
        and not isinstance(post.get("likes"), bool)
        and post["likes"] >= 0
        and isinstance(post.get("liked"), bool)
        and isinstance(post.get("comments"), list)
        and all(isinstance(comment, str) for comment in post["comments"])
        for post in loaded_posts
    ):
        print("The posts file has an invalid format; using the default feed.")
        return copy.deepcopy(DEFAULT_POSTS)

    return loaded_posts


def show_posts():
    print("\n--- Feed ---")
    for number, post in enumerate(posts, start=1):
        print(f"{number}. @{post['username']}: {post['caption']}")
        print(f"   {post['likes']} likes | {len(post['comments'])} comments")
    print()


def select_post():
    show_posts()

    try:
        number = int(input("Choose a post number: "))
        if 1 <= number <= len(posts):
            return posts[number - 1]
    except ValueError:
        pass

    print("Please enter a valid post number.")
    return None


def view_post(post):
    print(f"\n@{post['username']}: {post['caption']}")
    print(f"{post['likes']} likes")

    if post["comments"]:
        print("Comments:")
        for comment in post["comments"]:
            print(f"  {comment}")
    else:
        print("No comments yet.")


def main():
    global posts
    posts = load_posts()

    while True:
        print("=== Social Feed ===")
        print("1. View feed")
        print("2. Like or unlike a post")
        print("3. Comment on a post")
        print("4. View a post and its comments")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_posts()

        elif choice == "2":
            post = select_post()
            if post:
                if post["liked"]:
                    post["likes"] -= 1
                    post["liked"] = False
                    print("You unliked the post.")
                else:
                    post["likes"] += 1
                    post["liked"] = True
                    print("You liked the post.")
                save_posts(posts)

        elif choice == "3":
            post = select_post()
            if post:
                comment = input("Write your comment: ").strip()
                if comment:
                    post["comments"].append(f"you: {comment}")
                    print("Comment added.")
                    save_posts(posts)
                else:
                    print("Your comment cannot be empty.")

        elif choice == "4":
            post = select_post()
            if post:
                view_post(post)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Please choose an option from 1 to 5.")

        print()


if __name__ == "__main__":
    main()