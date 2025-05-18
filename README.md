<p align="center">
  <a href="https://ptithcm.edu.vn/" title="Học viên Công nghệ Bưu chính viễn thông cơ sở tại Tp Hồ Chí Minh" style="border: none;">
    <img src="https://daihoconline.edu.vn/wp-content/uploads/2022/12/logo_bcvt_transparent_Original_White-background_600px.png" alt="Học viện Công nghệ Bưu chính viễn thông">
  </a>
</p>

# Inverted Indexes

This is exercise 5 in the exercises_06 folder, under the exercises and project directory, is part of the Multimedia Database Systems course. It requires building a program that implements an inverted index for text retrieval.

## Supervisor

MSc. Le Ha Thanh – Faculty of Information Technology 2, Posts and Telecommunications Institute of Technology, Ho Chi Minh City Campus.

## Table of Contents

-   [Students’ Information](#students-information)
-   [Problem Description](#problem-description)
-   [Project Implementation Details](#project-implementation-details)
-   [Installation](#installation)
-   [Run The Program](#run-the-program)
-   [Example Input & Output](#example-input--output)
-   [Contributors](#contributors)

## Students’ Information

|**No.**|**Student ID**|  **Full Name**       |       **Email**                 |
|-------|--------------|----------------------|---------------------------------|
|   1   |N21DCCN034    |Nguyễn Minh Hoàng     |n21dccn034@student.ptithcm.edu.vn|
|   2   |N21DCCN072    |Tạ Hoàng Trung Sơn    |n21dccn072@student.ptithcm.edu.vn|
|   3   |N20DCCN086    |Lê Tuấn Anh           |N20DCCN086@student.ptithcm.edu.vn|
|   4   |N21DCCN097    |Đặng Ngọc Yến         |n21dccn097@student.ptithcm.edu.vn|

## Problem Description

As a project, write a program that implements inverted indexes. Your program must contain the following routines:

(a) CreateIndex(Dir, StopList) takes a directory name and a file called StopList (in that directory) as input. It returns an inverted index as output. The DocTable includes all files in the directory Dir, except for the StopList file. The TermTable includes only all words occurring in the directory that start with the letter C (lower- or uppercase).

(b) Find(Word, Weight, N) finds the top N documents in the index associated with the word specified in the input.

(c) Find(WordFile, N) is similar to the above, but there is one difference. Instead of taking a single word as part of the input, it takes a file called WordFile as input. This file has, on each line, a word (string) and a weight (integer). It then attempts to find, using the inverted index, the top N matches for this query.

## Project Implementation Details

### 1. src/index_builder.py (function create_index)

**Read the stopword list**
-   Open the `stoplist.txt` file in the `data` directory and store the contents in the `stopwords` set (all converted to lowercase).

**Iterate through each file in the `data` directory (excluding the stoplist file):**
-   Read the entire content and convert it to lowercase.
-   Use the regular expression `\b\w+\b` to extract words.
-   Assign a new `doc_id` (which is the index of the file in `doc_table`) and store the mapping `doc_id → filename`.

**Build the inverted index**
-   For each word in `words`:
    -   Skip the word if it is in `stopwords` or does not start with the letter “c”.
    -   Add the word to `term_table` (this is just to keep track of indexed terms; it is not used directly in search).
    -   In `inverted_index[word]` (which is a dictionary), increment the counter: `inverted_index[word][doc_id] += 1`.

**The function returns three structures:**
-   `inverted_index`: `{ term: { doc_id: term_frequency, … }, … }`
-   `doc_table`: `{ doc_id: filename, … }`
-   `term_table`: set of indexed words (those that start with “c”)

### 2. src/search_single.py (function find_single)

**Input:**
-   `word` (string),
-   `weight` (integer),
-   `N` (number of documents to retrieve),
-   and the pre-built `inverted_index` and `doc_table`.

**Processing:**
-   Normalize the word (convert to lowercase), and check if it exists in the `inverted_index`.
-   For each `(doc_id, count)` in the posting list of that word:
    -   Compute the score as `score = count * weight`.
-   Take the top-N results sorted by descending score, then map them back to `(filename, score)` to return.

### 3. src/search_multi.py (function find_multi)

**Input:**
-   `wordfile_path` (a file containing the query: each line is `"word weight"`),
-   `N`,
-   `inverted_index`,
-   `doc_table`.

**Processing:**
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

-   **Index Construction**

    ```bash
    index, doc_table, term_table = create_index('data', 'stoplist.txt')
    ```

-   **Single-word Search**

    Search with the keyword `"cat"`, weight `3`, and retrieve `3` results:

    ```bash
    results = find_single('cat', weight=3, N=3, inverted_index=index, doc_table=doc_table)
    print_top_documents(results)
    ```

-   **Multi-word Search**

    Search using multiple words from the file `data/query_words.txt`, retrieving `3` results:

    ```bash
    results = find_multi('data/query_words.txt', N=3, inverted_index=index, doc_table=doc_table)
    print_top_documents(results)
    ```

## Installation

Follow these steps to set up and run the application locally.

### 1. Clone the repository:

```bash
git clone https://github.com/hoangngm2083/inverted-indexes.git
```

🔹**Option 1: Run the project WITHOUT Docker (manually using Python)**

Make sure you have:
-   `Python` v3.7 or later
-   `pip`

### 2. Install required libraries:

```bash
pip install -r requirements.txt
```

### 3. Build the inverted index:

```bash
python src/index_builder.py
```

### 4. Perform search:

-   To search for a single word or phrase:

    ```bash
    python src/search_single.py
    ```

-   To search for multiple words from the query_words.txt file:

    ```bash
    python src/search_multi.py
    ```

🔹**Option 2: Run the project with Docker**

## Run The Program

### 🔹Option 1: Run the project without Docker

```bash
python main.py
```

### 🔹Option 2: Run the project with Docker

```bash
docker-compose up
```

## Example Input & Output

### Input
 **(a) create_index('data', 'stoplist.txt')**
-   The name of the directory: `data`
-   The name of the file containing the list of stop words: `stoplist.txt`

**(b) find_single('cat', weight=3, N=3, inverted_index=index, doc_table=doc_table)**
-   The keyword to search for: `cat`
-   An integer weight factor applied to term frequency or score: `weight=3`
-   The number of top documents to return: `N=3`
-   `inverted_index=index`
-   `doc_table=doc_table`

**(c) find_multi('data/query_words.txt', N=3, inverted_index=index, doc_table=doc_table)**
-   The keywords to search for: `data/query_words.txt`
-   The number of top documents to return: `N=3`
-   `inverted_index=index`
-   `doc_table=doc_table`

### Output
**(a) create_index('data', 'stoplist.txt')**

    index {'cats': {0: 1}, 'clever': {0: 1}, 'curious': {0: 1}, 'creatures': {0: 1}, 'climb': {0: 1}, 'chase': {0: 1}, 'cat': {0: 1, 2: 1}, 'computer': {1: 1, 2: 1}, 'concepts': {1: 1}, 'can': {1: 1}, 'challenging': {1: 1}, 'coding': {1: 1, 2: 1}, 'c': {1: 2}, 'common': {1: 1}, 'cs': {1: 1}, 'courses': {1: 1}}
    
    doc_table {0: 'doc1.txt', 1: 'doc2.txt', 2: 'query_words.txt'}
   
    term_table {'can', 'common', 'concepts', 'cat', 'courses', 'curious', 'clever', 'computer', 'c', 'chase', 'cats', 'cs', 'creatures', 'coding', 'climb', 'challenging'}

**(b) find_single('cat', weight=3, N=3, inverted_index=index, doc_table=doc_table)**

    Top documents for word='cat':
    query_words.txt: 3

**(c) find_multi('data/query_words.txt', N=3, inverted_index=index, doc_table=doc_table)**

    Top documents for query from file:
    query_words.txt: 6
    doc2.txt: 4

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
