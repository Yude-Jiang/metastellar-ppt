---
name: metastellar-slides
description: >
  Create premium marketing-agency pitch decks and polished presentations with the
  Metastellar blue design system. Optimized for agencies presenting strategies,
  campaigns, and proposals to clients. Prefer agency layouts from slide_theme.py.
---

# Metastellar Slides

Build **16:9 PowerPoint (.pptx)** decks for **marketing agencies presenting to clients**.
Default aesthetic: **premium, editorial, confident** — large type, generous whitespace,
clear story arc (challenge → insight → strategy → plan → proof → ask).

Read **`references/agency-pitch-playbook.md`** first for deck structure and tone.

## Workflow

1. Read `AGENTS.md` for the full build loop.
2. Read `references/agency-pitch-playbook.md` for client-pitch positioning.
3. Read `references/brand-spec.md` for palette (2–3 colors per slide max).
4. Pick layout from `references/layout-index.md` (agency section prioritized).
5. Prefer **`slide_theme.py`** agency builders — see below.
6. Render previews and fix overflow before finishing.

## Agency-first builders (`slide_theme.py`)

| Moment | Builder |
|--------|---------|
| Pitch cover | `agency_cover_slide` |
| Section divider | `agency_section_slide` |
| North-star insight | `big_idea_slide` |
| Challenge vs approach | `challenge_solution_slide` |
| Strategic pillars | `pillar_strategy_slide` |
| KPI / results | `metrics_3up_slide` |
| Campaign rollout | `campaign_timeline_slide` |
| Hero + proof rows | `left_image_icon_rows_slide` |
| Close | `closing_slide` |

Also available: `presentation_title_slide`, `agenda_slide`, `section_title_slide`,
`left_image_tiered_list_slide`, `migration_timeline_circles_slide`, `add_cards_row`,
`timeline_template_slide`, `add_message_bar`, `text_on(fill)`.

## Density

| Mode | Best for | Agency behavior |
|------|----------|-----------------|
| **Speaker-led** | Live client pitch | Default for agency — 1 idea/slide, hero metrics, minimal bullets |
| **Reading-first** | Proposal PDF / async | Denser pillars and timelines; still premium, not cramped |

## Core rules

- **16:9**, blank Title-Only layout.
- **Palette:** blue-800 / blue-500 / indigo-500 + gray neutrals (`brand-spec.md`).
- **Typography:** Segoe UI. Agency pitch titles 26–40pt; KPI values 44pt.
- **Contrast:** `text_on(fill)` always.
- **Images:** uploads, screenshots, real photography — no AI images unless allowed.
- **Story:** follow playbook arc when structure not specified.

## Self-check

- No overflow / overlap
- ≤3 colors per slide
- Every slide passes the "client boardroom" test: would an agency partner show this as-is?

## References

| File | Purpose |
|------|---------|
| `references/agency-pitch-playbook.md` | **Start here** — pitch arc, tone, typography |
| `references/brand-spec.md` | Colors, contrast |
| `references/layout-index.md` | Layout picker (agency section) |
| `references/layout-library.md` | Layout anatomy |
| `references/pptx-implementation.md` | Code patterns |
| `references/special-slides.md` | Title, agenda, section slides |
