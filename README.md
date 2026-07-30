# Web Scraping with Python (3rd ed, Ryan Mitchell)

My notes and code as I work through the book, chapter by chapter.

Each chapter folder contains my own typed-out/rebuilt code examples and a 
`notes.md` with what I learned, what confused me, and how I adapted things.

Where the book uses urlopen and regex for selecting HTML, I've generally 
rewritten examples using requests and BeautifulSoup instead (true for 
chapters 4-6 so far) — requests is the more common tool in real-world 
Python work, and BeautifulSoup is generally the more reliable choice for 
parsing HTML structure, since regex isn't well-suited to nested/inconsistent 
markup. This may not apply to every later chapter, depending on what each 
one actually covers.

````markdown
## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
````

## Progress

### Part I: Building Scrapers

| Chapter | Topic | Status |
|---|---|---|
| 1 | How the Internet Works | ✅ done |
| 2 | The Legalities and Ethics of Web Scraping | ✅ done |
| 3 | Applications of Web Scraping | ✅ done |
| 4 | Writing Your First Web Scraper | ✅ [done](./ch04-your-first-web-scraper) |
| 5 | Advanced HTML Parsing | ✅ [done](./ch05-advanced-html-parsing) |
| 6 | Writing Web Crawlers | ✅ [done](./ch06-writing-web-crawlers) |
| 7 | Web Crawling Models | 🔄 in progress |
| 8 | Scrapy | ⬜ not started |
| 9 | Storing Data | ⬜ not started |

### Part II: Advanced Scraping

| Chapter | Topic | Status |
|---|---|---|
| 10 | Reading Documents | ⬜ not started |
| 11 | Working with Dirty Data | ⬜ not started |
| 12 | Reading and Writing Natural Languages | ⬜ not started |
| 13 | Crawling Through Forms and Logins | ⬜ not started |
| 14 | Scraping JavaScript | ⬜ not started |
| 15 | Crawling Through APIs | ⬜ not started |
| 16 | Image Processing and Text Recognition | ⬜ not started |
| 17 | Avoiding Scraping Traps | ⬜ not started |
| 18 | Testing Your Website with Scrapers | ⬜ not started |
| 19 | Web Scraping in Parallel | ⬜ not started |
| 20 | Web Scraping Proxies | ⬜ not started |