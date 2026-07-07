# Layout Index — Digital Enterprise Deck System

**Agency client pitch?** Start with agency section, then `digital-enterprise-deck.md`.

## Agency pitch (client-facing) — prefer these

| Client moment | Page type | Builder |
|---------------|-----------|---------|
| Opener / cover | 01 Opener | `agency_cover_slide` |
| Agenda | 06 Agenda | `agenda_slide` |
| Section divider | 07 Divider | `agency_section_slide` |
| North-star / manifesto | 08 Statement | `big_idea_slide` |
| Challenge vs our approach | — | `challenge_solution_slide` |
| Strategy pillars (3–4) | 10 Services | `pillar_strategy_slide` |
| KPI / projected results | 09 Data | `metrics_3up_slide` |
| Campaign / rollout plan | 14 Timeline | `campaign_timeline_slide` |
| Creative + proof points | 11 Case | `left_image_icon_rows_slide` |
| Contact / thank you | 20 Contact | `contact_slide`, `closing_slide` |

## Chrome helpers (use on custom slides)

| Need | Function |
|------|----------|
| Logo lockup | `add_wordmark` |
| § header + rhs meta | `add_slide_header` |
| Sheet footer | `add_slide_footer` |
| KPI tile | `kpi_card` |
| Brand symbol only | `draw_metastellar_mark` |

## General layouts

| Content shape | Archetype | Builder |
|---------------|-----------|---------|
| Deck opener (simple) | presentation title | `presentation_title_slide` |
| Section break | section title | `section_title_slide` |
| N parallel items | cards-Nup | `add_cards_row` |
| Launch Gantt | timeline lanes | `timeline_template_slide` |
| Hero + category bullets | tiered list | `left_image_tiered_list_slide` |
| Phased migration | timeline circles | `migration_timeline_circles_slide` |

## Density hints

**Speaker-led:** `agency_cover_slide`, `big_idea_slide`, `metrics_3up_slide` — one hero per slide.

**Reading-first:** denser `pillar_strategy_slide`, `add_cards_row`, `campaign_timeline_slide`.
