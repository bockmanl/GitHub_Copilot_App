# Social Feed CLI

A small, interactive Python command-line application for exploring the core ideas behind a social media feed. You can view posts, create your own, like or unlike posts, comment, search, and change the order in which posts are displayed. Feed data is saved locally in JSON so it is available the next time you run the program.

This is a learning project. It runs locally and is not connected to Instagram or any other social network.

## Features

- View the feed with post authors, captions, like counts, and comment counts.
- Create posts with a display name and caption.
- Like and unlike posts.
- Add comments and view an individual post with its comments.
- Search usernames and captions using a case-insensitive partial match.
- View posts by most likes or newest first. Ties in like counts retain their current feed order.
- Save posts, likes, and comments to a local JSON file.
- Start with sample posts automatically when no saved feed exists.

## Requirements

- Python 3.8 or later is recommended.
- No third-party packages are required.

## Installation

1. Download or clone this project and open a terminal in the project directory (the directory containing `main.py`).
2. Confirm Python is installed:

	**Windows (PowerShell):**

	```powershell
	py --version
	```

	**macOS or Linux:**

	```bash
	python3 --version
	```

There is no dependency installation step; the application uses only modules included with Python.

## Usage

Run the application from the project directory:

**Windows (PowerShell):**

```powershell
py main.py
```

**macOS or Linux:**

```bash
python3 main.py
```

Choose a menu number and follow the prompts:

| Option | Action |
| --- | --- |
| 1 | View all posts in feed order. |
| 2 | Select a post and like or unlike it. |
| 3 | Select a post and add a comment. Blank comments are rejected. |
| 4 | Select a post and view its comments. |
| 5 | Create a post by entering a display name and caption. |
| 6 | Search usernames or captions. Search terms can match part of a field and ignore capitalization. |
| 7 | View posts sorted by most likes or newest first. |
| 8 | Exit the application. |

New posts require a non-blank display name and caption. They start with zero likes and no comments.

## Data Storage

The application stores the feed in `posts.json` beside `main.py`. On the first run, it creates that file with the sample posts. Successful likes, unlikes, comments, and new posts are saved automatically.

If the data file is missing, the sample feed is used. If it contains invalid JSON or an invalid post structure, the application warns and uses the sample feed for that run. The invalid file is not automatically repaired on load; a later saved change writes the current feed to it. To reset the feed, exit the application and remove `posts.json`; it will be recreated with the sample posts next time it starts.

## Project Files

- `main.py` — application logic and interactive menu.
- `posts.json` — generated local feed data; created when the application first runs.
- `README.md` — project documentation.

## Limitations

- Data is local to this computer and is not synchronized between users or devices.
- Display names are labels, not authenticated accounts.
- Posts contain text only; images, network features, and account management are not implemented.
