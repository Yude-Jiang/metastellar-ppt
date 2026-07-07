---
name: metastellar-slides
description: >
  Create SEO/GEO marketing agency pitch decks for MetaStellar 智元星启. Blue mono
  palette, Arial typography, 24-page deck with AI Search / GEO specialty slides.
---

# Metastellar Slides — SEO/GEO Agency Deck

Build **16:9 PowerPoint (.pptx)** for **MetaStellar SEO · GEO · Campaign · Strategy** client pitches.

Read **`references/seo-geo-deck.md`** for the 24-page structure.
Read **`references/agency-pitch-playbook.md`** for pitch arc and copy.

## Workflow

1. Read `AGENTS.md` for the build loop.
2. Read `references/brand-spec.md` for tokens.
3. Pick layouts from `references/layout-index.md`.
4. Build with **`slide_theme.py`** — use SEO/GEO builders below.
5. Every inner slide: § chrome + `NN / 24` footer.
6. Render previews; fix overflow before finishing.

## SEO/GEO builders (`slide_theme.py`)

| # | Slide | Builder |
|---|-------|---------|
| 01 | Opener | `agency_cover_slide` |
| 06 | Agenda | `agenda_slide` |
| 07 | Divider | `agency_section_slide` |
| 08 | Manifesto | `big_idea_slide` |
| 09 | Industry KPIs | `seo_geo_data_slide` |
| 10 | AI Search Landscape | `ai_search_landscape_slide` |
| 11 | GEO Explained | `geo_explained_slide` |
| 12 | SEO vs GEO | `seo_vs_geo_slide` |
| 13 | Methodology | `methodology_slide` |
| 14 | Services 4-up | `services_4up_slide` |
| 19 | Proposal tiers | `proposal_tiers_slide` |
| 24 | Contact | `contact_slide` |

**Also:** `metrics_3up_slide`, `kpi_card`, `challenge_solution_slide`, `campaign_timeline_slide`,
`left_image_tiered_list_slide`, `add_slide_header`, `add_slide_footer`, `add_wordmark`.

## Defaults (use unless user overrides)

```python
from slide_theme import (
    SEO_GEO_TAGLINE, SEO_GEO_MANIFESTO, SEO_GEO_CONTACT, DEFAULT_TOTAL
)
```

- Tagline: `The new science of visibility.`
- Manifesto: `If you can't be found, you don't exist.`
- Contact: `Let's make you findable.`
- Total pages: **24**

## Core rules

- Blue mono only — no indigo, no second hue, no italic
- `BRAND_DEEP` `#0F1E4A` for dark surfaces
- Arial + Consolas + Microsoft YaHei
- GEO service card / middle proposal tier = **featured** (dark anchor)
- Realistic search-industry metrics (CTR, citations, queries)

## References

| File | Purpose |
|------|---------|
| `references/seo-geo-deck.md` | **24-page SEO/GEO system** |
| `references/digital-enterprise-deck.md` | Generic page types (fallback) |
| `references/agency-pitch-playbook.md` | Pitch arc, copy |
| `references/brand-spec.md` | Tokens, logo |
