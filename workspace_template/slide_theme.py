"""Metastellar slide theme library for python-pptx.

Encodes the rules from skills/metastellar-slides (palette, typography, message bar,
Title-Only content slides, card rows, and diagram primitives) so generated decks
are on-brand by construction. Import this from the deck-build script.
"""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import MSO_AUTO_SIZE, PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.oxml.ns import qn

# ---- Metastellar palette (Tailwind blue system) ----
BLUE_500      = RGBColor(0x3B, 0x82, 0xF6)   # primary / links
BLUE_600      = RGBColor(0x25, 0x6E, 0xEB)   # emphasis / hover
INDIGO_500    = RGBColor(0x63, 0x66, 0xF1)   # accent tiles
INDIGO_600    = RGBColor(0x4F, 0x46, 0xE5)   # gradient end
BLUE_50       = RGBColor(0xEF, 0xF6, 0xFF)   # light background
BLUE_100      = RGBColor(0xDB, 0xEA, 0xFE)   # borders / selected
BLUE_800      = RGBColor(0x1E, 0x40, 0xAF)   # title / dark fills
GREEN_500     = RGBColor(0x22, 0xC5, 0x5E)   # success
WHITE         = RGBColor(0xFF, 0xFF, 0xFF)
GRAY_50       = RGBColor(0xF9, 0xFA, 0xFB)
GRAY_100      = RGBColor(0xF3, 0xF4, 0xF6)
GRAY_200      = RGBColor(0xE5, 0xE7, 0xEB)
GRAY_300      = RGBColor(0xD1, 0xD5, 0xDB)
GRAY_600      = RGBColor(0x4B, 0x55, 0x63)
GRAY_800      = RGBColor(0x1F, 0x29, 0x37)
# Semantic aliases
PRIMARY_DARK  = BLUE_800
ACCENT        = INDIGO_500
ACCENT_LIGHT  = BLUE_500
GRAY_1        = GRAY_100
GRAY_2        = GRAY_200
GRAY_3        = GRAY_300
SLATE         = BLUE_600
RAMP = [BLUE_800, BLUE_600, BLUE_500, BLUE_100]

FONT = "Segoe UI"
SLIDE_W = 13.333
SLIDE_H = 7.5


# Dark fills: white text. Light fills: PRIMARY_DARK text.
_DARK_FILLS = frozenset({BLUE_800, BLUE_600, INDIGO_600})


def ramp_text(step):
    return text_on(RAMP[min(step, 3)])


def text_on(fill_color):
    """Mandatory contrast: white on dark fills; PRIMARY_DARK on light fills."""
    if fill_color in _DARK_FILLS:
        return WHITE
    return BLUE_800


BODY_SIZE = 14   # prefer 14 pt per brand spec (12 min, 20 max)
TITLE_SIZE = 27
MSG_BAR_SIZE = 20


def new_deck():
    """16:9 presentation 16:9 widescreen geometry."""
    prs = Presentation()
    prs.slide_width = Inches(SLIDE_W)
    prs.slide_height = Inches(SLIDE_H)
    return prs


def title_only_slide(prs):
    """Reproduce the 'Title Only' layout: blank slide; place shapes yourself."""
    return prs.slides.add_slide(prs.slide_layouts[6])


def _slide_bg(slide, color):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color


def _place_logo(slide, logo_path, left, top, height=0.48):
    if logo_path:
        slide.shapes.add_picture(logo_path, Inches(left), Inches(top), height=Inches(height))


