# Layout Index — pick by content shape

Read the matching section in `layout-library.md` after choosing.

| Content shape | Archetype | Builder |
|---------------|-----------|---------|
| Deck opener | presentation title | `presentation_title_slide` |
| Table of contents | agenda | `agenda_slide` |
| Section break | section title | `section_title_slide` |
| One story over a photo | app-photo-overlay | compose with `add_message_bar`, `bullet_box` |
| Product + 2–3 feature blocks | left-image-feature-boxes | `box`, `bullet_box` |
| Two options compared | product-comparison-2up | `box` × 2 columns |
| N parallel items (image + bullets) | cards-Nup | `add_cards_row` |
| Cards + bottom punchline | cards-Nup + message bar | `add_cards_row` + `add_message_bar` |
| Icon grid (4–6 items) | icon-cards-5up | `box` grid |
| 4 facets of one topic | quadrant-2x2-center-badge | compose |
| Image portfolio grid | image-grid-2x3-caption-bars | compose |
| Sequential process | process-flow-circles | `box` + `arrow` |
| Label rows → visual | row-label-table-visual | compose |
| Era / evolution timeline | timeline-era-cards | compose |
| Launch Gantt (organic/paid) | timeline-organic-paid-lanes | `arrow`, `box`, `label` |
| Activation / content plan | timeline-content-promotion-lanes | `timeline_template_slide` |
| Hero + icon statement rows | left-image-icon-rows | `left_image_icon_rows_slide` |
| Phased migration | migration-timeline-circles | `migration_timeline_circles_slide` |
| Hero + category bullets | left-image-tiered-list | `left_image_tiered_list_slide` |

## Density hints

**Speaker-led:** prefer `left-image-icon-rows`, `section_title_slide`, single `add_message_bar` + 3 bullets.

**Reading-first:** prefer `add_cards_row`, `timeline_template_slide`, `left_image_tiered_list_slide`.
