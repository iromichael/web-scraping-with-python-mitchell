# Chapter 4: Writing Your First Web Scraper

## What this chapter covers
- Writing a scraper (getTitle function) that doesn't crash when a page 
  fails to load or doesn't have the structure expected

## New things I learned
- HTTPError vs URLError — HTTPError means the server responded but with 
  an error status. URLError means couldn't reach the server at all.
- Both need importing from urllib.error — not built-in
- AttributeError is built-in, no import needed — happens when trying to 
  access something on a None result (e.g. bs.body.h1 when there's no h1)
- `except SomeError as e` lets you capture and inspect the actual error 
  object, though the example in this chapter doesn't actually use `e` itself
- A function can have multiple return statements — whichever one is hit 
  first ends the function immediately

## Questions / things I'm still unsure about
- try/except is still going over the top of my head, I'll need to practice it more