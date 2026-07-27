# Chapter 5: Advanced HTML Parsing

## What this chapter covers
- Moving through the HTML tree structure — parents, children, descendants, siblings
- Using find/find_all more precisely by targeting specific attributes

## New things I learned
- Difference between children (direct, one level down) and descendants 
  (anything nested inside, any depth)
- Browsers auto-insert tags like <tbody> when rendering tables, even if 
  the raw HTML source never had one — DevTools' Elements panel shows the 
  browser's cleaned-up version, not the actual HTML my scraper receives
- Best way to check what my scraper actually sees: print(bs.prettify()) 
  or view-source, not DevTools Inspect
- I already knew find/find_all, but now understand why targeting specific 
  attributes (id, class, attributes/custom HTML attributes) is better practice than 
  relying on position/nesting — if the site's layout changes later, 
  attribute-based selectors are more likely to still work
- Regex lets you match a "shape" of text instead of one exact string 
  (e.g. img1.jpg, img2.jpg, img6.jpg all matched by one pattern) — still 
  need more practice actually writing these myself
- find_all can take a lambda function instead of a tag/attribute — lets 
  you filter by any custom condition, e.g.:
  `bs.find_all(lambda tag: tag.get_text() == 'Or maybe he\'s only resting?')`
- The same result can also be done without a lambda:
  `bs.find_all('', text='Or maybe he\'s only resting?')`

  ## Questions / things I'm still unsure about
- Regex
- Regex syntax still very confusing — need more practice with simple patterns 
  before it clicks properly
- Haven't practiced writing my own lambda functions yet, only seen the example