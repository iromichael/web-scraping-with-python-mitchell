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


## Questions / things I'm still unsure about
- Exactly how recursions works, still goes over head