def presentation_title_slide(prs, title, presenter=None, logo_path=None):
    """Main / presentation title — navy field, left accent bar, white title (see special-slides.md)."""
    slide = title_only_slide(prs)
    _slide_bg(slide, BLUE_800)
    accent = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0),
                                    Inches(0.14), Inches(SLIDE_H))
    fill(accent, ACCENT)
    tb = slide.shapes.add_textbox(Inches(1.1), Inches(2.55), Inches(9.5), Inches(1.15))
    tf = tb.text_frame
    no_autofit(tf)
    tf.text = title
    _style(tf, WHITE, 36, bold=True, align=PP_ALIGN.LEFT)
    if presenter:
        ptb = slide.shapes.add_textbox(Inches(1.1), Inches(3.85), Inches(8.0), Inches(0.55))
        ptf = ptb.text_frame
        no_autofit(ptf)
        ptf.text = presenter
        _style(ptf, WHITE, 18, bold=False, align=PP_ALIGN.LEFT)
    _place_logo(slide, logo_path, 11.35, 0.38, height=0.5)
    return slide


def agenda_slide(prs, topics, title="Agenda", logo_path=None, columns=2):
    """Agenda / table of contents — white field, accent numbered tiles (see special-slides.md)."""
    slide = title_only_slide(prs)
    _slide_bg(slide, WHITE)
    tb = slide.shapes.add_textbox(Inches(9.6), Inches(0.32), Inches(3.4), Inches(0.9))
    tf = tb.text_frame
    no_autofit(tf)
    tf.text = title
    tf.paragraphs[0].alignment = PP_ALIGN.RIGHT
    _style(tf, BLUE_800, 32, bold=True, align=PP_ALIGN.RIGHT)
    n = len(topics)
    cols = max(1, min(columns, 2))
    rows = (n + cols - 1) // cols
    col_x = [1.35, 7.05]
    row_y0 = 1.55
    row_gap = 1.05
    tile = 0.42
    for i, topic in enumerate(topics):
        col = i // rows if rows else 0
        row = i % rows if rows else 0
        if col >= cols:
            col = cols - 1
        x = col_x[col]
        y = row_y0 + row * row_gap
        sq = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y),
                                    Inches(tile), Inches(tile))
        fill(sq, ACCENT)
        stf = sq.text_frame
        no_autofit(stf)
        stf.vertical_anchor = MSO_ANCHOR.MIDDLE
        stf.text = str(i + 1)
        for p in stf.paragraphs:
            p.alignment = PP_ALIGN.CENTER
        _style(stf, BLUE_800, 14, bold=True, align=PP_ALIGN.CENTER)
        label = slide.shapes.add_textbox(Inches(x + tile + 0.18), Inches(y + 0.06),
                                         Inches(4.8), Inches(0.38))
        ltf = label.text_frame
        no_autofit(ltf)
        ltf.vertical_anchor = MSO_ANCHOR.MIDDLE
        ltf.text = topic
        _style(ltf, BLUE_800, 14, bold=False, align=PP_ALIGN.LEFT)
    _place_logo(slide, logo_path, 0.45, 6.55, height=0.42)
    return slide


def section_title_slide(prs, title, image_path=None, logo_path=None):
    """Section break — navy field, top accent bar, optional hero image (see special-slides.md)."""
    slide = title_only_slide(prs)
    _slide_bg(slide, BLUE_800)
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(3.35), Inches(0),
                                 Inches(SLIDE_W - 3.35), Inches(1.15))
    fill(bar, ACCENT)
    tf = bar.text_frame
    no_autofit(tf)
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.margin_left = Inches(0.35)
    tf.text = title
    _style(tf, BLUE_800, 30, bold=True, align=PP_ALIGN.LEFT)
    if image_path:
        slide.shapes.add_picture(image_path, Inches(2.2), Inches(1.65),
                                 width=Inches(8.9), height=Inches(4.35))
    rule = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.45), Inches(6.72),
                                  Inches(12.4), Inches(0.02))
    fill(rule, GRAY_3)
    _place_logo(slide, logo_path, 0.45, 6.85, height=0.38)
    return slide


