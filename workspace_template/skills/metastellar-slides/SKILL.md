---
name: metastellar-slides
description: >
  Create polished, modern PowerPoint decks with the Metastellar blue design system.
  Use for pitches, reports, talks, and internal presentations. Pick layouts by content
  shape and density; prefer slide_theme.py helpers for consistent palette and contrast.
---

# Metastellar Slides

Build **16:9 PowerPoint (.pptx)** decks with a cohesive blue Tailwind-inspired theme.
This is **not** STMicroelectronics brand — design for clarity, hierarchy, and modern corporate polish.

## Workflow

1. Read `AGENTS.md` for the full build loop.
2. Read `references/brand-spec.md` for the palette (2–3 colors per slide max).
3. Pick a layout from `references/layout-index.md`, then read that section in `layout-library.md`.
4. Prefer **`slide_theme.py`** builders over hand-placed shapes.
5. Render previews and fix overflow before finishing.

## Density (ask or infer)

| Mode | Best for | Behavior |
|------|----------|----------|
| **Speaker-led** | Talks, pitches, live presenting | 1 idea/slide, large type, 1–3 bullets, more slides |
| **Reading-first** | Reports, handouts, async review | Denser grids/tables, 4–6 bullets or cards when readable |

If content exceeds the slide, **split slides** — never shrink text until unreadable.

## Core rules

- **16:9**, blank Title-Only layout, shapes placed manually or via helpers.
- **Palette:** blue-800 / blue-500 / indigo-500 + gray neutrals. See `brand-spec.md`.
- **Typography:** Segoe UI (fallback Arial). Title ~27pt, message bar 20pt, body 14pt.
- **Contrast:** use `text_on(fill)` — white on dark fills, `PRIMARY_DARK` on light fills.
- **Images:** real photos, screenshots, user uploads. No AI-generated imagery unless user explicitly allows.
- **Message bar:** optional but recommended — `add_message_bar()` with `ACCENT_LIGHT` or `PRIMARY_DARK` fill.

## Layout quick map

See `references/layout-index.md` for the full archetype table.

Common builders in `slide_theme.py`:

| Archetype | Builder |
|-----------|---------|
| Title / agenda / section | `presentation_title_slide`, `agenda_slide`, `section_title_slide` |
| Hero + icon rows | `left_image_icon_rows_slide` |
| Hero + category list | `left_image_tiered_list_slide` |
| Migration timeline | `migration_timeline_circles_slide` |
| GTM / activation timeline | `timeline_template_slide`, `add_activation_timeline` |
| Parallel cards | `add_cards_row` |
| Thank-you close | `closing_slide` (optional) |

## Self-check

After `python tools/preview.py output/deck.pptx output`:

- No text overflow or overlapping panels
- ≤3 colors per slide
- Readable contrast on every filled shape
- 16:9 proportions preserved

## References

| File | Purpose |
|------|---------|
| `references/brand-spec.md` | Colors, type, contrast |
| `references/layout-index.md` | Choose layout by content shape |
| `references/layout-library.md` | Layout anatomy |
| `references/pptx-implementation.md` | Code patterns |
| `references/special-slides.md` | Title, agenda, section slides |
