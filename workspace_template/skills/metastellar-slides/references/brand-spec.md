# MetaStellar Brand Spec — Digital Enterprise Deck System

**MetaStellar · 智元星启** — dashboard-driven enterprise aesthetic. Blue mono palette,
Arial typography, data UI as primary visual language.

## Design principles (non-negotiable)

1. **Single hue** — blue only; use lightness for hierarchy. No yellow, pink, green, orange, purple accents.
2. **Sans-serif only** — Arial + Noto Sans SC (Microsoft YaHei in pptx). No serifs, no italic.
3. **Dark surfaces** — `#0F1E4A` (`BRAND_DEEP`). Never pure black `#000`.
4. **Data UI** — KPI cards, badges, charts are structure, not decoration.
5. **Chrome on every slide** — `§` section pill, sheet id `NN / 20`, mono metadata.
6. **Bilingual** — English display, Chinese sub (smaller, lighter).

## Color tokens

| Token | Hex | Use |
|-------|-----|-----|
| `INK` | `#0B1220` | Headings |
| `INK_2` | `#1E293B` | Body strong |
| `INK_3` | `#475569` | Body |
| `INK_4` | `#94A3B8` | Muted / footer |
| `PAPER` | `#FFFFFF` | Main background |
| `PAPER_2` | `#F8FAFC` | Card background |
| `PAPER_3` | `#F1F5F9` | Recessed panels |
| `LINE` | `#E2E8F0` | Border default |
| `LINE_2` | `#CBD5E1` | Border strong |
| `BRAND` | `#1E40AF` | Primary — headings, buttons |
| `BRAND_2` | `#2563EB` | Interactive |
| `BRAND_3` | `#3B82F6` | Lighter interactive / CTA on dark |
| `BRAND_4` | `#60A5FA` | Soft blue |
| `BRAND_DEEP` | `#0F1E4A` | Dark slide background |
| `BRAND_PALE` | `#DBEAFE` | Pill borders |
| `BRAND_TINT` | `#EFF6FF` | Pill / badge background |
| `BRAND_GLOW` | `#93C5FD` | Text on dark surfaces |
| `OK` | `#10B981` | Live dots only — sparingly |

## Shading ramp (blue mono)

Darkest → lightest: `BRAND_DEEP` → `BRAND` → `BRAND_2` → `BRAND_3`

Use `RAMP` in `slide_theme.py` or `ramp_text(step)` for contrast-safe text.

## Logo mark

MetaStellar symbol = **twin elliptical orbits (±28°)** + **open triangle** (3 disconnected strokes).
Wordmark: **MetaStellar** / **智元星启**.

Draw with `draw_metastellar_mark()` / `add_wordmark()` in `slide_theme.py`.

## Typography (pptx)

| Role | Font | Size | Weight |
|------|------|------|--------|
| Cover headline | Arial | 36–40pt | Bold |
| Section title | Arial | 32–34pt | Bold |
| Big idea | Arial | 36pt | Bold |
| KPI value | Arial | 44pt | Bold, tabular-nums |
| Slide title | Arial | 26–27pt | Bold |
| Body | Arial | 13–14pt | Regular |
| Mono label | Consolas | 10–11pt | Medium, UPPERCASE, 0.14em tracking |
| Chinese sub | Microsoft YaHei | ~30% of EN | Regular |

**Forbidden:** italic, serif, second hue, emoji icons.

## Contrast

- **White text** on: `BRAND_DEEP`, `BRAND`, `BRAND_2`
- **BRAND text** on: `PAPER`, `PAPER_2`, `PAPER_3`, `BRAND_TINT`
- Use `text_on(fill_color)` always

## Per-slide limits

- **2–3 colors** per slide (excluding white/gray neutrals)
- Dark slides ~20–30% of deck (cover panel, dividers, contact)
- One visual anchor per slide (hero title, KPI row, or mockup)

## Forbidden (anti-patterns)

- Indigo / purple / multi-hue gradients
- Segoe UI as primary (legacy — use Arial)
- Slides without `§` section id or sheet footer
- Glassmorphism on white backgrounds
- Pie charts / 3D charts as hero visuals