def _place_image_or_placeholder(slide, image_path, x, y, w, h, label="Image"):
    """Use a real provided image when available; otherwise leave a gray placeholder."""
    if image_path:
        slide.shapes.add_picture(image_path, Inches(x), Inches(y),
                                 width=Inches(w), height=Inches(h))
        return None
    ph = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y),
                                Inches(w), Inches(h))
    fill(ph, GRAY_2)
    ph.line.color.rgb = GRAY_3
    ph.line.width = Pt(1)
    tf = ph.text_frame
    no_autofit(tf)
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.text = label
    for p in tf.paragraphs:
        p.alignment = PP_ALIGN.CENTER
    _style(tf, BLUE_800, 11, bold=False, align=PP_ALIGN.CENTER)
    return ph


def left_image_icon_rows_slide(
    prs,
    title,
    rows,
    punchline=None,
    img_path=None,
    logo_path=None,
    img_placeholder="Image",
):
    """Left hero image + accent icon tiles + gray statement rows (see layout-library #14)."""
    slide = title_only_slide(prs)
    corner_accent(slide)
    img_w = 4.15
    _place_image_or_placeholder(slide, img_path, 0, 0, img_w, SLIDE_H, label=img_placeholder)
    _place_logo(slide, logo_path, 0.45, 6.55, height=0.4)
    rx = img_w + 0.35
    rw = SLIDE_W - rx - 0.35
    tb = slide.shapes.add_textbox(Inches(rx), Inches(0.32), Inches(rw), Inches(0.7))
    tf = tb.text_frame
    no_autofit(tf)
    tf.text = title
    tf.paragraphs[0].alignment = PP_ALIGN.LEFT
    _style(tf, BLUE_800, 26, bold=True, align=PP_ALIGN.LEFT)
    row_h = 0.52
    gap = 0.14
    y0 = 1.25
    tile = 0.48
    for i, row in enumerate(rows):
        y = y0 + i * (row_h + gap)
        sq = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(rx), Inches(y),
                                    Inches(tile), Inches(row_h))
        fill(sq, ACCENT)
        icon = row.get("icon_path")
        if icon:
            slide.shapes.add_picture(icon, Inches(rx + 0.06), Inches(y + 0.06),
                                     width=Inches(tile - 0.12), height=Inches(row_h - 0.12))
        bar_x = rx + tile + 0.12
        bar_w = rw - tile - 0.12
        box(slide, bar_x, y, bar_w, row_h, row.get("text", ""), GRAY_1,
            BLUE_800, size=13, bold=False, align=PP_ALIGN.LEFT)
    if punchline:
        ptb = slide.shapes.add_textbox(Inches(rx), Inches(5.85), Inches(rw), Inches(1.2))
        ptf = ptb.text_frame
        no_autofit(ptf)
        ptf.word_wrap = True
        ptf.text = punchline
        _style(ptf, BLUE_800, 22, bold=True, align=PP_ALIGN.LEFT)
    return slide


def left_image_tiered_list_slide(
    prs,
    title,
    message,
    categories,
    img_path=None,
    logo_path=None,
    img_placeholder="Image",
):
    """Left hero + overlapping navy message bar + accent/gray category rows (layout-library #16)."""
    slide = title_only_slide(prs)
    corner_accent(slide)
    img_w = 5.05
    img_top = 1.35
    img_h = 5.95
    _place_image_or_placeholder(slide, img_path, 0, img_top, img_w, img_h, label=img_placeholder)
    _place_logo(slide, logo_path, 0.45, 6.55, height=0.38)
    rx = img_w + 0.25
    rw = SLIDE_W - rx - 0.35
    tb = slide.shapes.add_textbox(Inches(rx), Inches(0.28), Inches(rw), Inches(0.65))
    tf = tb.text_frame
    no_autofit(tf)
    tf.text = title
    tf.paragraphs[0].alignment = PP_ALIGN.LEFT
    _style(tf, BLUE_800, 24, bold=True, align=PP_ALIGN.LEFT)
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.35), Inches(0.88),
                                 Inches(10.2), Inches(0.78))
    fill(bar, BLUE_800)
    btf = bar.text_frame
    no_autofit(btf)
    btf.vertical_anchor = MSO_ANCHOR.MIDDLE
    btf.margin_left = Inches(0.25)
    btf.margin_right = Inches(0.25)
    btf.text = message
    _style(btf, WHITE, 16, bold=True, align=PP_ALIGN.LEFT)
    y = 1.45
    head_w = 1.05
    gap = 0.12
    for cat in categories:
        body_h = max(0.95, 0.28 + 0.22 * len(cat.get("bullets", [])))
        box(slide, rx, y, head_w, body_h, cat.get("title", ""), ACCENT,
            BLUE_800, size=13, bold=True, align=PP_ALIGN.LEFT)
        bullet_box(slide, rx + head_w + gap, y, rw - head_w - gap, body_h,
                   cat.get("bullets", []), shade=GRAY_1, size=12)
        y += body_h + gap
    return slide


