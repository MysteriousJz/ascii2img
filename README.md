# ascii2img

Convert ASCII / Unicode box-art text files to **pixel-perfect PNG images** — no
line-wrapping, no missing box-drawing characters, identical appearance on every
device.

## Why?

Browser CSS cannot reliably render Unicode box-drawing characters
(`─│┌┐└┘├┤┬┴┼═║╔╗╚╝╠╣╦╩╬`) on mobile devices.  Server-side image generation
with a monospace TrueType font solves the problem once and for all.

---

## Requirements

```
pillow>=9.0.0
```

Install with:

```bash
pip install -r requirements.txt
```

A monospace TrueType font with box-drawing support is required at runtime.
**DejaVu Sans Mono** and **Liberation Mono** are searched automatically on Linux
and macOS.  On other systems pass `--font /path/to/font.ttf`.

---

## CLI Usage

```bash
# single file
python ascii2img.py file.txt

# multiple files
python ascii2img.py file1.txt file2.txt

# wildcard (shell expands the glob)
python ascii2img.py *.txt

# all .txt files in a directory, writing PNGs to a separate folder
python ascii2img.py --dir ./art/ --output-dir ./images/
```

### Options

| Option | Default | Description |
|---|---|---|
| `--font FONT` | auto-detected | Path or family name of a TrueType monospace font |
| `--font-size PT` | `14` | Font size in points |
| `--bg COLOR` | `white` | Background colour (any Pillow-accepted value, e.g. `#1e1e1e`) |
| `--fg COLOR` | `black` | Foreground text colour |
| `--padding PX` | `10` | Blank pixel border around the text |
| `--output-dir DIR` | same as input | Directory where PNG files are written |
| `--dir DIR` | — | Process all `*.txt` files in *DIR* |

---

## Module Interface

```python
from ascii2img import convert

# Basic usage
convert("art.txt", "art.png")

# Custom colours and font size (dark theme)
convert(
    "art.txt",
    "art.png",
    font_size=16,
    bg="#1e1e1e",
    fg="#d4d4d4",
    padding=15,
)

# Custom font path
convert("art.txt", "art.png", font="/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf")
```

### `convert()` signature

```python
def convert(
    input_path: str,
    output_path: str,
    *,
    font: str | None = None,
    font_size: int = 14,
    bg: str = "white",
    fg: str = "black",
    padding: int = 10,
) -> None: ...
```

---

## Output guarantees

- **No anti-aliasing** — rendered with a TrueType rasteriser at the exact
  requested size; no subpixel smoothing is applied by Pillow's `ImageDraw.text`.
- **Lossless PNG** — no JPEG artefacts, no colour degradation.
- **Exact dimensions** — canvas is sized to fit the content exactly:
  `width = longest_line × char_width + 2 × padding`
  `height = line_count × char_height + 2 × padding`
- **All printable ASCII + Unicode box drawing** — any character supported by the
  chosen font is rendered correctly.

---

## Examples

The `examples/` directory contains sample input files and their rendered PNGs.

```
examples/box.txt    →  examples/box.png
examples/table.txt  →  examples/table.png
```

Generate them yourself:

```bash
python ascii2img.py examples/box.txt examples/table.txt
```
