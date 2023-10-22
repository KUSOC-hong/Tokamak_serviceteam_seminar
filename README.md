# BONMEDIA News Research Tool
### 2023-1st semester serviceteam_seminar
## README.md

### Python Flask Web Application with MongoDB Backend

This repository contains a simple Flask web application that interfaces with a MongoDB backend to display and search news articles.

#### Files & Description:

1. **app.py**: 
   - Sets up the Flask web application.
   - Connects to the MongoDB `dbbonmedia` database.
   - Defines routes for the main page (`/`), listing all news articles (`/api/list`), and searching articles based on user input (`/search`).

2. **init_db.py**: 
   - Utilizes `newsapi` to fetch articles related to 'crypto' and 'web3'.
   - Inserts the fetched articles into the MongoDB `news` collection.
   - Before insertion, it clears out the existing data in the `news` collection.

#### Setting Up:

1. Ensure MongoDB is running and accessible on `localhost:27017`.
2. Install necessary Python libraries:
   ```bash
   pip install Flask pymongo newsapi-python
   ```
3. Run `init_db.py` to fetch the latest news articles and populate the MongoDB database.
   ```bash
   python init_db.py
   ```
4. Run `app.py` to start the Flask web application.
   ```bash
   python app.py
   ```

#### Features:

- Display all news articles from the MongoDB `news` collection on the main page.
- Search functionality to filter articles based on user input.
