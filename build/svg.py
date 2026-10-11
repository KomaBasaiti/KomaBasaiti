"""Small SVG plotting helpers for the formula sheet."""
import math

INK = "#1d2b2a"
AXIS = "#8a9896"
GRID = "#e6eceb"
C1 = "#1f6f68"   # teal
C2 = "#c0392b"   # red
C3 = "#b7791f"   # amber
C4 = "#2b5d9c"   # blue


def _fmt(v):
    return f"{v:.2f}".rstrip("0").rstrip(".")


def graph(funcs, xr, yr, w=210, h=150, asym=(), points=(), labels=(),
          hlines=(), pad=14, axes=True, title=None):
    """funcs: list of dicts {f, color, dom=(a,b), dash=False, width}.
    asym: list of ('v', x) / ('h', y).  points: (x, y, filled, color).
    labels: (x, y, text, anchor, color, size).  hlines: (y, color) solid lines."""
    x0, x1 = xr
    y0, y1 = yr
    sx = (w - 2 * pad) / (x1 - x0)
    top = 13 if title else 0
    sy = (h - 2 * pad - top) / (y1 - y0)
    X = lambda x: pad + (x - x0) * sx
    Y = lambda y: h - pad - (y - y0) * sy
    out = [f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" class="g" font-size="9">']
    if title:
        out.append(f'<text x="{w/2}" y="11" text-anchor="middle" class="gt">{title}</text>')
    if axes:
        if y0 <= 0 <= y1:
            out.append(f'<line x1="{pad-4}" y1="{_fmt(Y(0))}" x2="{w-pad+4}" y2="{_fmt(Y(0))}" stroke="{AXIS}" stroke-width="1" marker-end="url(#ar)"/>')
        if x0 <= 0 <= x1:
            out.append(f'<line x1="{_fmt(X(0))}" y1="{h-pad+4}" x2="{_fmt(X(0))}" y2="{pad+top-4}" stroke="{AXIS}" stroke-width="1" marker-end="url(#ar)"/>')
    for kind, v in asym:
        if kind == "v":
            out.append(f'<line x1="{_fmt(X(v))}" y1="{pad+top-4}" x2="{_fmt(X(v))}" y2="{h-pad+4}" stroke="{C2}" stroke-width="1" stroke-dasharray="4 3"/>')
        else:
            out.append(f'<line x1="{pad-4}" y1="{_fmt(Y(v))}" x2="{w-pad+4}" y2="{_fmt(Y(v))}" stroke="{C2}" stroke-width="1" stroke-dasharray="4 3"/>')
    for yv, col in hlines:
        out.append(f'<line x1="{pad-4}" y1="{_fmt(Y(yv))}" x2="{w-pad+4}" y2="{_fmt(Y(yv))}" stroke="{col}" stroke-width="1.3"/>')
    for fn in funcs:
        f = fn["f"]
        a, b = fn.get("dom", xr)
        n = 500
        segs, cur = [], []
        prev = None
        for i in range(n + 1):
            x = a + (b - a) * i / n
            try:
                y = f(x)
            except (ValueError, ZeroDivisionError):
                y = None
            if y is None or isinstance(y, complex) or math.isnan(y) or y < y0 - (y1 - y0) or y > y1 + (y1 - y0):
                if cur:
                    segs.append(cur)
                cur, prev = [], None
                continue
            if prev is not None and abs(y - prev) > (y1 - y0):
                segs.append(cur)
                cur = []
            cur.append((X(x), Y(max(min(y, y1 + 2), y0 - 2))))
            prev = y
        if cur:
            segs.append(cur)
        dash = ' stroke-dasharray="5 3"' if fn.get("dash") else ""
        for s in segs:
            if len(s) < 2:
                continue
            d = "M" + " L".join(f"{_fmt(px)} {_fmt(py)}" for px, py in s)
            out.append(f'<path d="{d}" fill="none" stroke="{fn.get("color", C1)}" stroke-width="{fn.get("width", 2)}"{dash} clip-path="url(#clip{w}x{h}t{top})"/>')
    for p in points:
        x, y, filled = p[0], p[1], p[2]
        col = p[3] if len(p) > 3 else INK
        fill = col if filled else "#fff"
        out.append(f'<circle cx="{_fmt(X(x))}" cy="{_fmt(Y(y))}" r="3.2" fill="{fill}" stroke="{col}" stroke-width="1.5"/>')
    for lab in labels:
        x, y, t = lab[0], lab[1], lab[2]
        anc = lab[3] if len(lab) > 3 else "middle"
        col = lab[4] if len(lab) > 4 else INK
        size = lab[5] if len(lab) > 5 else 9
        out.append(f'<text x="{_fmt(X(x))}" y="{_fmt(Y(y))}" text-anchor="{anc}" fill="{col}" font-size="{size}">{t}</text>')
    out.insert(1, f'<defs><clipPath id="clip{w}x{h}t{top}"><rect x="0" y="{pad+top-6}" width="{w}" height="{h-2*pad-top+12}"/></clipPath></defs>')
    out.append("</svg>")
    return "".join(out)
