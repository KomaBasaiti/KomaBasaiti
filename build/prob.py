"""Probability & statistics sections (4–8) for the simplified formula sheet."""
import math

from svg import C1, C2, C3, C4, INK

MUTED = "#6b7a78"


def _f(v):
    return f"{v:.2f}".rstrip("0").rstrip(".")


def box(kind, title, body):
    return f'<div class="box {kind}"><div class="tag">{kind.upper()}</div><h4>{title}</h4>{body}</div>'


def ex(body, title="Example"):
    return f'<div class="ex"><span class="exl">{title}</span>{body}</div>'


# ---------- figures ----------
venn = f"""
<svg viewBox="0 0 250 150" width="250" height="150" class="g" font-size="10">
  <rect x="6" y="6" width="238" height="138" rx="6" fill="#fbfdfc" stroke="{INK}"/>
  <text x="14" y="22" font-size="11" font-weight="700">ξ</text>
  <circle cx="98" cy="78" r="50" fill="{C1}" fill-opacity=".18" stroke="{C1}" stroke-width="1.6"/>
  <circle cx="152" cy="78" r="50" fill="{C4}" fill-opacity=".18" stroke="{C4}" stroke-width="1.6"/>
  <text x="62" y="36" fill="{C1}" font-weight="700" font-size="12">A</text>
  <text x="182" y="36" fill="{C4}" font-weight="700" font-size="12">B</text>
  <text x="74" y="82" text-anchor="middle">A ∩ B′</text><text x="74" y="96" text-anchor="middle" fill="{C1}" font-weight="700">0.3</text>
  <text x="125" y="82" text-anchor="middle">A ∩ B</text><text x="125" y="96" text-anchor="middle" fill="{INK}" font-weight="700">0.2</text>
  <text x="176" y="82" text-anchor="middle">A′ ∩ B</text><text x="176" y="96" text-anchor="middle" fill="{C4}" font-weight="700">0.2</text>
  <text x="226" y="132" text-anchor="end">neither: <tspan font-weight="700">0.3</tspan></text>
</svg>"""


def _tree():
    # without replacement: 3 red, 5 blue, two draws
    o = ['<svg viewBox="0 0 400 190" width="400" height="190" class="g" font-size="10">']
    root = (20, 95)
    first = [(130, 45, "R", "3/8", C2), (130, 145, "B", "5/8", C4)]
    second = {
        "R": [(250, 20, "R", "2/7", C2, "RR", "3/8 × 2/7 = 6/56"), (250, 70, "B", "5/7", C4, "RB", "3/8 × 5/7 = 15/56")],
        "B": [(250, 120, "R", "3/7", C2, "BR", "5/8 × 3/7 = 15/56"), (250, 170, "B", "4/7", C4, "BB", "5/8 × 4/7 = 20/56")],
    }
    o.append(f'<circle cx="{root[0]}" cy="{root[1]}" r="4" fill="{INK}"/>')
    for x, y, lab, p, col in first:
        o.append(f'<line x1="{root[0]}" y1="{root[1]}" x2="{x-10}" y2="{y}" stroke="{MUTED}" stroke-width="1.3"/>')
        o.append(f'<text x="{(root[0]+x)/2 - 4}" y="{(root[1]+y)/2 - 4}" text-anchor="middle" fill="{MUTED}">{p}</text>')
        o.append(f'<circle cx="{x}" cy="{y}" r="10" fill="{col}" fill-opacity=".15" stroke="{col}"/>')
        o.append(f'<text x="{x}" y="{y+4}" text-anchor="middle" font-weight="700" fill="{col}">{lab}</text>')
        for x2, y2, l2, p2, c2, name, prod in second[lab]:
            o.append(f'<line x1="{x+10}" y1="{y}" x2="{x2-10}" y2="{y2}" stroke="{MUTED}" stroke-width="1.3"/>')
            o.append(f'<text x="{(x+x2)/2}" y="{(y+y2)/2 - 4}" text-anchor="middle" fill="{MUTED}">{p2}</text>')
            o.append(f'<circle cx="{x2}" cy="{y2}" r="10" fill="{c2}" fill-opacity=".15" stroke="{c2}"/>')
            o.append(f'<text x="{x2}" y="{y2+4}" text-anchor="middle" font-weight="700" fill="{c2}">{l2}</text>')
            bold = ' font-weight="700"' if name == "RR" else ""
            o.append(f'<text x="{x2+18}" y="{y2+4}"{bold}>{name}: {prod}</text>')
    o.append(f'<text x="20" y="182" fill="{MUTED}" font-size="9">1st draw</text><text x="122" y="182" fill="{MUTED}" font-size="9"></text>')
    o.append("</svg>")
    return "".join(o)


tree = _tree()


