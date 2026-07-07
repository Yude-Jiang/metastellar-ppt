# Digital Enterprise Deck System — Page Types

> **MetaStellar default:** use **`seo-geo-deck.md`** (24-page SEO/GEO deck). This file is the generic 20-page fallback.

20-page pitch deck sequence. Each slide maps to `slide_theme.py` builders.

| # | Page type | Key components | Builder |
|---|-----------|----------------|---------|
| 01 | Opener | Left hero + right metric panel on `BRAND_DEEP` | `agency_cover_slide` |
| 02–05 | Cover variants | Enterprise / dark / split / launch | `agency_cover_slide` (params) |
| 06 | Agenda | Left hero + § numbered rows | `agenda_slide` |
| 07 | Section divider | `BRAND_DEEP` + § + oversized index | `agency_section_slide` |
| 08 | Statement | Single quote + § chrome | `big_idea_slide` |
| 09 | Data / KPIs | 3–4 KPI cards, 1 `.featured` | `metrics_3up_slide` |
| 10 | Services | 4×2 svc-card grid + DNA icons | `add_cards_row`, `pillar_strategy_slide` |
| 11 | Case study | Left dark dashboard + right copy | `left_image_tiered_list_slide` |
| 12 | Team | 4 team cards | `add_cards_row` |
| 13 | Clients | Logo grid | custom / `add_cards_row` |
| 14 | Timeline | Phase cards + track bar | `campaign_timeline_slide` |
| 15 | Proposal / pricing | 3 tier cards | `pillar_strategy_slide` |
| 16–17 | KV system / poster | SVG graphic modules | manual shapes |
| 18 | Applications | Social / dashboard / card mockups | custom |
| 19 | Directions recap | Cover thumbnails | custom |
| 20 | Contact | Dark + CTA + contact rows | `contact_slide` / `closing_slide` |

## Minimum viable pitch skeleton

`01 Opener` → `06 Agenda` → `07 Divider` → `08 Statement` → `09 Data` → `15 Proposal` → `20 Contact`

## Chrome (required on inner slides)

```
┌─ [logo] MetaStellar · v1.0          [pill] SHEET 06 / 20 ─┐
│  § 02 / INSIGHT · Section title                            │
│                    (content)                                │
└─ © 2026 MetaStellar                               06 / 20 ─┘
```

Use `add_slide_header()`, `add_slide_footer()`, `add_wordmark()`.

## KPI card anatomy

```
┌─────────────────────────────┐
│ METRIC NAME · 中文    [↑18%] │
│                             │
│ 92.4/100                    │
│ Description · EN subtitle   │
└─────────────────────────────┘
```

Last card in a row of 3–4 uses `featured=True` (`BRAND_DEEP` fill).

## Key visual modules (12 SVG concepts)

Signal Ring · Star Orbit (MetaStellar mark) · Crosshair · Data Grid · Waveform ·
Trend Up · Chart Bar · Node Map · Radar Plot · Terminal · Signal Gauge · Vector Path

All strokes `#1E40AF` — single hue only.
