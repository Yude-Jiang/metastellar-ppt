# ST Slide Layout Library

A catalog of proven, brand-compliant content layouts from ST's official slide-layout library.
When building a content slide, **pick the archetype that fits the content shape**, then style
it with the palette in `brand-spec.md`. All of these sit on the **"Title Only"** layout — the
title, corner accent, logo, and slide number come from the template; everything else you place
as shapes.

> Note: the small light-blue **"Example" tag** top-left in the source library is only a library
> marker. **Remove it on real slides.**

## Shared frame (every archetype)
- **Title**: top of slide, ST Dark Blue Arial. Right-aligned for most content slides;
  centered/left also seen. One or two lines.
- **Corner accent**: thin ST Dark Blue block at the top-right edge (from template).
- **Logo**: ST logo bottom-left. **Slide number** bottom-right. (template footer)
- **Content band** starts ~1.5 in from top, below the title.

## How to choose
| If the content is… | Use archetype |
|---|---|
| One use-case told over a hero photo | `app-photo-overlay` |
| One product/tech with 2–3 grouped feature blocks + a hero image | `left-image-feature-boxes` |
| Two products/options compared head-to-head | `product-comparison-2up` |
| 2–4 parallel items, each = image + a few bullets | `cards-Nup` (yellow or graded header) |
| Several items that share one punchline | add a bottom **yellow message bar** (`cards-4up-graded-message-bar`) |
| 4–6 categories each with an icon + label + one fact | `icon-cards-5up` |
| 4 facets of one thing, visual-heavy | `quadrant-2x2-center-badge` |
| A portfolio/overview of 4–6 image tiles | `image-grid-2x3-caption-bars` |
| A sequential N-step process | `process-flow-circles` |
| Rows of label → content → annotation, pointing at a visual | `row-label-table-visual` |
| Evolution over time | `timeline-era-cards` |

---

## 1. `app-photo-overlay` — application / use-case
Hero photo fills the left (or full) area; text floats on top.
- **Photo**: left half to full-bleed, behind everything.
- **Message bar**: full-width **ST Dark Blue** band near the top, white 20 pt Arial bold —
  the core statement.
- **Yellow callout**: a benefit sentence, ST Dark Blue text.
- **Gray bullet box** (`#EEEFF1`, slight transparency): the supporting bullet list, dark-blue
  bullets.
- Use when one application is the whole story. Keep to 4–6 bullets.

## 2. `left-image-feature-boxes` — product / technology highlight
- **Left image**: full-height product/beauty shot, ~⅓ width.
- **Feature boxes** (2–3): each a filled rectangle with a bold heading + 1–2 short paragraphs.
  Color them from the dark-blue ramp + one gray box (e.g. box 1 = `#03234B`, box 2 = `#425978`,
  side box = `#EEEFF1`). White text on the blue boxes, dark-blue text on gray.
- Title can be two lines, right-aligned.

## 3. `product-comparison-2up` — two products side by side
- **Two equal columns.** Each column:
  - **Header bar**: product name (bold) + one-line descriptor. Differentiate the two with
    **ST Dark Blue** (left) and **ST Light Blue** (right) headers (white text).
  - **Photo** of the application.
  - **Gray box** (`#EEEFF1`) with 2–3 spec bullets, plus a small product (package) shot.
- Great for "low voltage vs high voltage", "entry vs premium", etc.

## 4. `cards-Nup` — N parallel cards (2, 3 or 4 across)
The workhorse. N equal columns, each card = **header bar + image + gray bullet box**.
- **Header bar** options:
  - **Yellow** header, ST Dark Blue text (clean, high-energy) — see High-power example.
  - **Graded** headers from the dark-blue ramp (Step 1→4 across the columns) when you want the
    set to read as a sequence/intensity — see the 4-up example.
- **Image** sits directly under the header.
- **Gray box** (`#EEEFF1`) holds the bullets/short text (centered text works for 1–3 lines).
- Keep all cards the same width/height; align tops and bottoms (use Shift/Ctrl+Shift).

