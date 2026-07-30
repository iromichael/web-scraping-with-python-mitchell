# Chapter 6: Writing Web Crawlers

## What this chapter covers
- Getting all links from a page
- Writing scrapers that follow links across multiple pages automatically
- Two crawling patterns: random with a (while loop) and exploring indepth with (recursion)

## New things I learned
- The book's Wikipedia example has no headers set — without a real 
  User-Agent, requests don't get a 200 response for Wikipedia
- Used AI help to add headers with urlopen specifically — already knew 
  how to do this with requests, but urlopen needs it wrapped in a 
  Request object first, different syntax
- The example in the book referenced wikipedia div and classes and id but 
  this has changed and I was able to use the attributes to redo this example, 
  and instead of using regex for selector tags, I used beautiful soup instead
- Wrote my own function that outputs all internal links of a wiki page, 
  given a page URL as an argument
- the book introduced random wikipedia crawling; concept understood at a high 
  level, not comfortable with implementation yet
- learnt that scraped urls come in more than one valid format (relative paths, 
  protocol relative, and full urls) and a robust scraper needs to normalize whichever 
  form it encounters into something it can actually request, rather than assuming 
  every href will be consistent
- Recursion — a function calling itself. Different rhythm from a loop: 
  dives deep into the first new thing it finds before working through 
  the rest (depth-first), rather than moving through options one at a 
  time in sequence
- Learnt how important it is to place sleep() in the right place
- Always check stop/limit conditions inside functions AND inside loops, so you 
  have better control of your program and prevent bugs — learned this the hard way 
  when a 5-page limit printed way more because the check wasn't inside the for loop too
- urlparse breaks a URL into pieces (scheme, netloc, path etc) — netloc is 
  the domain. Used this to compare a link's domain against the current 
  page's domain to decide if a link is internal or external. 
  An exmaple is added below:
  Example breakdown:
```python
  url = 'https://cat.example/list;meow?breed=siberian#pawsize'
  urllib.parse.urlparse(url)
```
  - `https` = scheme (first element of a URL)
  - `cat.example` = netloc (sits between the scheme and path)
  - `/list` = path (between the netloc and params)
  - `meow` = params (sits between path and query)
  - `breed=siberian` = query (between the params and fragment)
  - `pawsize` = fragment (last element of a URL)

- Built getInternalLinks and getExternalLinks — same scanning pattern, 
  opposite filter. Internal keeps same-domain links (and rebuilds relative 
  links like /wiki/X into full URLs using the page's own scheme+netloc). 
  External keeps links with a domain that's different from the current page
- Built getAllExternalLinks — crawls an entire site by recursively visiting 
  every internal page, collecting every unique external link found anywhere 
  on the site into one master list
- Used a dictionary (allExtLinks = {}) instead of a list, so each external 
  link maps to the specific internal page it was found on — not just "here's 
  a link" but "here's a link, and here's where it came from"
- Same recursion depth-first pattern as before, but this time a limit had to 
  go in from the start (max_pages) since this function has zero natural 
  stopping point on its own — it'll try to visit every reachable page on 
  a site otherwise
- Realized a limitation: comparing by domain only means a client's own CDN 
  (e.g. fastcdn.co hosting their PDFs) shows up as "external" even though 
  it's really the same business — the code has no way to know that automatically


## Questions / things I'm still unsure about
- Exactly how recursions works, still goes over head