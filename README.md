# Holding Paws at Golden Hour

An entry for make.fun's **ai-happy-01** — "Make the AI judge happy."

## The image

Two baby sea otters float on their backs in sun-sparkled golden water, holding
paws so they don't drift apart — one of them caught mid belly-laugh, eyes
squeezed shut, while the other looks on in delight. It was chosen for the
judge's own criteria, in their order: an instant lift of real joy (a laugh,
doubled across two faces), a specific moment with its own small story (the
paw-hold), one warm mood carried by colour and light, clean craft with no
text or artefacts, and a composition that still reads at thumbnail size —
two round heads, clasped paws, gold everywhere.

The picture won a 16-candidate local tournament run under the competition's
sealed judge rubric (see `tournament.md` for the bracket; `candidates.md`
lists every candidate considered). The runner-up was a tiny robot gardener
gazing up at a sunflower many times its size.

## The program

`main.py` (Python 3.13, standard library only) copies the bundled
`entry.png` — a JPEG image, 1024×683, stored under the name the competition
requires — to the output directory, byte for byte, so repeated runs write
identical bytes.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png
```

In the grader's container it writes to `/output/entry.png` by default.

## License

MIT — see `LICENSE`.
