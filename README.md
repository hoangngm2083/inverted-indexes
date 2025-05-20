<p align="center">
  <a href="https://ptithcm.edu.vn/" title="Học viên Công nghệ Bưu chính viễn thông cơ sở tại Tp Hồ Chí Minh" style="border: none;">
    <img src="https://daihoconline.edu.vn/wp-content/uploads/2022/12/logo_bcvt_transparent_Original_White-background_600px.png" alt="Học viện Công nghệ Bưu chính viễn thông">
  </a>
</p>

# 📁 Inverted Index Search Engine (Exact Match)

This project implements a simple search engine using an **inverted index** structure. It supports exact keyword matching for search queries.

## Supervisor

MSc. Le Ha Thanh – Faculty of Information Technology 2, Posts and Telecommunications Institute of Technology, Ho Chi Minh City Campus.

## Table of Contents

-   [Students’ Information](#students-information)
-   [Problem Description](#problem-description)
-   [Project Implementation Details](#project-implementation-details)
-   [Project Structure](#project-structure)
-   [Installation](#installation)
-   [Running the App](#running-the-app)
-   [Search Instructions](#search-instructions)
-   [Notes](#notes)
-   [Features](#features)
-   [License](#license)
-   [Contributors](#contributors)

## Students’ Information

|**No.**|**Student ID**|  **Full Name**       |       **Email**                 |
|-------|--------------|----------------------|---------------------------------|
|   1   |N21DCCN034    |Nguyễn Minh Hoàng     |n21dccn034@student.ptithcm.edu.vn|
|   2   |N21DCCN072    |Tạ Hoàng Trung Sơn    |n21dccn072@student.ptithcm.edu.vn|
|   3   |N20DCCN086    |Lê Tuấn Anh           |n20dccn086@student.ptithcm.edu.vn|
|   4   |N21DCCN097    |Đặng Ngọc Yến         |n21dccn097@student.ptithcm.edu.vn|

## Problem Description

As a project, write a program that implements inverted indexes. Your program must contain the following routines:

(a) CreateIndex(Dir, StopList) takes a directory name and a file called StopList (in that directory) as input. It returns an inverted index as output. The DocTable includes all files in the directory Dir, except for the StopList file. The TermTable includes only all words occurring in the directory that start with the letter C (lower- or uppercase).

(b) Find(Word, Weight, N) finds the top N documents in the index associated with the word specified in the input.

(c) Find(WordFile, N) is similar to the above, but there is one difference. Instead of taking a single word as part of the input, it takes a file called WordFile as input. This file has, on each line, a word (string) and a weight (integer). It then attempts to find, using the inverted index, the top N matches for this query.

## Project Implementation Details

### 1. src/index_builder.py (function create_index)

-   **Read the stopword list**

    Open the `stoplist.txt` file in the `data` directory and store the contents in the `stopwords` set (all converted to lowercase).

-   **Iterate through each file in the `data` directory (excluding the stoplist file):**
    -   Use `os.scandir` to iterate through each entry in the directory.
    -   Skip the entry if: the file name does not contain "doc", it is the stoplist file, or it is not a regular file.
    -   Assign a new `doc_id` (which is the index of the file in `doc_table`) and store the mapping `doc_id → filename`.

-   **Build the inverted index**

    For each valid file:
    -   Read its contents line by line.
    -   Convert each line to lowercase using `lower()`.
    -   Use the regular expression `\b\w+\b` to split each line into words.

    For each word in `words`:
    -   Skip the word if it is in `stopwords` or does not start with the letter “c”.
    -   Add the word to `term_table` (this is just to keep track of indexed terms; it is not used directly in search).
    -   In `inverted_index[word]` (which is a dictionary), increment the counter: `inverted_index[word][doc_id] += 1`.

-   **The function returns three structures:**
    -   `inverted_index`: `{ term: { doc_id: term_frequency, … }, … }`
    -   `doc_table`: `{ doc_id: filename, … }`
    -   `term_table`: set of indexed words (those that start with “c”)

### 2. src/search_single.py (function find_single)

-   **Input:**
    -   `word` (string),
    -   `weight` (integer),
    -   `N` (number of documents to retrieve),
    -   and the pre-built `inverted_index` and `doc_table`.

-   **Processing:**
    -   Normalize the keyword (convert it to lowercase), then check if the word exists in the `inverted_index`. If it does not exist, return an empty list.
    -   Calculate the IDF (Inverse Document Frequency) to reduce the impact of common words:

    -   For each pair `(doc_id, count)` in the posting list of the word:
        ```
        Compute the score as: score = count * weight * idf
        ```
    -   Sort the documents by score in descending order.
    -   Take the top-N documents with the highest scores, map `doc_id` → `filename`, and return the result as a list of `(filename, score)` tuples.

### 3. src/search_multi.py (function find_multi)

-   **Input:**
    -   `wordfile_path` (a file containing the query: each line is `"word weight"`),
    -   `N`,
    -   `inverted_index`,
    -   `doc_table`.

-   **Processing:**
    -   Read each line and split it into `(word, weight)`.
    -   For each word, if it exists in the index, iterate over `(doc_id, count)` and accumulate `count * weight` into `scores[doc_id]`.
    -   After processing the entire file, sort the `scores` and select the top-N, then return a list of `(filename, total_score)`.

### 4. src/utils.py

Contains only one function: print_top_documents(results) to print to the screen in the format:

```bash
filename1.txt: score1
filename2.txt: score2
```

### 5. main.py

-   **Building the index, doc_table, and term_table:**

    ```bash
    index, doc_table, term_table = create_index('data', 'stoplist.txt')
    ```

    **Main Menu Loop:**

    The program runs in an infinite loop (`while True`) until the user chooses to exit.

    The user selects a search mode:

    -   `0`: Exit the program
    -   `1`: Search by a single word
    -   `2`: Search by multiple words

-   **Single-word Search**

    The user inputs: `word` (keyword), `weight` (an integer)

    ```bash
    results = find_single(word, weight=weight, N=3, inverted_index=index, doc_table=doc_table)
    print_top_documents(results)
    ```

-   **Multi-word Search**

    Display a message indicating that the program is searching for keywords from the file `data/query_words.txt`.

    ```bash
    results = find_multi('data/query_words.txt', N=3, inverted_index=index, doc_table=doc_table)
    print_top_documents(results)
    ```

## Project Structure

```
project/
├── data/                   # Folder for text documents and query file
│   ├── document1.txt
│   ├── document2.txt
│   └── query_words.txt     # Each line = 1 multi-word query
├── stoplist.txt            # Stop words (1 word per line)
├── main.py                 # Entry point
├── src/
│   ├── index_builder.py    # Index construction logic
│   ├── search_single.py    # Single keyword search
│   ├── search_multi.py     # Multi-keyword search
│   └── utils.py            # Utility functions
├── requirements.txt
└── docker-compose.yml      # Docker config
```

## Installation

Follow these steps to set up and run the application locally.

### 1. Clone the repository:

```bash
git clone https://github.com/hoangngm2083/inverted-indexes.git
```

🔹**Option 1: Run the project with Docker**

-   **Check WSL:**

    Make sure WSL 2 and Ubuntu are installed. Run the following in PowerShell:

    ```bash
    wsl --list --verbose
    ```
    If you see Ubuntu with `VERSION: 2`, you're ready. If not, install WSL.

-   **Give execute permission to the script:**

    ```bash
    chmod +x install-docker.sh
    ```

-   **Run the script:**

    ```bash
    sudo ./install-docker.sh
    ```
    -   The script will request sudo privileges and automatically perform the necessary steps.
    -   The process may take a few minutes depending on your network speed.

-   **Log out and log back in:**

    After the script finishes, exit WSL:

    ```bash
    exit
    ```
    Then reopen WSL:

    ```bash
    wsl
    ```

-   **Verify the installation:**

    Run the following command:

    ```bash
    docker run hello-world
    ```
    If you see a message from the container, Docker is working properly.

🔹**Option 2: Run the project without Docker (manually using Python)**

-   Make sure you have:
    -   `Python` v3.7 or later
    -   `pip`

-   **Install required libraries:**

    ```bash
    pip install -r requirements.txt
    ```

-   **Build the inverted index:**

    ```bash
    python src/index_builder.py
    ```

-   **Perform search:**

    -   To search for a single word or phrase:

        ```bash
        python src/search_single.py
        ```

    -   To search for multiple words from the query_words.txt file:

        ```bash
        python src/search_multi.py
        ```

## Running the App

### 🔹Option 1: Run with Docker

```bash
docker-compose run --rm inverted-index-project
```

### 🔹Option 2: Run locally (Python 3.10+)

```bash
pip install -r requirements.txt
python main.py
```

## Search Instructions

### Mode Selection
When the app starts, you'll be prompted to choose a search mode:
```
Selection search mode: 
0: exit
1: single search
2: multi search
```

### Mode 1: Single Keyword Search
- Input a **keyword** and its **weight** (integer).
- Only exact matches will be found (e.g., `cat` != `cats`).
- Top 3 matching documents will be displayed with scores.

    **Example:**
    ```
    Enter your search mode: 1
    Enter your search word: cat
    Enter your search word's weight: 2
    ```

    **Output**
    ```
    Top documents for word='cat' with weight='2':
    Không tìm thấy tài liệu phù hợp.
    ```

### Mode 2: Multi-Keyword Search
- Queries are read from `data/query_words.txt`, one per line.
- Each line can contain multiple words.
- Top 3 documents for each query will be shown.

    **Example:**
    ```
    Enter your search mode: 2
    ```

    **Output**
    ```
    Top documents for query from query_words.txt:
    doc2.txt: 4
    ```

## Notes
- Ensure all input `.txt` documents are placed in the `data/` folder.
- `stoplist.txt` should contain common words to ignore during indexing.
- All search is case-sensitive and exact.
- The app uses a simple terminal interface with `input()` calls, best run with `docker-compose run` for full stdin compatibility.

## Features
- Create an inverted index from a folder of `.txt` files
- Stop word filtering using a provided stoplist
- Exact match search (e.g., `cat` does **not** match `cats` or `Cat`)
- Two search modes:
  - Single keyword with weight
  - Multi-keyword queries loaded from file
- Top-N ranking of matched documents

## License
This project is for educational and demonstration purposes.

## Contributors

<table>
    <tr>
        <td align="center">
            <a href="https://github.com/hoangngm2083">
                <img 
                    src="https://avatars.githubusercontent.com/u/189230434?v=4"
                    alt="hoangngm2083" width="100px;" height="100px;" 
                    style="border-radius: 4px; background: #fff;"
                /><br />
                <sub><b>Nguyễn Minh Hoàng</b></sub>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/T-Anh-202">
                <img 
                    src="https://avatars.githubusercontent.com/u/208268848?v=4"
                    alt="T-Anh-202" width="100px;" height="100px;" 
                    style="border-radius: 4px; background: #fff;"
                /><br />
                <sub><b>T-Anh-202</b></sub>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/ketapcode">
                <img 
                    src="https://avatars.githubusercontent.com/u/125541868?v=4"
                    alt="ketapcode" width="100px;" height="100px;" 
                    style="border-radius: 4px; background: #fff;"
                /><br />
                <sub><b>ketapcode</b></sub>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/NgocYenDg">
                <img 
                    src="https://avatars.githubusercontent.com/u/163749076?v=4"
                    alt="NgocYenDg" width="100px;" height="100px;" 
                    style="border-radius: 4px; background: #fff;"
                /><br />
                <sub><b>NgocYenDg</b></sub>
            </a>
        </td>
    </tr>
</table>
