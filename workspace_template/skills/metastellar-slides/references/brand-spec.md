# Metastellar Brand Spec — Colors & Typography

## Primary palette (blue system)

| Role | Name | Hex | RGB | Use |
|------|------|-----|-----|-----|
| Title / dark fill | blue-800 | `#1E40AF` | 30, 64, 175 | Titles, dark message bars, primary boxes |
| Emphasis | blue-600 | `#2563EB` | 37, 99, 235 | Hover states, secondary headers |
| Primary | blue-500 | `#3B82F6` | 59, 130, 246 | Message bars, links, icons |
| Accent | indigo-500 | `#6366F1` | 99, 102, 241 | Tiles, numbered badges, highlights |
| Accent deep | indigo-600 | `#4F46E5` | 79, 70, 229 | Gradient end, emphasis bars |
| Light bg | blue-50 | `#EFF6FF` | 239, 246, 255 | Subtle panels |
| Light border | blue-100 | `#DBEAFE` | 219, 234, 254 | Borders, selected states |

## Success (optional, 1 accent per deck)

| green-500 | `#22C55E` | Success callouts, completion states |
| emerald-500 | `#10B981` | Step-complete markers |

## Neutrals

| white | `#FFFFFF` | Card backgrounds |
| gray-50 | `#F9FAFB` | Page/slide background feel |
| gray-100 | `#F3F4F6` | Bullet boxes, light panels |
| gray-200 | `#E5E7EB` | Borders |
| gray-300 | `#D1D5DB` | Placeholders |
| gray-600 | `#4B5563` | Body text secondary |
| gray-800 | `#1F2937` | Body text primary |

## Shading ramp (graded headers / process steps)

Darkest → lightest: `#1E40AF` → `#2563EB` → `#3B82F6` → `#DBEAFE`

Use `RAMP` in `slide_theme.py` or `ramp_text(step)` for contrast-safe text.

## Typography

- **Font:** Segoe UI (PowerPoint-safe modern sans). Arial acceptable fallback only.
- **Title:** 27pt bold, `PRIMARY_DARK` on light slides / white on dark slides
- **Message bar:** 20pt bold
- **Body:** 14pt (12pt min, 20pt max for inline emphasis)

## Contrast rules

- **White text** on: blue-800, blue-600, indigo-600, indigo-500 (dark fills)
- **PRIMARY_DARK text** on: white, gray-100, blue-50, blue-100
- **Never** white text on gray-100, blue-50, or indigo-500 at small sizes without checking preview
- Use `text_on(fill_color)` in `slide_theme.py`

## Per-slide limits

- **2–3 colors maximum** per slide (excluding white/gray neutrals)
- Large areas use primary blues or gray-100 panels
- One accent color (indigo or green) per slide at most