def migration_timeline_circles_slide(
    prs,
    title,
    subtitle=None,
    steps=None,
    logo_path=None,
):
    """Wave timeline with alternating circles + accent callout markers (layout-library #15)."""
    slide = title_only_slide(prs)
    corner_accent(slide)
    steps = steps or []
    tb = slide.shapes.add_textbox(Inches(7.8), Inches(0.28), Inches(5.2), Inches(0.95))
    tf = tb.text_frame
    no_autofit(tf)
    tf.text = title
    tf.paragraphs[0].alignment = PP_ALIGN.RIGHT
    _style(tf, BLUE_800, 26, bold=True, align=PP_ALIGN.RIGHT)
    if subtitle:
        p = tf.add_paragraph()
        p.text = subtitle
        p.alignment = PP_ALIGN.RIGHT
        for r in p.runs:
            r.font.name = FONT
            r.font.size = Pt(18)
            r.font.color.rgb = BLUE_800
    n = len(steps)
    if not n:
        return slide
    d = 1.75
    x0 = 0.75
    span = SLIDE_W - 1.5
    gap = (span - d * n) / (n - 1) if n > 1 else 0
    cy = 3.55
    arrow(slide, x0, cy, x0 + span, cy, color=BLUE_800, width=1.2, dashed=True)
    for i, step in enumerate(steps):
        x = x0 + i * (d + gap)
        col = BLUE_800 if i % 2 == 0 else RAMP[2]
        tc = text_on(col)
        circ = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x), Inches(cy - d / 2),
                                      Inches(d), Inches(d))
        fill(circ, col)
        ctf = circ.text_frame
        no_autofit(ctf)
        ctf.vertical_anchor = MSO_ANCHOR.MIDDLE
        ctf.word_wrap = True
        ctf.text = step.get("label", "")
        for p in ctf.paragraphs:
            p.alignment = PP_ALIGN.CENTER
        _style(ctf, tc, 11, bold=True, align=PP_ALIGN.CENTER)
        callout = step.get("callout")
        if callout:
            above = step.get("callout_pos", "above") != "below"
            my = cy - d / 2 - 0.55 if above else cy + d / 2 + 0.18
            dot = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x + d / 2 - 0.03),
                                         Inches(my - 0.18 if above else cy + d / 2),
                                         Inches(0.06), Inches(0.28 if above else 0.22))
            fill(dot, ACCENT)
            label(slide, x + d / 2 - 1.35, my - 0.15 if above else my,
                  2.7, callout, size=10, bold=False, align=PP_ALIGN.CENTER)
    _place_logo(slide, logo_path, 0.45, 6.55, height=0.38)
    return slide


def fill(shape, color):
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()


def no_autofit(tf):
    tf.word_wrap = True
    tf.auto_size = MSO_AUTO_SIZE.NONE


def _style(tf, color, size_pt, bold=False, font=FONT, align=None):
    for p in tf.paragraphs:
        if align is not None:
            p.alignment = align
        for r in p.runs:
            r.font.name = font
            r.font.size = Pt(size_pt)
            r.font.bold = bold
            r.font.color.rgb = color


