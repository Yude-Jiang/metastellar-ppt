"""Render a .pptx to PNG previews on Linux (no PowerPoint needed).

pptx -> pdf (LibreOffice headless) -> png per slide (poppler pdftoppm).
Usage: python tools/preview.py <deck.pptx> <outdir>
Writes <outdir>/preview-1.png, preview-2.png, ... (one per slide).
Open each one to verify layout by eye.
"""
import glob
import os
import subprocess
import sys


def main():
    pptx = sys.argv[1]
    outdir = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(pptx) or "."
    os.makedirs(outdir, exist_ok=True)

    # clear stale previews so the count always matches the current deck
    for old in glob.glob(os.path.join(outdir, "preview-*.png")):
        os.remove(old)

    subprocess.run(
        ["soffice", "--headless", "--convert-to", "pdf", "--outdir", outdir, pptx],
        check=True,
    )
    pdf = os.path.join(outdir, os.path.splitext(os.path.basename(pptx))[0] + ".pdf")
    subprocess.run(
        ["pdftoppm", "-png", "-r", "150", pdf, os.path.join(outdir, "preview")],
        check=True,
    )
    pngs = sorted(glob.glob(os.path.join(outdir, "preview-*.png")))
    print("saved", len(pngs), "preview image(s):", *[os.path.basename(p) for p in pngs])


if __name__ == "__main__":
    main()
