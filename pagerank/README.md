# PageRank

Ranks web pages by importance using the **random surfer model**, computed two ways:

- `sample_pagerank`: simulates a surfer who follows a random link with probability `d = 0.85` and jumps to a random page otherwise, then counts how often each page is visited (10,000 samples).
- `iterate_pagerank`: repeatedly applies the PageRank formula until every rank changes by less than 0.001.

`transition_model` returns the next-page distribution for the current page. Pages with no outgoing links are treated as linking to every page.

The two methods agree closely, which is a good sanity check.

## Run

```
python pagerank.py corpus0
```

```
PageRank Results from Sampling (n = 10000)
  1.html: 0.2157
  2.html: 0.4306
  3.html: 0.2228
  4.html: 0.1309
PageRank Results from Iteration
  1.html: 0.2198
  2.html: 0.4294
  3.html: 0.2198
  4.html: 0.1311
```

(Sampling values vary slightly between runs.) `crawl` and `main` are provided by the course; the other three functions are mine.