def corner_accent(slide):
    """Thin accent block, top-right (template accent)."""
    a = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(12.55), Inches(0.0),
                               Inches(0.78), Inches(0.34))
    fill(a, BLUE_800)
    return a


def add_title(slide, text, subtitle=None, align=PP_ALIGN.RIGHT, size=27):
    tb = slide.shapes.add_textbox(Inches(1.0), Inches(0.28), Inches(12.1), Inches(0.95))
    tf = tb.text_frame
    no_autofit(tf)
    tf.text = text
    tf.paragraphs[0].alignment = align
    _style(tf, BLUE_800, size, bold=True)
    if subtitle:
        p = tf.add_paragraph()
        p.text = subtitle
        p.alignment = align
        for r in p.runs:
            r.font.name = FONT
            r.font.size = Pt(13)
            r.font.color.rgb = ACCENT_LIGHT
    return tb


def add_message_bar(slide, text, fill_color=ACCENT_LIGHT):
    """The key message bar. 20pt Segoe UI; use theme palette fills only."""
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(1.43),
                                 Inches(9.8), Inches(0.84))
    fill(bar, fill_color)
    tf = bar.text_frame
    no_autofit(tf)
    tf.margin_left = Inches(0.3)
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.text = text
    txt = text_on(fill_color)
    _style(tf, txt, MSG_BAR_SIZE, bold=True)
    return bar


def box(slide, x, y, w, h, text, fill_color, text_color=None, size=BODY_SIZE, bold=True,
        align=PP_ALIGN.CENTER, sub=None, sub_size=12):
    """A rectangle with embedded text. text_color defaults to text_on(fill)."""
    if text_color is None:
        text_color = text_on(fill_color)
    sh = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y),
                                Inches(w), Inches(h))
    fill(sh, fill_color)
    tf = sh.text_frame
    no_autofit(tf)
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.margin_left = Inches(0.08)
    tf.margin_right = Inches(0.08)
    tf.margin_top = Inches(0.03)
    tf.margin_bottom = Inches(0.03)
    tf.text = text
    p0 = tf.paragraphs[0]
    p0.alignment = align
    for r in p0.runs:
        r.font.name = FONT
        r.font.size = Pt(size)
        r.font.bold = bold
        r.font.color.rgb = text_color
    if sub:
        p = tf.add_paragraph()
        p.text = sub
        p.alignment = align
        for r in p.runs:
            r.font.name = FONT
            r.font.size = Pt(sub_size)
            r.font.color.rgb = text_color
    return sh


def bullet_box(slide, x, y, w, h, bullets, shade=GRAY_1, size=BODY_SIZE, heading=None):
    sh = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y),
                                Inches(w), Inches(h))
    fill(sh, shade)
    tf = sh.text_frame
    no_autofit(tf)
    tf.vertical_anchor = MSO_ANCHOR.TOP
    tf.margin_left = Inches(0.16)
    tf.margin_top = Inches(0.12)
    tf.margin_right = Inches(0.14)
    first = True
    if heading:
        tf.text = heading
        tf.paragraphs[0].alignment = PP_ALIGN.LEFT
        for r in tf.paragraphs[0].runs:
            r.font.name = FONT
            r.font.size = Pt(size + 2)
            r.font.bold = True
            r.font.color.rgb = BLUE_800
        first = False
    for b in bullets:
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.text = "\u2022 " + b
        p.alignment = PP_ALIGN.LEFT
        p.space_after = Pt(4)
        for r in p.runs:
            r.font.name = FONT
            r.font.size = Pt(size)
            r.font.color.rgb = BLUE_800
    return sh


def label(slide, x, y, w, text, color=BLUE_800, size=11, bold=True,
          align=PP_ALIGN.LEFT):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(0.3))
    tf = tb.text_frame
    no_autofit(tf)
    tf.margin_left = Inches(0.02)
    tf.margin_top = Inches(0)
    tf.text = text
    tf.paragraphs[0].alignment = align
    for r in tf.paragraphs[0].runs:
        r.font.name = FONT
        r.font.size = Pt(size)
        r.font.bold = bold
        r.font.color.rgb = color
    return tb


