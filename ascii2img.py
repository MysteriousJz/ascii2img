#!/usr/bin/env python3
"""ascii2img — Convert ASCII/Unicode box-art text files to pixel-perfect PNGs.

Usage (CLI):
    ascii2img.py file.txt
    ascii2img.py file1.txt file2.txt
    ascii2img.py *.txt
    ascii2img.py --dir ./art/ --output-dir ./images/

Module interface:
    from ascii2img import convert
    convert("art.txt", "art.png", font_size=14, bg="white", fg="black")
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from typing import Optional

from PIL import Image, ImageDraw, ImageFont

# Preferred monospace fonts with Unicode box-drawing support, searched in order.
_FONT_SEARCH_PATHS = [
    # Explicit paths for common Linux distributions
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
    "/usr/share/fonts/dejavu/DejaVuSansMono.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf",
    "/usr/share/fonts/liberation/LiberationMono-Regular.ttf",
    # macOS locations
    "/Library/Fonts/Courier New.ttf",
    "/System/Library/Fonts/Courier New.ttf",
    # Windows locations (for completeness / Wine environments)
    "C:/Windows/Fonts/cour.ttf",
]

_FONT_NAMES = [
    "DejaVuSansMono",
    "DejaVu Sans Mono",
    "LiberationMono",
    "Liberation Mono",
    "CourierNew",
    "Courier New",
]


def _load_font(font: Optional[str], font_size: int) -> ImageFont.FreeTypeFont:
    """Load a TrueType font.

    Tries *font* first (path or family name), then falls back through the
    built-in search list.  Raises ``RuntimeError`` if no suitable font is
    found.
    """
    candidates: list[str] = []
    if font:
        candidates.append(font)
    candidates.extend(_FONT_SEARCH_PATHS)

    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, font_size)
        except (IOError, OSError):
            pass

    # Last resort: try by family name via Pillow's font lookup
    for name in _FONT_NAMES:
        try:
            return ImageFont.truetype(name, font_size)
        except (IOError, OSError):
            pass

    raise RuntimeError(
        "No suitable monospace TrueType font found.  Install DejaVu Sans Mono "
        "or Liberation Mono, or pass --font /path/to/font.ttf."
    )


def _measure_char(font: ImageFont.FreeTypeFont) -> tuple[int, int]:
    """Return (char_width, char_height) for the given monospace font."""
    # Use 'W' as a representative wide character.
    bbox = font.getbbox("W")
    char_w = bbox[2] - bbox[0]
    # For line height, use a full-height character that includes descenders.
    # ascent + descent gives a reliable line height.
    ascent, descent = font.getmetrics()
    char_h = ascent + descent
    return char_w, char_h


def convert(
    input_path: str,
    output_path: str,
    *,
    font: Optional[str] = None,
    font_size: int = 14,
    bg: str = "white",
    fg: str = "black",
    padding: int = 10,
) -> None:
    """Convert a single ASCII/Unicode text file to a PNG image.

    Parameters
    ----------
    input_path:
        Path to the input text file.
    output_path:
        Destination PNG file path.
    font:
        Path or family name of a TrueType monospace font.  When *None* the
        function searches for DejaVu Sans Mono → Liberation Mono → Courier New.
    font_size:
        Point size used to render the font (default 14).
    bg:
        Background colour accepted by Pillow (e.g. ``"white"``, ``"#1e1e1e"``).
    fg:
        Foreground (text) colour (e.g. ``"black"``, ``"#d4d4d4"``).
    padding:
        Blank pixel border around the rendered text (default 10 px).
    """
    text = Path(input_path).read_text(encoding="utf-8")
    lines = text.splitlines()

    # Ensure at least one line so we never get a zero-sized canvas.
    if not lines:
        lines = [""]

    ttf = _load_font(font, font_size)
    char_w, char_h = _measure_char(ttf)

    max_len = max(len(line) for line in lines)
    img_w = max_len * char_w + 2 * padding
    img_h = len(lines) * char_h + 2 * padding

    # Create image — 'RGB' avoids lossy alpha and is guaranteed lossless as PNG.
    img = Image.new("RGB", (img_w, img_h), bg)
    draw = ImageDraw.Draw(img)

    y = padding
    for line in lines:
        if line:
            draw.text((padding, y), line, font=ttf, fill=fg)
        y += char_h

    # Save as lossless PNG.
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    img.save(output_path, format="PNG")


def _output_path(input_path: str, output_dir: Optional[str]) -> str:
    """Derive the output PNG path from *input_path* and an optional directory."""
    stem = Path(input_path).stem
    filename = stem + ".png"
    if output_dir:
        return str(Path(output_dir) / filename)
    return str(Path(input_path).with_suffix(".png"))


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        prog="ascii2img",
        description="Convert ASCII/Unicode box-art text files to pixel-perfect PNGs.",
    )
    parser.add_argument(
        "files",
        nargs="*",
        metavar="FILE",
        help="Input text file(s).",
    )
    parser.add_argument(
        "--dir",
        metavar="DIR",
        help="Process all *.txt files in DIR.",
    )
    parser.add_argument(
        "--output-dir",
        metavar="DIR",
        help="Directory where PNG files are written (default: same as input).",
    )
    parser.add_argument(
        "--font",
        metavar="FONT",
        help="Path or family name of a TrueType monospace font.",
    )
    parser.add_argument(
        "--font-size",
        type=int,
        default=14,
        metavar="PT",
        help="Font size in points (default: 14).",
    )
    parser.add_argument(
        "--bg",
        default="white",
        metavar="COLOR",
        help="Background colour (default: white).",
    )
    parser.add_argument(
        "--fg",
        default="black",
        metavar="COLOR",
        help="Foreground text colour (default: black).",
    )
    parser.add_argument(
        "--padding",
        type=int,
        default=10,
        metavar="PX",
        help="Padding in pixels around the text (default: 10).",
    )

    args = parser.parse_args(argv)

    inputs: list[str] = list(args.files)

    if args.dir:
        dir_path = Path(args.dir)
        if not dir_path.is_dir():
            print(f"ascii2img: error: --dir '{args.dir}' is not a directory.", file=sys.stderr)
            return 1
        inputs.extend(str(p) for p in sorted(dir_path.glob("*.txt")))

    if not inputs:
        parser.print_help()
        return 1

    errors = 0
    for input_file in inputs:
        if not os.path.isfile(input_file):
            print(f"ascii2img: warning: '{input_file}' not found, skipping.", file=sys.stderr)
            errors += 1
            continue
        out = _output_path(input_file, args.output_dir)
        try:
            convert(
                input_file,
                out,
                font=args.font,
                font_size=args.font_size,
                bg=args.bg,
                fg=args.fg,
                padding=args.padding,
            )
            print(f"  {input_file}  →  {out}")
        except (IOError, OSError, RuntimeError, ValueError) as exc:
            print(f"ascii2img: error: {input_file}: {exc}", file=sys.stderr)
            errors += 1

    return 0 if errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
