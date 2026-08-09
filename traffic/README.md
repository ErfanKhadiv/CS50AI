# Traffic — CNN Traffic Sign Classifier

A convolutional neural network that classifies German traffic sign images ([GTSRB dataset](https://benchmark.ini.rub.de/gtsrb_news.html), 43 categories).

## How it works
- `load_data()` — reads and resizes images from category subfolders into arrays + labels
- `get_model()` — builds a CNN: 2 conv+pool blocks, a flatten layer, a 128-unit dense layer with dropout, and a softmax output layer over 43 classes
- Trained with the Adam optimizer

See [`EXPERIMENTATION.md`](EXPERIMENTATION.md) for the full writeup of architecture choices — number of conv layers, filter sizes, dropout rate, and optimizer comparisons (Adam vs. RMSprop vs. SGD) tried during development.

## Run
```bash
pip install -r requirements.txt
python traffic.py gtsrb [model.h5]
```
(Expects the GTSRB dataset in a `gtsrb/` folder with one subfolder per category — not included here due to size; download separately.)

## What it demonstrates
CNN architecture design and the iterative experimentation process (documented, not just the final result) — trying and comparing alternatives rather than landing on one architecture by guesswork.