def arrow(slide, x1, y1, x2, y2, color=BLUE_800, width=2.25, dashed=False):
    c = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1),
                                   Inches(x2), Inches(y2))
    c.line.color.rgb = color
    c.line.width = Pt(width)
    ln = c.line._get_or_add_ln()
    ln.append(ln.makeelement(qn('a:tailEnd'),
                             {'type': 'triangle', 'w': 'med', 'len': 'med'}))
    if dashed:
        ln.insert(0, ln.makeelement(qn('a:prstDash'), {'val': 'dash'}))
    return c


def dashed_container(slide, x, y, w, h, color=SLATE):
    sh = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y),
                                Inches(w), Inches(h))
    sh.fill.background()
    sh.line.color.rgb = color
    sh.line.width = Pt(1.5)
    ln = sh.line._get_or_add_ln()
    ln.append(ln.makeelement(qn('a:prstDash'), {'val': 'dash'}))
    sh.shadow.inherit = False
    return sh


def add_activation_timeline(
    slide,
    checkpoints,
    top_items=None,
    bottom_items=None,
    x0=0.55,
    x1=12.8,
    y_line=3.95,
):
    """Draw a 2-lane activation timeline similar to GTM launch plans.

    checkpoints: [{"x": 2.4, "label": "Mar 5"}, ...]
    top_items / bottom_items:
      [{"x": 2.6, "title": "Milestone", "note": "optional", "w": 2.0, "color": ACCENT}, ...]
    """
    top_items = top_items or []
    bottom_items = bottom_items or []

    # Main axis
    arrow(slide, x0, y_line, x1, y_line, color=BLUE_800, width=2.2)

    # Lane labels
    box(slide, 0.0, y_line - 1.55, 0.42, 1.42, "CONTENT", BLUE_800, WHITE, size=10)
    box(slide, 0.0, y_line + 0.15, 0.42, 1.42, "PROMO", BLUE_800, WHITE, size=10)

    # Checkpoints on axis
    for cp in checkpoints:
        x = cp["x"]
        dot = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x - 0.08), Inches(y_line - 0.08),
                                     Inches(0.16), Inches(0.16))
        fill(dot, WHITE)
        dot.line.color.rgb = BLUE_800
        dot.line.width = Pt(1.5)
        if cp.get("label"):
            label(slide, x - 0.35, y_line - 0.42, 0.8, cp["label"], color=BLUE_800,
                  size=10, bold=False, align=PP_ALIGN.CENTER)

    # Activity cards above axis
    for i, item in enumerate(top_items):
        w = item.get("w", 2.0)
        h = 0.5 if not item.get("note") else 0.82
        y = y_line - 1.2 - (0.62 * (i % 2))
        fc = item.get("color", ACCENT)
        tc = text_on(fc)
        box(slide, item["x"] - w / 2, y, w, h, item["title"], fc, tc, size=11,
            align=PP_ALIGN.LEFT, sub=item.get("note"), sub_size=10)
        arrow(slide, item["x"], y + h, item["x"], y_line - 0.12, color=GRAY_3, width=1.2)

    # Activity cards below axis
    for i, item in enumerate(bottom_items):
        w = item.get("w", 2.0)
        h = 0.5 if not item.get("note") else 0.82
        y = y_line + 0.26 + (0.62 * (i % 2))
        fc = item.get("color", GRAY_1)
        tc = text_on(fc)
        box(slide, item["x"] - w / 2, y, w, h, item["title"], fc, tc, size=11,
            align=PP_ALIGN.LEFT, sub=item.get("note"), sub_size=10)
        arrow(slide, item["x"], y, item["x"], y_line + 0.12, color=GRAY_3, width=1.2)


