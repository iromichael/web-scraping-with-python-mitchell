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

  ## Questions / things I'm still unsure about
- Regex