def bars(probs, hi=None, w=330, h=150, title="", xlabel="x", ymax=None):
    n = len(probs)
    pad_l, pad_b, pad_t = 30, 22, 18
    ymax = ymax or max(probs) * 1.15
    bw = (w - pad_l - 10) / n
    o = [f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" class="g" font-size="9">']
    o.append(f'<text x="{w/2}" y="12" text-anchor="middle" class="gt">{title}</text>')
    base = h - pad_b
    for i, p in enumerate(probs):
        bh = (base - pad_t) * p / ymax
        x = pad_l + i * bw + bw * 0.12
        col = C3 if i == hi else C1
        o.append(f'<rect x="{_f(x)}" y="{_f(base-bh)}" width="{_f(bw*0.76)}" height="{_f(bh)}" fill="{col}" fill-opacity="{0.85 if i == hi else 0.55}"/>')
        o.append(f'<text x="{_f(x+bw*0.38)}" y="{base+11}" text-anchor="middle">{i}</text>')
        if p > 0.05:
            o.append(f'<text x="{_f(x+bw*0.38)}" y="{_f(base-bh-3)}" text-anchor="middle" font-size="7.5" fill="{MUTED}">{p:.3f}</text>')
    o.append(f'<line x1="{pad_l}" y1="{base}" x2="{w-6}" y2="{base}" stroke="{INK}"/>')
    o.append(f'<text x="{w-8}" y="{base+20}" text-anchor="end" fill="{MUTED}">{xlabel}</text>')
    o.append("</svg>")
    return "".join(o)


binom10 = [math.comb(10, k) * 0.3**k * 0.7**(10 - k) for k in range(11)]
bin_fig = bars(binom10, hi=3, title="X ~ Bi(10, 0.3): the tallest bar is the mode, x = 3", xlabel="number of successes x")


def area_plot(f, xr, yr, shade, w=260, h=160, title="", marks=(), labels=(), curve_dom=None, pad=16):
    x0, x1 = xr
    y0, y1 = yr
    top = 14
    X = lambda x: pad + (x - x0) * (w - 2 * pad) / (x1 - x0)
    Y = lambda y: h - pad - (y - y0) * (h - 2 * pad - top) / (y1 - y0)
    a, b = curve_dom or xr
    o = [f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" class="g" font-size="9">',
         f'<text x="{w/2}" y="12" text-anchor="middle" class="gt">{title}</text>']
    for (sa, sb, col) in shade:
        pts = [(X(sa), Y(0))] + [(X(sa + (sb - sa) * i / 120), Y(f(sa + (sb - sa) * i / 120))) for i in range(121)] + [(X(sb), Y(0))]
        o.append(f'<polygon points="{" ".join(f"{_f(px)},{_f(py)}" for px, py in pts)}" fill="{col}" fill-opacity=".28"/>')
    o.append(f'<line x1="{pad-4}" y1="{_f(Y(0))}" x2="{w-pad+4}" y2="{_f(Y(0))}" stroke="#8a9896" marker-end="url(#ar)"/>')
    d = "M" + " L".join(f"{_f(X(a + (b - a) * i / 300))} {_f(Y(f(a + (b - a) * i / 300)))}" for i in range(301))
    o.append(f'<path d="{d}" fill="none" stroke="{C1}" stroke-width="2"/>')
    for xm, col, lab in marks:
        o.append(f'<line x1="{_f(X(xm))}" y1="{_f(Y(0))}" x2="{_f(X(xm))}" y2="{_f(Y(f(xm)))}" stroke="{col}" stroke-width="1.3" stroke-dasharray="4 3"/>')
        o.append(f'<text x="{_f(X(xm))}" y="{_f(Y(0)+11)}" text-anchor="middle" fill="{col}">{lab}</text>')
    for lx, ly, t, anc, col in labels:
        o.append(f'<text x="{_f(X(lx))}" y="{_f(Y(ly))}" text-anchor="{anc}" fill="{col}">{t}</text>')
    o.append("</svg>")
    return "".join(o)


pdf_fig = area_plot(lambda x: 3 * x * x / 8, (-0.3, 2.4), (0, 1.6), [(1, 2, C1)],
                    title="f(x) = 3x²/8 on [0, 2]", curve_dom=(0, 2),
                    marks=[(4 ** (1 / 3), C3, "median 1.59"), (1.5, C2, "")],
                    labels=[(1.5, 1.05, "mean 1.5", "middle", C2), (1.55, 0.22, "Pr(1 ≤ X ≤ 2) = 7/8", "middle", INK)])

phi = lambda z: math.exp(-z * z / 2) / math.sqrt(2 * math.pi)


def bell():
    w, h, pad, top = 400, 200, 16, 14
    X = lambda z: pad + (z + 3.6) * (w - 2 * pad) / 7.2
    Y = lambda y: h - 52 - y * (h - 52 - pad - top) / 0.42
    o = [f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" class="g" font-size="9">',
         f'<text x="{w/2}" y="12" text-anchor="middle" class="gt">The 68–95–99.7 rule</text>']
    for k, col, op in [(3, C4, .12), (2, C3, .22), (1, C1, .35)]:
        pts = [(X(-k), Y(0))] + [(X(-k + 2 * k * i / 150), Y(phi(-k + 2 * k * i / 150))) for i in range(151)] + [(X(k), Y(0))]
        o.append(f'<polygon points="{" ".join(f"{_f(a)},{_f(b)}" for a, b in pts)}" fill="{col}" fill-opacity="{op}"/>')
    d = "M" + " L".join(f"{_f(X(-3.6 + 7.2 * i / 300))} {_f(Y(phi(-3.6 + 7.2 * i / 300)))}" for i in range(301))
    o.append(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="1.8"/>')
    o.append(f'<line x1="{pad}" y1="{_f(Y(0))}" x2="{w-pad}" y2="{_f(Y(0))}" stroke="{INK}"/>')
    labs = ["μ−3σ", "μ−2σ", "μ−σ", "μ", "μ+σ", "μ+2σ", "μ+3σ"]
    for i, z in enumerate(range(-3, 4)):
        o.append(f'<line x1="{_f(X(z))}" y1="{_f(Y(0))}" x2="{_f(X(z))}" y2="{_f(Y(0)+4)}" stroke="{INK}"/>')
        o.append(f'<text x="{_f(X(z))}" y="{_f(Y(0)+14)}" text-anchor="middle">{labs[i]}</text>')
    o.append(f'<text x="{_f(X(0))}" y="{_f(Y(0.2))}" text-anchor="middle" font-weight="700" fill="{C1}" font-size="11">68%</text>')
    for k, col, lab, dy in [(2, C3, "95%", 26), (3, C4, "99.7%", 42)]:
        yy = Y(0) + dy
        o.append(f'<line x1="{_f(X(-k))}" y1="{_f(yy)}" x2="{_f(X(k))}" y2="{_f(yy)}" stroke="{col}" stroke-width="1.3" marker-end="url(#ar)" marker-start="url(#ar)"/>')
        o.append(f'<rect x="{_f(X(0)-18)}" y="{_f(yy-7)}" width="36" height="13" fill="#fbfdfc"/>')
        o.append(f'<text x="{_f(X(0))}" y="{_f(yy+3.5)}" text-anchor="middle" fill="{col}" font-weight="700">{lab}</text>')
    o.append("</svg>")
    return "".join(o)


bell_fig = bell()


def tail_pic(lo, hi, title, note):
    w, h = 190, 105
    X = lambda z: 10 + (z + 3.3) * (w - 20) / 6.6
    Y = lambda y: h - 18 - y * (h - 40) / 0.42
    lo_ = max(lo, -3.3)
    hi_ = min(hi, 3.3)
    pts = [(X(lo_), Y(0))] + [(X(lo_ + (hi_ - lo_) * i / 100), Y(phi(lo_ + (hi_ - lo_) * i / 100))) for i in range(101)] + [(X(hi_), Y(0))]
    d = "M" + " L".join(f"{_f(X(-3.3 + 6.6 * i / 200))} {_f(Y(phi(-3.3 + 6.6 * i / 200)))}" for i in range(201))
    return (f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" class="g" font-size="9">'
            f'<text x="{w/2}" y="12" text-anchor="middle" class="gt">{title}</text>'
            f'<polygon points="{" ".join(f"{_f(a)},{_f(b)}" for a, b in pts)}" fill="{C2}" fill-opacity=".3"/>'
            f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="1.5"/>'
            f'<line x1="10" y1="{_f(Y(0))}" x2="{w-10}" y2="{_f(Y(0))}" stroke="{INK}"/>'
            f'<text x="{w/2}" y="{h-5}" text-anchor="middle" fill="{MUTED}">{note}</text></svg>')


tails = "".join([
    tail_pic(-9, 0.8, "Pr(X &lt; b)", "normalCdf(−∞, b, μ, σ)"),
    tail_pic(0.8, 9, "Pr(X &gt; a)", "normalCdf(a, ∞, μ, σ)"),
    tail_pic(-0.7, 1.0, "Pr(a &lt; X &lt; b)", "normalCdf(a, b, μ, σ)"),
])

ci_line = f"""
<svg viewBox="0 0 420 80" width="420" height="80" class="g" font-size="10">
  <line x1="20" y1="45" x2="400" y2="45" stroke="{INK}"/>
  <line x1="90" y1="38" x2="90" y2="52" stroke="{C2}" stroke-width="2"/>
  <line x1="330" y1="38" x2="330" y2="52" stroke="{C2}" stroke-width="2"/>
  <rect x="90" y="40" width="240" height="10" fill="{C2}" fill-opacity=".18"/>
  <circle cx="210" cy="45" r="5" fill="{C1}"/>
  <text x="210" y="70" text-anchor="middle" fill="{C1}" font-weight="700">p̂ = 0.4</text>
  <text x="90" y="70" text-anchor="middle" fill="{C2}">0.304</text>
  <text x="330" y="70" text-anchor="middle" fill="{C2}">0.496</text>
  <line x1="94" y1="24" x2="206" y2="24" stroke="{C3}" marker-end="url(#ar)" marker-start="url(#ar)"/>
  <line x1="214" y1="24" x2="326" y2="24" stroke="{C3}" marker-end="url(#ar)" marker-start="url(#ar)"/>
  <text x="150" y="18" text-anchor="middle" fill="{C3}">M = 0.096</text>
  <text x="270" y="18" text-anchor="middle" fill="{C3}">M = 0.096</text>
</svg>"""


def strip(sel, n=7):
    cells = []
    for i in range(n):
        on = i in sel
        cells.append(f'<span class="dot{" on" if on else ""}">{i}</span>')
    return '<span class="strip">' + "".join(cells) + "</span>"


words = f"""
<table>
<tr><th>The question says…</th><th>Write</th><th>Values included (x = 0 to 6)</th><th>Calculator form</th></tr>
<tr><td>exactly 3</td><td class="m">Pr(X = 3)</td><td>{strip({3})}</td><td class="m">binomPdf(n, p, 3)</td></tr>
<tr><td>at most 3 / no more than 3</td><td class="m">Pr(X ≤ 3)</td><td>{strip({0,1,2,3})}</td><td class="m">binomCdf(n, p, 0, 3)</td></tr>
<tr><td>fewer than 3 / less than 3</td><td class="m">Pr(X ≤ 2)</td><td>{strip({0,1,2})}</td><td class="m">binomCdf(n, p, 0, 2)</td></tr>
<tr><td>at least 3 / no fewer than 3</td><td class="m">Pr(X ≥ 3) = 1 − Pr(X ≤ 2)</td><td>{strip({3,4,5,6})}</td><td class="m">binomCdf(n, p, 3, n)</td></tr>
<tr><td>more than 3</td><td class="m">Pr(X ≥ 4)</td><td>{strip({4,5,6})}</td><td class="m">binomCdf(n, p, 4, n)</td></tr>
<tr><td>between 2 and 5 inclusive</td><td class="m">Pr(2 ≤ X ≤ 5)</td><td>{strip({2,3,4,5})}</td><td class="m">binomCdf(n, p, 2, 5)</td></tr>
</table>"""


PROB_CSS = """
.strip { display:inline-flex; gap:3px; }
.dot { display:inline-flex; width:17px; height:17px; border-radius:50%; border:1.3px solid #c9d4d2; color:#9aa9a7; font-size:8.5pt; align-items:center; justify-content:center; }
.dot.on { background:#1f6f68; border-color:#1f6f68; color:#fff; font-weight:700; }
.bridge { border:2px dashed #e7b94a; border-radius:9px; padding:6px 10px; margin:7px 0; background:#fffdf5; break-inside:avoid; }
.bridge .tag { font-size:7.8pt; letter-spacing:.12em; font-weight:700; color:#b7791f; }
.bridge h4 { font-size:10.6pt; margin:1px 0 3px; }
.cond { display:grid; grid-template-columns:repeat(4,1fr); gap:6px; margin:5px 0; break-inside:avoid; }
.cond div { border:1.5px solid #1f6f68; border-radius:8px; padding:6px; text-align:center; background:#eef5f4; font-size:9.2pt; }
.cond b { display:block; font-size:15pt; color:#1f6f68; font-family:Fraunces,serif; }
.right { color:#1f6f68; font-weight:700; } .wrong { color:#c0392b; font-weight:700; }
"""


def bridge(title, body):
    return f'<div class="bridge"><div class="tag">LINK TO YEAR 7 — COLLECTING &amp; SUMMARISING DATA</div><h4>{title}</h4>{body}</div>'


PROB = f"""
<!-- ======================= 4 ======================= -->
<h2><span class="num">4</span> Probability rules and conditional probability</h2>

<div class="grid2">
<div>
<table>
<tr><th>Rule</th><th>Formula</th></tr>
<tr><td>Complement</td><td class="m">Pr(A′) = 1 − Pr(A)</td></tr>
<tr><td>Addition ("or")</td><td class="m">Pr(A ∪ B) = Pr(A) + Pr(B) − Pr(A ∩ B)</td></tr>
<tr><td>Mutually exclusive</td><td class="m">Pr(A ∩ B) = 0</td></tr>
<tr><td>Conditional ("given")</td><td class="m">Pr(A | B) = Pr(A ∩ B) / Pr(B)</td></tr>
<tr><td>Multiplication ("and")</td><td class="m">Pr(A ∩ B) = Pr(A | B) × Pr(B)</td></tr>
<tr><td>Independent</td><td class="m">Pr(A ∩ B) = Pr(A) × Pr(B)</td></tr>
<tr><td>Neither</td><td class="m">Pr(A′ ∩ B′) = 1 − Pr(A ∪ B)</td></tr>
</table>
</div>
<div class="fig">{venn}<div class="cap">Pr(A) = 0.5, Pr(B) = 0.4, Pr(A ∩ B) = 0.2</div></div>
</div>

<h3>The two-way (Karnaugh) table — fastest method for "and / or / given / neither"</h3>
<div class="grid2">
<table>
<tr><th></th><th class="c">B</th><th class="c">B′</th><th class="c">Total</th></tr>
<tr><th>A</th><td class="c"><b>0.2</b></td><td class="c">0.5 − 0.2 = <b>0.3</b></td><td class="c">0.5</td></tr>
<tr><th>A′</th><td class="c">0.4 − 0.2 = <b>0.2</b></td><td class="c"><b>0.3</b></td><td class="c">0.5</td></tr>
<tr><th>Total</th><td class="c">0.4</td><td class="c">0.6</td><td class="c"><b>1</b></td></tr>
</table>
{ex('Pr(A ∪ B) = 0.5 + 0.4 − 0.2 = <b>0.7</b>. &nbsp;Neither = <b>0.3</b>.<br>Pr(A | B) = 0.2 ÷ 0.4 = <b>0.5</b> = Pr(A) → A and B are <b>independent</b>. (Check: 0.5 × 0.4 = 0.2 ✓)')}
</div>
<p class="small">Fill the totals you are given, then the inner cells. Every row and column must add up, and the corner is always 1.</p>

<h3>Tree diagrams — multiply along, add across</h3>
<div class="grid2">
<div class="fig">{tree}<div class="cap">3 red and 5 blue counters, draw 2 <b>without</b> replacement</div></div>
<div>
<table>
<tr><th></th><th>With replacement</th><th>Without replacement</th></tr>
<tr><td>Pr(both red)</td><td class="m">3/8 × 3/8 = 9/64</td><td class="m">3/8 × 2/7 = 3/28</td></tr>
<tr><td>Probabilities</td><td>stay the same</td><td>change each draw</td></tr>
<tr><td>Model</td><td>binomial ✓</td><td>tree, <b>not</b> binomial</td></tr>
</table>
<p class="small">Pr(one of each) = RB + BR = 15/56 + 15/56 = 30/56 = 15/28. Branches leaving any point must add to 1.</p>
</div>
</div>
{box('trap', 'Mutually exclusive is NOT the same as independent', '<p>Mutually exclusive: A and B <b>can\'t both happen</b> (Pr(A ∩ B) = 0). Independent: one <b>doesn\'t change</b> the chance of the other. If both events can happen on their own, mutually exclusive events are always <b>dependent</b>. Always prove independence with numbers: compare Pr(A ∩ B) with Pr(A) × Pr(B).</p>')}

<div class="try">
<h4>Try it yourself — Section 4</h4>
<ol>
<li>Pr(A) = 0.6, Pr(B) = 0.5 and Pr(A ∩ B) = 0.3. Find Pr(A ∪ B) and Pr(A′ ∩ B′).</li>
<li>Are A and B in Q1 independent? Show why.</li>
</ol>
</div>

<!-- ======================= 5 ======================= -->
<h2><span class="num">5</span> Discrete random variables and the binomial distribution</h2>
{bridge('E(X) is the "mean from a frequency table" you already know', '''<p>In Year 7: mean = Σ(score × frequency) ÷ total. Divide each frequency by the total and you get a probability — so the mean becomes <span class="m">E(X) = Σ x · Pr(X = x)</span>.</p>
<table>
<tr><th>Books read, x</th><td class="c">0</td><td class="c">1</td><td class="c">2</td><td class="c">3</td><th>Total</th></tr>
<tr><th>Frequency</th><td class="c">6</td><td class="c">6</td><td class="c">4</td><td class="c">1</td><td class="c">17</td></tr>
<tr><th>Pr(X = x)</th><td class="c">6/17</td><td class="c">6/17</td><td class="c">4/17</td><td class="c">1/17</td><td class="c">1</td></tr>
</table>
<p>Year 7: (0×6 + 1×6 + 2×4 + 3×1) ÷ 17 = 17 ÷ 17 = 1. &nbsp;Methods: 0(6/17) + 1(6/17) + 2(4/17) + 3(1/17) = <b>1</b>. Same answer!</p>''')}

<h3>A probability distribution — the one-table method</h3>
<p>Two rules: every probability is between 0 and 1, and they <b>add to 1</b>. Then build E(X) and E(X²) in the same table:</p>
<table>
<tr><th>x</th><td class="c">0</td><td class="c">1</td><td class="c">2</td><td class="c">3</td><th class="c">Sum</th></tr>
<tr><th>Pr(X = x)</th><td class="c">0.1</td><td class="c">0.3</td><td class="c"><b>k = 0.4</b></td><td class="c">0.2</td><td class="c">1 → k = 0.4</td></tr>
<tr><th>x · Pr</th><td class="c">0</td><td class="c">0.3</td><td class="c">0.8</td><td class="c">0.6</td><td class="c"><b>E(X) = 1.7</b></td></tr>
<tr><th>x² · Pr</th><td class="c">0</td><td class="c">0.3</td><td class="c">1.6</td><td class="c">1.8</td><td class="c"><b>E(X²) = 3.7</b></td></tr>
</table>
<p><span class="m">Var(X) = E(X²) − [E(X)]² = 3.7 − 1.7² = 0.81</span> &nbsp;→&nbsp; <span class="m">sd(X) = √0.81 = 0.9</span></p>
{box('trap', 'E(X²) is not [E(X)]²', '<p>Square each <b>x</b>, keep the probabilities the same. If your variance comes out negative, you squared the wrong thing.</p>')}

<h3>Changing X:  aX + b</h3>
<table>
<tr><th>Measure</th><th>Rule</th><th>E(X) = 2.1, Var(X) = 0.49 → for 3X − 1</th></tr>
<tr><td>Mean</td><td class="m">E(aX + b) = aE(X) + b</td><td>3(2.1) − 1 = <b>5.3</b></td></tr>
<tr><td>Variance</td><td class="m">Var(aX + b) = a² Var(X)</td><td>9 × 0.49 = <b>4.41</b> (the −1 does nothing)</td></tr>
<tr><td>Standard deviation</td><td class="m">sd(aX + b) = |a| sd(X)</td><td>3 × 0.7 = <b>2.1</b></td></tr>
</table>

<h3>The binomial distribution  X ~ Bi(n, p)</h3>
<p>Use it only when <b>all four</b> are true:</p>
<div class="cond">
<div><b>n</b>fixed number of trials</div>
<div><b>2</b>outcomes: success / failure</div>
<div><b>p</b>same chance every trial</div>
<div><b>⊥</b>trials independent</div>
</div>
<div class="grid2">
<div>
<table>
<tr><th>What</th><th>Formula</th></tr>
<tr><td>Probability</td><td class="m">Pr(X = x) = ⁿCₓ pˣ (1 − p)ⁿ⁻ˣ</td></tr>
<tr><td>Mean</td><td class="m">E(X) = np</td></tr>
<tr><td>Variance</td><td class="m">Var(X) = np(1 − p)</td></tr>
<tr><td>At least one</td><td class="m">Pr(X ≥ 1) = 1 − (1 − p)ⁿ</td></tr>
<tr><td>Most likely value</td><td class="m">mode = whole-number part of (n + 1)p</td></tr>
</table>
{ex('X ~ Bi(5, 0.2): Pr(X = 2) = ⁵C₂(0.2)²(0.8)³ = 10 × 0.04 × 0.512 = <b>0.2048</b>.<br>Check: the powers 2 + 3 add to n = 5 ✓')}
</div>
<div class="fig">{bin_fig}<div class="cap">(n + 1)p = 11 × 0.3 = 3.3 → mode 3. Mean np = 3, variance 2.1</div></div>
</div>

<h3>Turning words into inequalities</h3>
{words}
{box('trap', 'Off by one in "at least"', '<p>For a discrete X: <span class="m">Pr(X ≥ 3) = 1 − Pr(X ≤ 2)</span>, <b>not</b> 1 − Pr(X ≤ 3). For Bi(20, 0.4) the right answer is 0.9964; the wrong one gives 0.9840 — close enough to look fine, still wrong.</p>')}
{box('trick', '"At least one" is one line', '<p>Never add Pr(X = 1) + Pr(X = 2) + … Use <span class="m">1 − (1 − p)ⁿ</span>. With n = 5, p = 0.2: 1 − 0.8⁵ = <b>0.67232</b>.<br>Backwards — "how many trials for at least a 95% chance?": 1 − 0.8ⁿ ≥ 0.95 → n ≥ 13.4 → <b>n = 14</b> (always round <b>up</b>; n = 13 only gives 0.945).</p>')}
{box('trick', 'Conditional binomial: divide, don\'t subtract', '<p><span class="m">Pr(X ≥ 2 | X ≥ 1) = Pr(X ≥ 2) ÷ Pr(X ≥ 1)</span> because "X ≥ 2" sits inside "X ≥ 1". For Bi(8, 0.25): 0.6329 ÷ 0.8999 = <b>0.7033</b>.</p>')}
{box('check', 'Binomial variance is always smaller than the mean', '<p>np(1 − p) &lt; np. Bi(20, 0.4): mean 8, variance 4.8. If you get a variance of 8 or more, you forgot the (1 − p).</p>')}

<div class="try">
<h4>Try it yourself — Section 5</h4>
<ol>
<li>x = 1, 2, 3 with Pr = 0.2, k, 0.5. Find k and E(X).</li>
<li>X ~ Bi(10, 0.1). Find E(X), Var(X) and Pr(X ≥ 1).</li>
<li>Write "more than 2 but fewer than 6" as an inequality in X.</li>
</ol>
</div>

<!-- ======================= 6 ======================= -->
<h2><span class="num">6</span> Continuous random variables (probability density functions)</h2>
<div class="grid2">
<div>
<table>
<tr><th>What</th><th>Formula</th></tr>
<tr><td>It is a pdf if</td><td class="m">f(x) ≥ 0 and total area = 1</td></tr>
<tr><td>Probability = area</td><td class="m">Pr(a ≤ X ≤ b) = ∫ₐᵇ f(x) dx</td></tr>
<tr><td>Mean</td><td class="m">E(X) = ∫ x f(x) dx</td></tr>
<tr><td>Variance</td><td class="m">E(X²) − [E(X)]², E(X²) = ∫ x² f(x) dx</td></tr>
<tr><td>Median m</td><td class="m">∫ from start to m of f(x) dx = 0.5</td></tr>
<tr><td>Mode</td><td>x where f(x) is highest (can be an endpoint)</td></tr>
</table>
<p class="small">For a continuous X, Pr(X = a) = 0, so ≤ and &lt; give the same answer.</p>
</div>
<div class="fig">{pdf_fig}</div>
</div>
{ex('f(x) = 3x²/8 on [0, 2].<br>Area: [x³/8] from 0 to 2 = 8/8 = 1 ✓ &nbsp;·&nbsp; Pr(1 ≤ X ≤ 2) = 8/8 − 1/8 = <b>7/8</b><br>E(X) = ∫ 3x³/8 dx = [3x⁴/32] = 48/32 = <b>3/2</b> &nbsp;·&nbsp; E(X²) = [3x⁵/40] = 96/40 = 12/5 &nbsp;·&nbsp; Var = 12/5 − 9/4 = <b>3/20</b><br>Median: m³/8 = 1/2 → m³ = 4 → <b>m = ∛4 ≈ 1.587</b>. (Mean ≠ median because the graph is not symmetric.)')}
{box('trick', 'Unknown constant? Set the area to 1', '<p>If f(x) = kx on [0, 4], then ∫ kx dx = 8k = 1, so k = 1/8. Then check k makes f(x) ≥ 0.</p>')}

<div class="try">
<h4>Try it yourself — Section 6</h4>
<ol>
<li>f(x) = x/2 on [0, 2]. Show it is a pdf, then find Pr(X &lt; 1) and E(X).</li>
</ol>
</div>

<!-- ======================= 7 ======================= -->
<h2><span class="num">7</span> The normal distribution  X ~ N(μ, σ²)</h2>
<div class="figrow">{bell_fig}</div>
<table>
<tr><th>Fact</th><th>What to remember</th></tr>
<tr><td>Shape</td><td>bell-shaped, symmetric about μ → mean = median = mode = μ</td></tr>
<tr><td>Notation</td><td class="m">N(50, 9) means σ² = 9, so σ = 3 (not 9!)</td></tr>
<tr><td>z-score</td><td class="m">z = (x − μ) / σ — how many sds above the mean</td></tr>
<tr><td>Back to x</td><td class="m">x = μ + zσ</td></tr>
<tr><td>One tail</td><td>Pr(X &gt; μ + σ) ≈ 0.16, Pr(X &gt; μ + 2σ) ≈ 0.025 (halve what is left over)</td></tr>
<tr><td>Exact 95% cut</td><td>z = ±1.96 (not ±2)</td></tr>
</table>
{ex('Maths: you got 75, class μ = 65, σ = 5 → z = (75 − 65)/5 = <b>2</b>.<br>English: you got 80, class μ = 70, σ = 8 → z = (80 − 70)/8 = <b>1.25</b>.<br>The Maths mark is more impressive — it is further above its mean in standard deviations.', 'Example — compare with z-scores')}

<h3>Calculator commands — always sketch and shade first</h3>
<div class="figrow">{tails}</div>
<table>
<tr><th>You want</th><th>Command</th><th>Example, X ~ N(70, 4²)</th></tr>
<tr><td>a probability</td><td class="m">normalCdf(lower, upper, μ, σ)</td><td>Pr(X &gt; 75) = normalCdf(75, ∞, 70, 4) = <b>0.1056</b></td></tr>
<tr><td>an x-value from a probability</td><td class="m">invNorm(area to the LEFT, μ, σ)</td><td>Pr(X &lt; k) = 0.9 → k = invNorm(0.9, 70, 4) = <b>75.13</b></td></tr>
<tr><td>upper-tail k</td><td class="m">Pr(X &gt; k) = q → invNorm(1 − q, μ, σ)</td><td>Pr(X &gt; k) = 0.05 → enter <b>0.95</b>, not 0.05</td></tr>
</table>
{box('trick', 'Use symmetry — three answers from one calculation', '<p>65 and 75 are both 5 (= 1.25σ) away from 70. So once you know Pr(X &gt; 75) = 0.1056, you also know Pr(X &lt; 65) = <b>0.1056</b> and Pr(65 &lt; X &lt; 75) = 1 − 2(0.1056) = <b>0.7887</b>.</p>')}
{ex('σ = 5 and Pr(X &lt; 50) = 0.025. Find μ.<br>① z = invNorm(0.025) = −1.96 &nbsp; ② 50 = μ + (−1.96)(5) &nbsp; ③ μ = 50 + 9.8 = <b>59.8</b>.<br>Sense check: a small left-tail probability means 50 is <b>below</b> μ ✓', 'Example — find an unknown μ')}
{box('trap', 'The calculator wants σ, not σ²', '<p>X ~ N(50, 9): type σ = <b>3</b>. Write "σ = …" on the page before you touch the calculator.</p>')}
{box('trap', 'Standard deviations don\'t add — variances do', '<p>For two independent X₁, X₂ with sd σ, Var(X₁ + X₂) = 2σ², so sd = σ√2. But 2X (one value doubled) has sd 2σ.</p>')}

<div class="try">
<h4>Try it yourself — Section 7</h4>
<ol>
<li>X ~ N(100, 15²). Use the 68–95–99.7 rule to estimate Pr(X &gt; 130).</li>
<li>X ~ N(100, 15²). Pr(X &gt; k) = 0.1. What number do you enter into invNorm?</li>
</ol>
</div>

<!-- ======================= 8 ======================= -->
<h2><span class="num">8</span> Sample proportions and confidence intervals</h2>
{bridge('Census vs sample → p vs p̂', '''<table>
<tr><th></th><th>Population (census)</th><th>Sample</th></tr>
<tr><td>Who</td><td>everyone</td><td>a group chosen from the population</td></tr>
<tr><td>Proportion</td><td class="m">p — fixed, usually unknown</td><td class="m">p̂ = x / n — changes from sample to sample</td></tr>
<tr><td>Year 7 example</td><td>shoe sizes of <i>everyone</i> in your team</td><td>favourite cereal of 500 Australians</td></tr>
</table>
<p>Remember the Year 7 skate-park question: surveying 20 people <b>at</b> the skate park is a <b>biased</b> sample. A bigger n can't fix a biased method — it must be a <b>random</b> sample.</p>''')}

<h3>The distribution of P̂</h3>
<table>
<tr><th>What</th><th>Formula</th><th>Example: p = 0.4, n = 100</th></tr>
<tr><td>Mean</td><td class="m">E(P̂) = p</td><td>0.4</td></tr>
<tr><td>Standard deviation</td><td class="m">sd(P̂) = √( p(1 − p) / n )</td><td>√(0.24/100) = <b>0.0490</b></td></tr>
<tr><td>Approx. normal when</td><td class="m">np ≥ 10 and n(1 − p) ≥ 10</td><td>40 ✓ and 60 ✓</td></tr>
</table>
{box('trick', 'Small n? Turn P̂ back into a count', '<p>n = 4, p = 0.6: Pr(P̂ ≥ 0.5) = Pr(X ≥ 2) where X ~ Bi(4, 0.6) = <b>0.8208</b>. (Multiply p̂ by n to get the count.) Don\'t use the normal here — np = 2.4 is far below 10.</p>')}

<h3>Approximate confidence interval for p</h3>
<p class="m" style="font-size:10.5pt;white-space:normal">( p̂ − z√(p̂(1 − p̂)/n) , p̂ + z√(p̂(1 − p̂)/n) ) &nbsp; where the margin of error M = z√(p̂(1 − p̂)/n)</p>
<div class="grid2">
<table>
<tr><th>Confidence level</th><td class="c">90%</td><td class="c">95%</td><td class="c">99%</td></tr>
<tr><th>z</th><td class="c">1.645</td><td class="c">1.96</td><td class="c">2.576</td></tr>
<tr><th>Interval</th><td class="c">narrower</td><td class="c">→</td><td class="c">wider</td></tr>
</table>
<div class="fig">{ci_line}</div>
</div>
{ex('p̂ = 0.4, n = 100, 95%. &nbsp;M = 1.96 × √(0.4 × 0.6 / 100) = 1.96 × 0.0490 = <b>0.096</b>.<br>Interval: 0.4 ± 0.096 = <b>(0.304, 0.496)</b>.<br><b>Backwards:</b> from an interval, p̂ = (upper + lower)/2 and M = (upper − lower)/2.')}

<h3>How big a sample?</h3>
<table>
<tr><th>Rule</th><th>Formula</th><th>Example</th></tr>
<tr><td>sample size for margin M</td><td class="m">n ≥ z² p̂(1 − p̂) / M²</td><td rowspan="2">95%, M ≤ 0.03, no estimate of p:<br>n ≥ 1.96² / (4 × 0.03²) = 1067.1 → <b>n = 1068</b></td></tr>
<tr><td>no estimate of p (worst case)</td><td class="m">use p̂(1 − p̂) = 0.25</td></tr>
<tr><td>halve M</td><td colspan="2">multiply n by <b>4</b> (to cut M to a third, multiply n by 9). Doubling n only divides M by √2 ≈ 1.41</td></tr>
</table>
{box('trap', 'Round the sample size UP — always', '<p>n ≥ 1067.1 means 1068, even though .1 would normally round down. n = 1067 gives M = 0.030001, which is too big.</p>')}
{box('trap', 'Say what a confidence interval means — correctly', '''<table>
<tr><td class="right">✓ Correct</td><td>"We are 95% confident that the interval (0.304, 0.496) contains p." Or: "about 95% of intervals made this way would contain p."</td></tr>
<tr><td class="wrong">✗ Wrong</td><td>"There is a 95% chance that p is between 0.304 and 0.496." — p is a fixed number; it is the <b>interval</b> that changes between samples.</td></tr>
</table>''')}
{box('check', 'Three checks on any interval', '<p>① p̂ is exactly the middle. ② Both ends are between 0 and 1. ③ On the same data, 99% is wider than 95%, which is wider than 90%.</p>')}

<div class="try">
<h4>Try it yourself — Section 8</h4>
<ol>
<li>In a random sample of 400 people, 120 like a new app. Find p̂ and an approximate 95% confidence interval for p.</li>
<li>A poll wants a margin of error of 0.05 at 95% confidence with no estimate of p. What sample size is needed?</li>
<li>If the sample size is multiplied by 4, what happens to the margin of error?</li>
</ol>
</div>
"""

PROB_ANS = """
<div>
<h4>Section 4</h4>
<p>1. Pr(A ∪ B) = 0.6 + 0.5 − 0.3 = <b>0.8</b>; neither = 1 − 0.8 = <b>0.2</b></p>
<p>2. 0.6 × 0.5 = 0.3 = Pr(A ∩ B) → <b>independent</b></p>
<h4>Section 5</h4>
<p>1. 0.2 + k + 0.5 = 1 → <b>k = 0.3</b>; E(X) = 0.2 + 0.6 + 1.5 = <b>2.3</b></p>
<p>2. E(X) = 1, Var(X) = 0.9, Pr(X ≥ 1) = 1 − 0.9¹⁰ ≈ <b>0.6513</b></p>
<p>3. <b>Pr(3 ≤ X ≤ 5)</b></p>
<h4>Section 6</h4>
<p>1. f ≥ 0 and ∫₀² x/2 dx = [x²/4] = 1 ✓; Pr(X &lt; 1) = <b>1/4</b>; E(X) = ∫₀² x²/2 dx = <b>4/3</b></p>
</div>
<div>
<h4>Section 7</h4>
<p>1. 130 = μ + 2σ → about 0.025 (exact 0.0228)</p>
<p>2. Left area 1 − 0.1 = <b>0.9</b>: invNorm(0.9, 100, 15) ≈ 119.2</p>
<h4>Section 8</h4>
<p>1. p̂ = 0.3; M = 1.96√(0.3 × 0.7/400) ≈ 0.0449 → <b>(0.255, 0.345)</b></p>
<p>2. n ≥ 1.96²/(4 × 0.05²) = 384.2 → <b>n = 385</b></p>
<p>3. It is <b>halved</b> (M ∝ 1/√n)</p>
</div>
"""