def timeline_template_slide(prs, title, message, checkpoints, top_items=None, bottom_items=None):
    """One-call template: title + message bar + 2-lane timeline."""
    slide = title_only_slide(prs)
    corner_accent(slide)
    add_title(slide, title, align=PP_ALIGN.RIGHT, size=TITLE_SIZE + 2)
    add_message_bar(slide, message, fill_color=ACCENT_LIGHT)
    add_activation_timeline(slide, checkpoints, top_items=top_items, bottom_items=bottom_items)
    return slide


def add_cards_row(slide, cards, top=2.5, bottom=6.95, gap=0.4, left_margin=0.45,
                  header="accent", img_ratio=2.35):
    """cards = [{"title", "bullets":[...], "img": path|None}].
    header = 'accent' (indigo accent bar) or 'ramp' (graded blue ramp).
    Lays out N equal cards: header bar + optional image banner + gray bullet box.
    """
    from PIL import Image
    n = len(cards)
    total_w = SLIDE_W - 2 * left_margin
    w = (total_w - gap * (n - 1)) / n
    head_h = 0.5
    img_top = top + head_h + 0.08
    img_h = w / img_ratio
    box_top = img_top + img_h + 0.08
    for i, c in enumerate(cards):
        x = left_margin + i * (w + gap)
        if header == "accent":
            hf, ht = ACCENT, BLUE_800
        else:
            hf, ht = RAMP[min(i, 3)], text_on(RAMP[min(i, 3)])
        box(slide, x, top, w, head_h, c["title"], hf, ht, size=BODY_SIZE,
            align=PP_ALIGN.LEFT)
        bt = box_top
        img = c.get("img")
        if img:
            # crop to a clean banner, then place with locked aspect ratio
            im = Image.open(img)
            iw, ih = im.size
            crop_h = min(ih, int(iw / img_ratio))
            cropped = img + ".banner.png"
            im.crop((0, 0, iw, crop_h)).save(cropped)
            slide.shapes.add_picture(cropped, Inches(x), Inches(img_top),
                                     width=Inches(w), height=Inches(img_h))
        else:
            bt = top + head_h
        bullet_box(slide, x, bt, w, top + (bottom - top) - bt,
                   c.get("bullets", []))


def footer(slide, text):
    tb = slide.shapes.add_textbox(Inches(0.45), Inches(7.12), Inches(12.4), Inches(0.32))
    tf = tb.text_frame
    no_autofit(tf)
    tf.text = text
    for r in tf.paragraphs[0].runs:
        r.font.name = FONT
        r.font.size = Pt(9)
        r.font.color.rgb = BLUE_800
    return tb


CLOSING_FOOTER = "Thank you"


def closing_slide(prs, logo_path=None, tagline="Thank you"):
    """Optional thank-you / closing slide (see compliance checklist)."""
    slide = title_only_slide(prs)
    corner_accent(slide)
    panel = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(SLIDE_W), Inches(5.85)
    )
    fill(panel, BLUE_800)
    if logo_path:
        slide.shapes.add_picture(logo_path, Inches(0.55), Inches(0.45), height=Inches(0.55))
    tb = slide.shapes.add_textbox(Inches(0.8), Inches(2.35), Inches(11.7), Inches(1.4))
    tf = tb.text_frame
    no_autofit(tf)
    tf.text = tagline
    tf.paragraphs[0].alignment = PP_ALIGN.CENTER
    _style(tf, WHITE, 32, bold=True)
    band = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0), Inches(5.95), Inches(SLIDE_W), Inches(1.55)
    )
    fill(band, ACCENT)
    ftb = slide.shapes.add_textbox(Inches(0.45), Inches(6.05), Inches(12.4), Inches(1.35))
    ftf = ftb.text_frame
    no_autofit(ftf)
    ftf.word_wrap = True
    ftf.text = CLOSING_FOOTER
    for p in ftf.paragraphs:
        p.alignment = PP_ALIGN.LEFT
        p.space_after = Pt(2)
        for r in p.runs:
            r.font.name = FONT
            r.font.size = Pt(8)
            r.font.color.rgb = BLUE_800
    return slide
