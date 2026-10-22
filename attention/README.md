# Attention

Visualizes the self-attention heads of BERT (`bert-base-uncased`) on a masked sentence.

Given a sentence containing `[MASK]`, the program:

1. Predicts the top 3 words for the mask using `TFBertForMaskedLM`.
2. Generates one grayscale diagram per attention head (12 layers x 12 heads = 144 PNGs), where lighter cells mean higher attention between two tokens.

See [`analysis.md`](analysis.md) for observations on two heads, with the matching diagrams in [`diagrams/`](diagrams/).

## Run

```
pip install -r requirements.txt
python mask.py
Text: She bought a [MASK] cake for the party.
```

The first run downloads the pre-trained model. Diagrams are written to the current folder as `Attention_Layer<L>_Head<H>.png` (ignored by git).

## What I implemented

- `get_mask_token_index`: finds the position of the mask token in the tokenized input
- `get_color_for_attention_score`: maps an attention score to a gray level
- `visualize_attentions`: loops over all layers and heads to generate every diagram
- `analysis.md`: interpretation of selected heads

Provided by the course: `main`, `generate_diagram` and the font.
