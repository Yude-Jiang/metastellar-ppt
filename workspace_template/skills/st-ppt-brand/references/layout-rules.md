# ST Layout & Composition Rules

## Layout selection
Right-click slide → Layout. Choose by slide type:

- **Use "Title Only" for ALL normal content slides.** Place your boxes/shapes/text in the
  body area yourself. This keeps composition consistent and avoids placeholder drift.
- **Special slides** use their dedicated layouts:
  - **Main title** (with or without picture)
  - **Section title**
  - **Agenda**
  - **Thank you**
- **Avoid** these layouts entirely: *Title and contents*, *Title and two contents*, *Empty*.

When generating programmatically, replicate the "Title Only" layout: a title placeholder at
top, everything else as free shapes.

## The key message bar
The single most distinctive ST slide element. The title explains the slide; **the message
bar states the one thing the audience should remember.**

Why it matters: surfaces the core idea, enforces brand/visual consistency, improves
readability and flow, supports the "less is more" approach.

Attributes — keep them exactly as the template defines:
- **Geometry** (16:9 = 13.333 in × 7.5 in): spans from the **left edge of the slide** to the
  **4th vertical guide**, and from the **3rd to the 5th horizontal guide** from the top.
  Working values: `x = 0, y ≈ 1.43 in, width ≈ 9.8 in, height ≈ 0.84 in`.
- **Fill**: one of ST Yellow, ST Dark Blue, ST Light Blue, or the first shade of dark blue.
- **Font**: **20 pt Arial, no exceptions.** Single color — white or dark blue (match the
  fill for contrast: dark-blue text on yellow/light-blue, white text on dark blue).
- Do not resize, reposition, or restyle beyond the allowed fills/text colors.

## Title area
- Keep the title in its reserved zone.
- **No graphical elements** in the title area **except** the sub-brand logo (or the
  10-years longevity stamp) in its reserved spot.

## Footer / footnotes
- Use the **pre-defined footer field**: Insert → (Text) → Header & Footer. Do not draw
  manual footnote text boxes.
- Slide numbers and the trademark/footer come from the template — leave them in place.

## Text-box best practices

### 1. Do NOT Autofit
In Format Shape → Text Box there are three options:
- *Shrink text on overflow* → changes font size/line spacing → inconsistent text across
  slides. **Avoid.**
- *Resize shape to fit text* → changes box height → causes alignment issues. **Avoid.**
- **Do not Autofit → the correct choice.** Keep it and size the box manually so font size
  and alignment stay uniform across the deck.

### 2. Embed text directly into shapes
Don't stack a separate "Text Box" on top of a colored rectangle. Any shape can hold text:
insert the rectangle and type into it. Embedded text moves and aligns with the shape, which
makes layout far easier.

### 3. Shade to organize
Use the light gray family (Gray 1/2/3) to distinguish blocks of text. Reserve **yellow for
one critical highlight** only.

## Images
- **Always maintain aspect ratio.** Hold **Shift** and drag from a **corner**; keep
  *Lock aspect ratio* checked in Format Picture.
- **Crop** via right-click → Crop; drag side/corner handles; you may reposition the image
  inside the crop window.
- Source images from brand.st.com (ST-owned). **No AI-generated images.** Prefer SVG for
  logos/icons/shapes; **never SmartArt.**

## Productivity conventions (apply when editing in PowerPoint)
- **Guides on**: View → tick *Guides* (shows margins, 50% lines, logo safe zone).
- **Shift** = constrain move to one axis. **Ctrl** + drag = duplicate. **Ctrl+Shift** +
  drag = duplicate aligned on one axis.
- **F4** repeats the last action (fast consistent formatting).
