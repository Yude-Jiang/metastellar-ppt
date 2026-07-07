---
name: metastellar-slides
description: >
  Create premium marketing-agency pitch decks with the MetaStellar Digital Enterprise
  Deck System. Blue mono palette, Arial typography, KPI cards, § chrome, MetaStellar
  logo mark. Optimized for SaaS/consulting/agency client pitches.
---

# Metastellar Slides — Digital Enterprise Deck System

Build **16:9 PowerPoint (.pptx)** decks for **marketing agencies presenting to clients**.
Style: **dashboard-driven enterprise** — Arial, data UI, blue mono, `BRAND_DEEP` dark pages.

Read **`references/digital-enterprise-deck.md`** for the 20-page type system.
Read **`references/agency-pitch-playbook.md`** for pitch arc and copy tone.

## Workflow

1. Read `AGENTS.md` for the full build loop.
2. Read `references/brand-spec.md` for tokens and forbidden patterns.
3. Pick layout from `references/layout-index.md`.
4. Build with **`slide_theme.py`** — prefer agency builders below.
5. Every inner slide: `add_slide_header` + `add_slide_footer` (or use builders that include chrome).
6. Render previews and fix overflow before finishing.

## Primary builders (`slide_theme.py`)

| Moment | Builder |
|--------|---------|
| Opener / cover | `agency_cover_slide` |
| Agenda | `agenda_slide` |
| Section divider | `agency_section_slide` |
| Statement / manifesto | `big_idea_slide` |
| Data / KPIs | `metrics_3up_slide` + `kpi_card` |
| Challenge vs approach | `challenge_solution_slide` |
| Strategic pillars | `pillar_strategy_slide` |
| Campaign rollout | `campaign_timeline_slide` |
| Hero + proof rows | `left_image_icon_rows_slide` |
| Contact / close | `contact_slide`, `closing_slide` |

**Chrome primitives:** `add_wordmark`, `draw_metastellar_mark`, `add_slide_header`,
`add_slide_footer`, `kpi_card`, `text_on(fill)`.

Also available: `presentation_title_slide`, `section_title_slide`, `left_image_tiered_list_slide`,
`migration_timeline_circles_slide`, `add_cards_row`, `timeline_template_slide`, `add_message_bar`.

## Density

| Mode | Best for | Behavior |
|------|----------|----------|
| **Speaker-led** | Live pitch | 1 idea/slide, hero KPIs, § chrome, minimal bullets |
| **Reading-first** | Proposal PDF | Denser pillars/timelines; still premium |

## Core rules

- **16:9**, blank Title-Only layout.
- **Palette:** blue mono only (`brand-spec.md`). No indigo, no second hue.
- **Typography:** Arial + Consolas labels + Microsoft YaHei for 中文. **No italic.**
- **Dark bg:** `BRAND_DEEP` `#0F1E4A` only — never `#000`.
- **Chrome:** every inner slide needs `§` section pill + `NN / total` footer.
- **KPI cards:** tabular numbers; last card `featured` on data slides.
- **Contrast:** `text_on(fill)` always.
- **Story:** cover → agenda → divider → insight → data → plan → contact.

## Self-check

- No serif / italic / second hue
- Every slide has § id + sheet footer (except minimal covers if client-branded)
- KPI values large (44pt), mono labels UPPERCASE
- Dark slides use `BRAND_DEEP`, not `BRAND` or black
- Preview PNGs: no overflow, ≤3 colors per slide

## References

| File | Purpose |
|------|---------|
| `references/digital-enterprise-deck.md` | **20-page type system** |
| `references/agency-pitch-playbook.md` | Pitch arc, copy tone |
| `references/brand-spec.md` | Tokens, logo, typography |
| `references/layout-index.md` | Layout picker |
| `references/layout-library.md` | Layout anatomy |
| `references/pptx-implementation.md` | Code patterns |
| `references/special-slides.md` | Title, agenda, section |