## 5. `cards-4up-graded-message-bar` — cards + bottom punchline
Same as `cards-Nup` (4 graded-header cards) **plus** a **full-width ST Yellow message bar**
across the bottom with the single takeaway (e.g. the part number + "Efficient, flexible, and
available!"), ST Dark Blue text, bold key words. Use when the cards build to one conclusion.

## 6. `icon-cards-5up` — categories with icons
- **Top message bar**: ST Dark Blue full-width band, white text — the umbrella statement.
- **5 columns** (4–6 works), each:
  - **Yellow icon tile** (square) with a dark-blue **monochrome icon** (SVG pictogram, not
    SmartArt, not AI art).
  - **Gray box** (`#EEEFF1`) with a bold heading, a standard/label line, and a short
    description — all ST Dark Blue, centered.
- Ideal for certifications, pillars, capability families.

## 7. `quadrant-2x2-center-badge` — four facets, visual
- **2×2 grid.** Cells alternate **photo** and **colored text panel**; panels use `#03234B`
  and `#425978` (white headings + short body).
- **Center badge**: a white circle straddling the four cells holding the product/tool **logo**.
- Title top-right. Use for a tool/product with four selling points and strong imagery.

## 8. `image-grid-2x3-caption-bars` — portfolio / overview grid
- **6 tiles** in 2 rows × 3 columns (also works 1×N or 2×2). Each tile = **caption header bar +
  photo**.
- **Alternate header colors** tile-to-tile between **ST Dark Blue** (white text) and
  **ST Yellow** (dark-blue text) for rhythm.
- Use for "our product families", "our markets", a visual table of contents.

## 9. `process-flow-circles` — sequential steps
- **N circles** in a row (5 shown), **alternating `#03234B` and `#8091A5`**, white text inside
  (short label per step).
- **Dotted connector** weaving through the circles; an arrowhead on the last.
- **Step markers**: small **ST Yellow** dots on short lines above/below alternating circles,
  each with "**Step N**" (bold) + a label, ST Dark Blue.
- Use for workflows/pipelines. Don't exceed ~6 steps.

## 10. `row-label-table-visual` — labelled rows pointing to a visual
- **Left stack of rows**: each row = **ST Dark Blue label box** (white bold) + **gray content
  cell** (`#EEEFF1`, holds a logo/diagram/text) + optional right-side annotation text.
- **Large gray arrow** pointing right from the rows to a **supporting visual** (e.g. a product
  screenshot / device render).
- **Light-blue URL button** (`#3CB4E6`) bottom with a globe pictogram for the call-to-action link.
- Use to map "capability → asset → where it lives".

## 11. `timeline-era-cards` — evolution over time
- **N era cards** across the top: each = **ST Yellow header** (era name, dark-blue bold) +
  **gray box** (`#EEEFF1`) with bullets.
- **Navy arrow timeline** beneath them (`#03234B`, arrowhead at right) with **ST Yellow circle
  markers** (white ring) at each era and a **year label** (dark-blue bold) under each marker.
- **Photo strip**: one image per era aligned to the columns at the bottom.
- Use for market evolution, roadmap history, generational progress.

---

## Applying any of these
1. Confirm it's a **"Title Only"** slide.
2. Build with **shapes that embed their own text** (don't stack text boxes on rectangles);
   set every text frame to **Do not Autofit**.
3. Respect the **2–3 color** rule per slide — these archetypes already do (blue ramp + gray +
   one yellow accent).
4. Source photos from brand.st.com; icons as **SVG pictograms**; **no AI imagery, no SmartArt**.
5. Maintain image **aspect ratio**; align card edges with the grid/guides.

Parametrized python-pptx builders for the recurring families (`cards-Nup`,
`product-comparison-2up`, `process-flow-circles`) are in `pptx-implementation.md`.
