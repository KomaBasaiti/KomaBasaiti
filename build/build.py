"""Builds the simplified Methods 3&4 formula sheet as HTML."""
import math
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from svg import graph, C1, C2, C3, C4, INK  # noqa: E402
from prob import PROB, PROB_ANS, PROB_CSS  # noqa: E402
from calc import EXTRA_S1, EXTRA_S2, EXTRA_S3, S3_TRY, S3_ANS, CALC, CALC_ANS  # noqa: E402
from extra import EXTRA, EXTRA_ANS  # noqa: E402

PI = math.pi
s = math.sin
c = math.cos

# ---------- figures ----------
end_beh = "".join([
    graph([{"f": lambda x: x**2}], (-2, 2), (-1, 4), 120, 90, title="even, a &gt; 0"),
    graph([{"f": lambda x: -x**2}], (-2, 2), (-4, 1), 120, 90, title="even, a &lt; 0"),
    graph([{"f": lambda x: x**3}], (-1.7, 1.7), (-4, 4), 120, 90, title="odd, a &gt; 0"),
    graph([{"f": lambda x: -x**3}], (-1.7, 1.7), (-4, 4), 120, 90, title="odd, a &lt; 0"),
])

mult1 = graph([{"f": lambda x: (x - 1)}], (-0.6, 2.6), (-1.6, 1.6), 120, 86, labels=[(1, -0.55, "a")])
mult2 = graph([{"f": lambda x: (x - 1) ** 2}], (-0.6, 2.6), (-0.6, 2.2), 120, 86, labels=[(1, -0.45, "a")])
mult3 = graph([{"f": lambda x: (x - 1) ** 3}], (-0.6, 2.6), (-1.6, 1.6), 120, 86, labels=[(1, -0.55, "a")])

disc = "".join([
    graph([{"f": lambda x: x**2 - 1}], (-2, 2), (-1.5, 3), 120, 90, points=[(-1, 0, True, C2), (1, 0, True, C2)], title="Δ &gt; 0 : two"),
    graph([{"f": lambda x: x**2}], (-2, 2), (-1.5, 3), 120, 90, points=[(0, 0, True, C2)], title="Δ = 0 : one (touch)"),
    graph([{"f": lambda x: x**2 + 0.6}], (-2, 2), (-1.5, 3), 120, 90, title="Δ &lt; 0 : none"),
])

hyper = graph([{"f": lambda x: 2 / (x - 3) + 4}], (-1, 8), (-3, 10), 210, 160,
              asym=[("v", 3), ("h", 4)],
              points=[(2.5, 0, True, C1), (0, 10 / 3, True, C1)],
              labels=[(3.25, 9.2, "x = 3", "start", C2), (7.8, 4.5, "y = 4", "end", C2),
                      (2.5, -1.3, "(5/2, 0)", "middle", C1), (0.25, 10/3 + 0.4, "(0, 10/3)", "start", C1)],
              title="y = 2/(x − 3) + 4")
trunc = graph([{"f": lambda x: 1 / (x - 2) ** 2 + 3}], (-1, 5), (-1, 10), 210, 160,
              asym=[("v", 2), ("h", 3)],
              labels=[(2.2, 9.2, "x = 2", "start", C2), (4.9, 2.2, "y = 3", "end", C2)],
              title="y = 1/(x − 2)² + 3  (both arms up)")
sqrtg = graph([{"f": lambda x: -2 * math.sqrt(x + 1) + 3, "dom": (-1, 6)}], (-2, 6), (-3, 4.5), 210, 160,
              points=[(-1, 3, True, C1), (1.25, 0, True, C1)],
              labels=[(-1, 3.5, "endpoint (−1, 3)", "start", C1), (1.6, 0.4, "(5/4, 0)", "start", C1)],
              title="y = −2√(x + 1) + 3")
hybrid = graph([{"f": lambda x: x * x, "dom": (-1.6, 1)}, {"f": lambda x: 2 * x - 1, "dom": (1, 2.6), "color": C4}],
               (-1.7, 2.7), (-0.6, 4.4), 210, 150, points=[(1, 1, True, INK)],
               labels=[(-1.4, 3.2, "x²", "start", C1), (2.2, 2.0, "2x − 1", "start", C4), (1.15, 0.6, "(1, 1)", "start")],
               title="joins smoothly at x = 1")
modg = graph([{"f": lambda x: x * x - 4, "dash": True, "color": "#9aa9a7", "width": 1.4},
              {"f": lambda x: abs(x * x - 4)}], (-3.2, 3.2), (-4.5, 6), 210, 150,
             labels=[(0.15, -3.6, "y = x² − 4", "start", "#7b8987"), (0.15, 4.6, "flipped up", "start", C1)],
             title="y = |x² − 4|")

# annotated sine
sin_x = graph([{"f": lambda x: 3 * s(2 * x) - 1}], (-0.3, 2 * PI + 0.3), (-4.8, 3.2), 330, 170,
              asym=[("h", -1)],
              points=[(PI / 4, 2, True, C3), (3 * PI / 4, -4, True, C3)],
              labels=[(PI / 4, 2.4, "max 2", "middle", C3), (3 * PI / 4, -4.6, "min −4", "middle", C3),
                      (2 * PI + 0.2, -0.75, "mean y = −1", "end", C2),
                      (PI / 2, -2.8, "π/2", "middle", "#6b7a78", 8), (PI, 0.35, "π", "middle", "#6b7a78", 8),
                      (3 * PI / 2, -2.8, "3π/2", "middle", "#6b7a78", 8), (2 * PI, 0.35, "2π", "middle", "#6b7a78", 8)],
              title="y = 3 sin(2x) − 1")

tan_g = graph([{"f": lambda x: math.tan(x)}], (-PI, PI), (-4, 4), 210, 150,
              asym=[("v", -PI / 2), ("v", PI / 2)],
              labels=[(-PI / 2, 3.4, "x = −π/2", "end", C2, 8), (PI / 2, 3.4, " x = π/2", "start", C2, 8),
                      (PI, -0.7, "π", "end", "#6b7a78", 8), (-PI, -0.7, "−π", "start", "#6b7a78", 8)],
              title="y = tan x (period π)")

xs = [PI / 18, 5 * PI / 18, 13 * PI / 18, 17 * PI / 18, 25 * PI / 18, 29 * PI / 18]
sol6 = graph([{"f": lambda x: s(3 * x)}], (-0.2, 2 * PI + 0.25), (-1.4, 1.5), 360, 140,
             hlines=[(0.5, C2)],
             points=[(x, 0.5, True, C2) for x in xs],
             labels=[(x, 0.8, str(i + 1), "middle", C2, 9) for i, x in enumerate(xs)]
             + [(2 * PI + 0.2, 0.25, "y = ½", "end", C2), (2 * PI, -0.35, "2π", "middle", "#6b7a78", 8)],
             title="sin(3x) = ½ on [0, 2π): 3 cycles × 2 = 6 crossings")

unit_circle = f"""
<svg viewBox="0 0 230 210" width="230" height="210" class="g">
  <rect x="115" y="10" width="105" height="95" fill="#e8f3f1"/>
  <rect x="10" y="10" width="105" height="95" fill="#fdf3e1"/>
  <rect x="10" y="105" width="105" height="95" fill="#f6e6e4"/>
  <rect x="115" y="105" width="105" height="95" fill="#e7eef8"/>
  <circle cx="115" cy="105" r="78" fill="none" stroke="{INK}" stroke-width="1.4"/>
  <line x1="10" y1="105" x2="220" y2="105" stroke="#8a9896"/>
  <line x1="115" y1="200" x2="115" y2="10" stroke="#8a9896"/>
  <text x="190" y="32" class="q">A</text><text x="190" y="44" class="qs">All +</text>
  <text x="40" y="32" class="q">S</text><text x="40" y="44" class="qs">sin +</text>
  <text x="40" y="182" class="q">T</text><text x="40" y="194" class="qs">tan +</text>
  <text x="190" y="182" class="q">C</text><text x="190" y="194" class="qs">cos +</text>
  <text x="196" y="100" font-size="8" fill="#6b7a78">0, 2π</text>
  <text x="119" y="19" font-size="8" fill="#6b7a78">π/2</text>
  <text x="14" y="100" font-size="8" fill="#6b7a78">π</text>
  <text x="119" y="197" font-size="8" fill="#6b7a78">3π/2</text>
  <line x1="115" y1="105" x2="182.5" y2="66" stroke="{C1}" stroke-width="1.6"/>
  <circle cx="182.5" cy="66" r="3" fill="{C1}"/>
  <text x="150" y="58" font-size="8.5" fill="{C1}" text-anchor="end">(cos θ, sin θ)</text>
  <path d="M135 105 A20 20 0 0 0 132.3 95" fill="none" stroke="{C1}"/>
  <text x="138" y="100" font-size="8" fill="{C1}">θ</text>
</svg>"""

triangle = f"""
<svg viewBox="0 0 200 120" width="200" height="120" class="g">
  <polygon points="20,100 140,100 140,20" fill="#e8f3f1" stroke="{C1}" stroke-width="1.6"/>
  <rect x="130" y="90" width="10" height="10" fill="none" stroke="{C1}"/>
  <text x="80" y="114" text-anchor="middle" font-size="10">adj = 4</text>
  <text x="146" y="64" font-size="10">opp = 3</text>
  <text x="64" y="52" text-anchor="end" font-size="10">hyp = 5</text>
  <text x="38" y="96" font-size="10" fill="{C2}">θ</text>
</svg>"""

machine = f"""
<svg viewBox="0 0 470 70" width="470" height="70" class="g">
  <text x="18" y="40" font-size="13" text-anchor="middle">x</text>
  <line x1="30" y1="36" x2="70" y2="36" stroke="{INK}" marker-end="url(#ar)"/>
  <rect x="74" y="16" width="70" height="40" rx="8" fill="#e7eef8" stroke="{C4}"/>
  <text x="109" y="41" text-anchor="middle" font-size="13" fill="{C4}">g</text>
  <line x1="144" y1="36" x2="214" y2="36" stroke="{INK}" marker-end="url(#ar)"/>
  <text x="179" y="28" text-anchor="middle" font-size="10">g(x)</text>
  <rect x="218" y="16" width="70" height="40" rx="8" fill="#e8f3f1" stroke="{C1}"/>
  <text x="253" y="41" text-anchor="middle" font-size="13" fill="{C1}">f</text>
  <line x1="288" y1="36" x2="340" y2="36" stroke="{INK}" marker-end="url(#ar)"/>
  <text x="380" y="40" text-anchor="middle" font-size="13">f(g(x))</text>
  <text x="179" y="66" text-anchor="middle" font-size="9" fill="{C2}">these outputs must be allowed into f</text>
  <text x="109" y="11" text-anchor="middle" font-size="9" fill="#6b7a78">1st</text>
  <text x="253" y="11" text-anchor="middle" font-size="9" fill="#6b7a78">2nd</text>
</svg>"""

steps = """
<div class="flow">
  <div class="step"><b>1</b> Isolate the trig ratio<span>2 sin(2x) + 1 = 0 → sin(2x) = −½</span></div>
  <div class="arrow">→</div>
  <div class="step"><b>2</b> Change the domain<span>x ∈ [0, 2π] → 2x ∈ [0, 4π]</span></div>
  <div class="arrow">→</div>
  <div class="step"><b>3</b> Base angle → quadrants → add periods<span>base π/6; sin − in Q3, Q4: 7π/6, 11π/6, then +2π: 19π/6, 23π/6</span></div>
  <div class="arrow">→</div>
  <div class="step"><b>4</b> Undo (÷ 2)<span>x = 7π/12, 11π/12, 19π/12, 23π/12</span></div>
</div>"""


def box(kind, title, body):
    return f'<div class="box {kind}"><div class="tag">{kind.upper()}</div><h4>{title}</h4>{body}</div>'


def ex(body, title="Example"):
    return f'<div class="ex"><span class="exl">{title}</span>{body}</div>'


html = f"""<!doctype html>
<html><head><meta charset="utf-8">
<title>Methods 3&amp;4 Formulas Made Easy</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=Karla:wght@400;600;700&display=swap" rel="stylesheet">
<style>
@page {{ size: A4; margin: 14mm 13mm 16mm; }}
:root {{ --teal:#1f6f68; --ink:#1d2b2a; --muted:#5f6e6c; --line:#d5dfdd; --soft:#eef5f4; }}
* {{ box-sizing:border-box; }}
body {{ font-family: Karla, Inter, "DejaVu Sans", sans-serif; color:var(--ink); font-size:10.4pt; line-height:1.42; margin:0; background:#fff; }}
h1,h2,h3,h4 {{ font-family: Fraunces, "DejaVu Serif", serif; margin:0; }}
.head {{ display:flex; align-items:center; gap:14px; border-bottom:2px solid var(--teal); padding-bottom:8px; margin-bottom:10px; }}
.logo {{ width:44px; height:44px; border-radius:10px; background:var(--teal); color:#fff; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:13pt; font-family:Fraunces,serif; }}
.head h1 {{ font-size:19pt; color:var(--teal); }}
.head p {{ margin:2px 0 0; color:var(--muted); font-size:9.5pt; }}
.pill {{ display:inline-block; background:#e7b94a; color:#fff; font-weight:700; font-size:8.5pt; padding:1px 8px; border-radius:5px; margin-left:6px; vertical-align:middle; }}
.legend {{ display:flex; gap:8px; flex-wrap:wrap; margin:6px 0 4px; font-size:9pt; }}
.legend span {{ padding:3px 9px; border-radius:20px; border:1.5px solid; }}
h2 {{ font-size:15pt; margin:16px 0 6px; color:var(--teal); display:flex; align-items:center; gap:8px; break-after:avoid; }}
h2 .num {{ background:var(--teal); color:#fff; border-radius:50%; width:24px; height:24px; display:inline-flex; align-items:center; justify-content:center; font-size:11pt; }}
h3 {{ font-size:11.6pt; margin:12px 0 5px; break-after:avoid; border-left:4px solid #e7b94a; padding-left:7px; }}
p {{ margin:4px 0; }}
table {{ border-collapse:collapse; width:100%; margin:4px 0 6px; font-size:9.8pt; break-inside:avoid; }}
th {{ background:var(--soft); text-align:left; font-weight:700; }}
th, td {{ border:1px solid var(--line); padding:4px 7px; vertical-align:middle; }}
td.c, th.c {{ text-align:center; }}
.m {{ font-family:"DejaVu Sans Mono", monospace; font-size:9.3pt; color:#7a2e22; white-space:nowrap; }}
.grid2 {{ display:grid; grid-template-columns:1fr 1fr; gap:10px; align-items:start; }}
.figrow {{ display:flex; gap:6px; flex-wrap:wrap; justify-content:center; margin:4px 0; break-inside:avoid; }}
.fig {{ text-align:center; }}
.fig .cap {{ font-size:8.6pt; color:var(--muted); }}
svg.g {{ background:#fbfdfc; border:1px solid var(--line); border-radius:6px; font-family:Karla,Inter,sans-serif; }}
svg.g text {{ fill:var(--ink); }}
svg.g text.gt {{ font-weight:700; }}
svg.g text.q {{ font-family:Fraunces,serif; font-size:20px; font-weight:700; text-anchor:middle; fill:var(--teal); }}
svg.g text.qs {{ font-size:9px; text-anchor:middle; }}
.box {{ border:1px solid var(--line); border-left:5px solid; border-radius:7px; padding:6px 10px 7px; margin:7px 0; break-inside:avoid; background:#fff; }}
.box .tag {{ font-size:7.8pt; letter-spacing:.12em; font-weight:700; }}
.box h4 {{ font-size:10.6pt; margin:1px 0 3px; }}
.box p {{ margin:2px 0; }}
.trick {{ border-left-color:#d59a1c; background:#fffaf0; }} .trick .tag {{ color:#b7791f; }}
.trap  {{ border-left-color:#c0392b; background:#fff6f5; }} .trap .tag  {{ color:#c0392b; }}
.check {{ border-left-color:#1f6f68; background:#f3faf8; }} .check .tag {{ color:#1f6f68; }}
.ex {{ background:#f2f6fc; border:1px dashed #9cb4d6; border-radius:7px; padding:5px 9px; margin:5px 0; break-inside:avoid; }}
.exl {{ display:inline-block; background:#2b5d9c; color:#fff; font-size:7.8pt; font-weight:700; letter-spacing:.08em; padding:1px 7px; border-radius:4px; margin-right:6px; text-transform:uppercase; }}
.flow {{ display:flex; align-items:stretch; gap:4px; margin:6px 0; break-inside:avoid; }}
.flow .step {{ flex:1; border:1.5px solid var(--teal); border-radius:8px; padding:6px; font-size:9.2pt; background:var(--soft); }}
.flow .step b {{ display:inline-flex; width:18px; height:18px; border-radius:50%; background:var(--teal); color:#fff; align-items:center; justify-content:center; font-size:8.5pt; margin-right:3px; }}
.flow .step span {{ display:block; margin-top:3px; color:var(--muted); font-size:8.6pt; }}
.flow .arrow {{ display:flex; align-items:center; color:var(--teal); font-weight:700; }}
.try {{ border:2px solid var(--teal); border-radius:9px; padding:7px 11px; margin:10px 0; break-inside:avoid; }}
.try h4 {{ color:var(--teal); font-size:10.8pt; }}
.try ol {{ margin:4px 0 0; padding-left:20px; }}
.try li {{ margin:3px 0; }}
.ans {{ font-size:9.4pt; }}
.ans h4 {{ margin-top:6px; }}
.pb {{ break-before:page; }}
.foot {{ margin-top:14px; border-top:1px solid var(--line); padding-top:5px; font-size:8.4pt; color:var(--muted); text-align:center; }}
.small {{ font-size:9pt; color:var(--muted); }}
{PROB_CSS}
</style></head><body>
<svg width="0" height="0" style="position:absolute"><defs>
<marker id="ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="#8a9896"/></marker>
</defs></svg>

<div class="head">
  <div class="logo">PhD</div>
  <div>
    <h1>Formulas &amp; Tricks — Made Easy <span class="pill">Units 3 &amp; 4</span></h1>
    <p>VCE Mathematical Methods Units 3 &amp; 4 · Functions · Trig · Transformations · Coordinate geometry · Calculus · Probability · Statistics · Algebra · Algorithms · Exam technique</p>
  </div>
</div>
<p>This is the short, friendly version of the big formula sheet. Every rule comes with a picture, a table or a worked example. Look for the coloured boxes:</p>
<div class="legend">
  <span style="border-color:#d59a1c;background:#fffaf0">TRICK — saves time</span>
  <span style="border-color:#c0392b;background:#fff6f5">TRAP — where marks are lost</span>
  <span style="border-color:#1f6f68;background:#f3faf8">CHECK — catch your own mistakes</span>
  <span style="border-color:#2b5d9c;background:#f2f6fc">EXAMPLE — see it worked out</span>
</div>

<!-- ======================= 1 ======================= -->
<h2><span class="num">1</span> Functions and graphs</h2>

<h3>Interval notation — square bracket or round bracket?</h3>
<table>
<tr><th>Write</th><th>Means</th><th>On a graph</th><th>Example</th></tr>
<tr><td class="m">[a, b]</td><td>both ends included</td><td>● filled dots at both ends</td><td class="m">[1, 4] → 1 ≤ x ≤ 4</td></tr>
<tr><td class="m">(a, b)</td><td>both ends left out</td><td>○ open circles at both ends</td><td class="m">(1, 4) → 1 &lt; x &lt; 4</td></tr>
<tr><td class="m">[a, b)</td><td>only a included</td><td>● at a, ○ at b</td><td class="m">[1, 4) → 1 ≤ x &lt; 4</td></tr>
<tr><td class="m">R \\ {{2}}</td><td>every real number except 2</td><td>hole / asymptote at x = 2</td><td class="m">(−∞, 2) ∪ (2, ∞)</td></tr>
</table>
<p class="small">∞ always gets a round bracket — you can never "reach" infinity.</p>

<h3>Maximal (largest possible) domain</h3>
<table>
<tr><th>If the rule has…</th><th>You need…</th><th>Example</th><th>Domain</th></tr>
<tr><td>a square root √(g(x))</td><td class="m">g(x) ≥ 0</td><td class="m">√(x − 3)</td><td class="m">[3, ∞)</td></tr>
<tr><td>a fraction 1 / g(x)</td><td class="m">g(x) ≠ 0</td><td class="m">1 / (x + 5)</td><td class="m">R \\ {{−5}}</td></tr>
<tr><td>a log  log<sub>e</sub>(g(x))</td><td class="m">g(x) &gt; 0</td><td class="m">log<sub>e</sub>(2 − x)</td><td class="m">(−∞, 2)</td></tr>
<tr><td>more than one of these</td><td>all of them at once</td><td colspan="2">see the example below</td></tr>
</table>
{ex('<span class="m">y = √(x + 2) + 1/(x − 1)</span>. &nbsp;Root: x ≥ −2. &nbsp;Fraction: x ≠ 1. &nbsp;Together: <b class="m">[−2, 1) ∪ (1, ∞)</b>.')}

<h3>Polynomials — shape from the degree</h3>
<p>A polynomial of degree <b>n</b> has <b>at most n</b> x-intercepts and <b>at most n − 1</b> turning points. Only the <b>leading term</b> decides where the arms go:</p>
<div class="figrow">{end_beh}</div>
<table>
<tr><th>Factor</th><th class="c">Picture near x = a</th><th>What the graph does</th><th>Sign changes?</th></tr>
<tr><td class="m">(x − a)</td><td class="c">{mult1}</td><td><b>cuts</b> straight through</td><td>yes</td></tr>
<tr><td class="m">(x − a)²</td><td class="c">{mult2}</td><td><b>touches</b> and turns back (turning point)</td><td>no</td></tr>
<tr><td class="m">(x − a)³</td><td class="c">{mult3}</td><td><b>flattens</b> then goes through (stationary point of inflection)</td><td>yes</td></tr>
</table>
<p class="small">Rule of thumb: <b>even</b> power → touch, <b>odd</b> power → cross.</p>
{ex('<span class="m">y = (x − 1)²(x + 3)</span>: touches the x-axis at x = 1, cuts at x = −3. It is a cubic but has only <b>2 distinct</b> zeros.')}

<h3>Quadratics  y = ax² + bx + c</h3>
<table>
<tr><th>What you want</th><th>Formula</th><th>Quick note</th></tr>
<tr><td>x of the turning point</td><td class="m">x = −b / (2a)</td><td>then substitute to get y</td></tr>
<tr><td>turning point form</td><td class="m">y = a(x − h)² + k → TP (h, k)</td><td>watch the minus: y = 2(x + 3)² − 1 has TP (−3, −1)</td></tr>
<tr><td>quadratic formula</td><td class="m">x = (−b ± √(b² − 4ac)) / (2a)</td><td>leave surds exact</td></tr>
<tr><td>axis of symmetry</td><td class="m">x = (p + q) / 2</td><td>halfway between the x-intercepts p and q</td></tr>
<tr><td>discriminant</td><td class="m">Δ = b² − 4ac</td><td>tells you <b>how many</b> solutions — see pictures</td></tr>
</table>
<div class="figrow">{disc}</div>
{box('trick', 'Use the discriminant — do not solve', '<p>"For what k is the line a tangent?" → set the rules equal, collect into ax² + bx + c = 0, then put <b>Δ = 0</b>. (Δ &gt; 0: two intersections, Δ &lt; 0: none.) No need to actually solve the quadratic.</p>')}

<h3>Hyperbola, truncus and square-root graphs</h3>
<table>
<tr><th>Graph</th><th>Rule</th><th>Asymptotes / endpoint</th><th>Domain</th><th>Range</th></tr>
<tr><td>Hyperbola</td><td class="m">y = a/(x − h) + k</td><td>x = h, y = k</td><td class="m">R \\ {{h}}</td><td class="m">R \\ {{k}}</td></tr>
<tr><td>Truncus</td><td class="m">y = a/(x − h)² + k</td><td>x = h, y = k</td><td class="m">R \\ {{h}}</td><td class="m">(k, ∞) if a &gt; 0</td></tr>
<tr><td>Square root</td><td class="m">y = a√(x − h) + k</td><td>endpoint (h, k)</td><td class="m">[h, ∞)</td><td class="m">[k, ∞) if a &gt; 0<br>(−∞, k] if a &lt; 0</td></tr>
</table>
<div class="figrow">{hyper}{trunc}{sqrtg}</div>
{ex('<span class="m">y = 2/(x − 3) + 4</span> &nbsp;x-intercept: 2/(x − 3) = −4 → x − 3 = −½ → x = 5/2. &nbsp;y-intercept: 2/(−3) + 4 = 10/3.')}
{box('trick', 'Split the numerator instead of long division', '<p>Make the top contain the bottom: <span class="m">(3x + 1)/(x − 2) = (3(x − 2) + 7)/(x − 2) = 3 + 7/(x − 2)</span>. Now you can read the asymptotes straight off: <b>x = 2</b> and <b>y = 3</b>.</p>')}
{box('check', 'Endpoint or asymptote? Pick the right bracket', '<p>A square-root endpoint <b>is</b> reached → square bracket: range of y = −2√(x + 1) + 3 is <span class="m">(−∞, 3]</span>. An asymptote is <b>never</b> reached → round bracket / "\\": range of the truncus above is <span class="m">(3, ∞)</span>.</p>')}

<h3>Hybrid (piecewise) functions</h3>
<div class="grid2">
<div>
<table>
<tr><th>To be…</th><th>Check at the join x = a</th></tr>
<tr><td><b>continuous</b> (no gap)</td><td>left value = right value = f(a)</td></tr>
<tr><td><b>differentiable</b> (smooth, no corner)</td><td>continuous <b>and</b> left gradient = right gradient</td></tr>
</table>
{ex('f(x) = x² for x ≤ 1, &nbsp;2x − 1 for x &gt; 1.<br>Values: 1² = 1 and 2(1) − 1 = 1 ✓ &nbsp;Gradients: 2x = 2 and 2 ✓ → smooth join.<br>If it were x² and x: values match (1 = 1) but gradients 2 ≠ 1 → a <b>corner</b>, not differentiable.')}
</div>
<div class="fig">{hybrid}</div>
</div>

<h3>Modulus |x| and odd / even functions</h3>
<div class="grid2">
<div>
<table>
<tr><th>Type</th><th>Rule</th><th>Example</th></tr>
<tr><td>equation</td><td class="m">|x − a| = b → x = a ± b</td><td class="m">|x − 2| = 5 → x = 7 or −3</td></tr>
<tr><td>"less than"</td><td class="m">|x| &lt; a ⇔ −a &lt; x &lt; a</td><td class="m">|x| &lt; 3 → (−3, 3)</td></tr>
<tr><td>"greater than"</td><td class="m">|x| &gt; a ⇔ x &lt; −a or x &gt; a</td><td class="m">two separate pieces</td></tr>
<tr><td>graph of |f(x)|</td><td colspan="2">flip everything <b>below</b> the x-axis up</td></tr>
<tr><td>graph of f(|x|)</td><td colspan="2">keep x ≥ 0, mirror it in the y-axis</td></tr>
</table>
</div>
<div class="fig">{modg}</div>
</div>
<table>
<tr><th>Even function</th><th>Odd function</th></tr>
<tr><td><span class="m">f(−x) = f(x)</span> — mirror image in the y-axis. e.g. x², cos x, |x|</td><td><span class="m">f(−x) = −f(x)</span> — same after a half-turn about the origin. e.g. x³, sin x, 1/x</td></tr>
</table>

{EXTRA_S1}
{box('trap', 'Double factor touches, triple factor flattens', '<p>At (x − a)² the curve turns back. At (x − a)³ it flattens and <b>keeps going</b>. Students often draw a turning point at a triple factor — don\'t.</p>')}
{box('check', 'Count features against the degree', '<p>A degree-n polynomial can\'t have more than n x-intercepts or more than n − 1 turning points. A quartic drawn with 4 turning points is wrong on sight.</p>')}

<div class="try">
<h4>Try it yourself — Section 1</h4>
<ol>
<li>Find the maximal domain of <span class="m">y = √(4 − x) + 1/(x + 1)</span>.</li>
<li>Find the asymptotes of <span class="m">y = (2x + 5)/(x + 1)</span>. (Hint: split the numerator.)</li>
<li>Describe what <span class="m">y = (x + 2)²(x − 1)³</span> does at x = −2 and at x = 1.</li>
</ol>
</div>

<!-- ======================= 2 ======================= -->
<h2 class="pb"><span class="num">2</span> Trigonometric functions</h2>

<h3>Radians and exact values</h3>
<p><span class="m">π rad = 180°</span> &nbsp;·&nbsp; degrees → radians: × π/180 &nbsp;·&nbsp; radians → degrees: × 180/π</p>
<table>
<tr><th>θ</th><th class="c">0</th><th class="c">π/6 (30°)</th><th class="c">π/4 (45°)</th><th class="c">π/3 (60°)</th><th class="c">π/2 (90°)</th></tr>
<tr><th>sin θ</th><td class="c">0</td><td class="c">1/2</td><td class="c">√2/2</td><td class="c">√3/2</td><td class="c">1</td></tr>
<tr><th>cos θ</th><td class="c">1</td><td class="c">√3/2</td><td class="c">√2/2</td><td class="c">1/2</td><td class="c">0</td></tr>
<tr><th>tan θ</th><td class="c">0</td><td class="c">√3/3 (= 1/√3)</td><td class="c">1</td><td class="c">√3</td><td class="c">undefined</td></tr>
</table>
{box('trick', 'Remember the sin row in 5 seconds', '<p>Write <span class="m">√0/2, √1/2, √2/2, √3/2, √4/2</span> → 0, ½, √2/2, √3/2, 1. The cos row is the <b>same numbers backwards</b>. tan = sin ÷ cos.</p>')}

<h3>The unit circle and the quadrants (ASTC)</h3>
<div class="grid2">
<div class="fig">{unit_circle}<div class="cap">"<b>A</b>ll <b>S</b>tudents <b>T</b>ake <b>C</b>alculus" — which ratio is positive</div></div>
<div>
<table>
<tr><th>Quadrant</th><th>Angle in terms of base angle θ</th><th>Positive</th></tr>
<tr><td>1 (0 to π/2)</td><td class="m">θ</td><td>all</td></tr>
<tr><td>2 (π/2 to π)</td><td class="m">π − θ</td><td>sin only</td></tr>
<tr><td>3 (π to 3π/2)</td><td class="m">π + θ</td><td>tan only</td></tr>
<tr><td>4 (3π/2 to 2π)</td><td class="m">2π − θ</td><td>cos only</td></tr>
</table>
{ex('sin(7π/6): 7π/6 = π + π/6 → quadrant 3, base angle π/6. sin is negative there, so <b>sin(7π/6) = −1/2</b>.')}
<p class="small">Also useful: <span class="m">sin(−θ) = −sin θ</span>, <span class="m">cos(−θ) = cos θ</span>, <span class="m">sin(π/2 − θ) = cos θ</span>, <span class="m">sin²θ + cos²θ = 1</span>, <span class="m">tan θ = sin θ / cos θ</span>.</p>
</div>
</div>

<h3>Finding one ratio from another</h3>
<div class="grid2">
<div>
{ex('sin θ = 3/5 and θ ∈ (π/2, π). Find cos θ and tan θ.<br>① Draw the triangle: opp 3, hyp 5 → adj 4 (3-4-5).<br>② Quadrant 2: cos is negative → <b>cos θ = −4/5</b>.<br>③ <b>tan θ = (3/5) ÷ (−4/5) = −3/4</b>.')}
</div>
<div class="fig">{triangle}<div class="cap">the triangle gives the size, the quadrant gives the sign</div></div>
</div>
{box('trap', 'The identity gives the size, the quadrant gives the sign', '<p>cos²θ = 1 − 9/25 = 16/25 gives cos θ = <b>±</b>4/5. Only the given domain tells you which sign. Writing +4/5 loses the mark even though the arithmetic is right.</p>')}

<h3>Graphs of sine and cosine:  y = a sin(n(x + b)) + c</h3>
<div class="grid2">
<div>
<table>
<tr><th>Feature</th><th>Formula</th><th>For y = 3 sin(2x) − 1</th></tr>
<tr><td>amplitude</td><td class="m">|a|</td><td>3</td></tr>
<tr><td>period</td><td class="m">2π / |n|</td><td>2π/2 = π</td></tr>
<tr><td>mean (centre) line</td><td class="m">y = c</td><td>y = −1</td></tr>
<tr><td>range</td><td class="m">[c − |a|, c + |a|]</td><td>[−4, 2]</td></tr>
<tr><td>cycles in [0, 2π]</td><td class="m">2π ÷ period</td><td>2 cycles</td></tr>
</table>
<p class="small">Key points are a <b>quarter-period apart</b>: sine starts at the mean line going up; cosine starts at a max (if a &gt; 0).</p>
</div>
<div class="fig">{sin_x}</div>
</div>

<h3>The tangent graph  y = a tan(n(x + b)) + c</h3>
<div class="grid2">
<div>
<table>
<tr><th>Feature</th><th>Rule</th></tr>
<tr><td>period</td><td class="m">π / |n|</td></tr>
<tr><td>asymptotes of tan x</td><td class="m">x = π/2 + kπ, k ∈ Z</td></tr>
<tr><td>x-intercepts of tan x</td><td class="m">x = kπ, k ∈ Z</td></tr>
<tr><td>amplitude</td><td><b>none</b> — range is R</td></tr>
</table>
{ex('y = tan(2x): period π/2. Asymptotes: 2x = π/2 + kπ → x = π/4 + kπ/2.')}
</div>
<div class="fig">{tan_g}</div>
</div>

<h3>Solving a trig equation on a restricted domain — 4 steps</h3>
<p>Example: solve <span class="m">2 sin(2x) + 1 = 0</span> for <span class="m">x ∈ [0, 2π]</span>.</p>
{steps}
{box('trick', 'Change the domain, not the answers', '<p>Convert the domain first (2x ∈ [0, 4π]), find <b>every</b> answer for 2x in that bigger interval, then divide by 2 at the very end. Solving for x first and adding periods later is where solutions go missing.</p>')}

<h3>How many solutions should I expect?</h3>
<table>
<tr><th>Equation (over one interval of length 2π)</th><th>Number of solutions</th><th>Example on [0, 2π)</th></tr>
<tr><td class="m">sin(nx) = k or cos(nx) = k, with |k| &lt; 1</td><td><b>2n</b></td><td class="m">sin(3x) = ½ → 6 solutions</td></tr>
<tr><td class="m">sin(nx) = ±1 or cos(nx) = ±1</td><td><b>n</b> (one per cycle)</td><td class="m">sin(2x) = 1 → 2 solutions</td></tr>
<tr><td class="m">tan(nx) = k (any k)</td><td><b>n per π</b>, so 2n per 2π</td><td class="m">tan x = −√3 → 2 solutions</td></tr>
<tr><td class="m">sin or cos = k with |k| &gt; 1</td><td><b>0</b></td><td class="m">sin x = 2 → no solution</td></tr>
</table>
<div class="figrow">{sol6}</div>
{ex('sin(3x) = ½ on [0, 2π): 3x ∈ [0, 6π). Base angle π/6, sin + in Q1, Q2:<br>3x = π/6, 5π/6, 13π/6, 17π/6, 25π/6, 29π/6 → <b>x = π/18, 5π/18, 13π/18, 17π/18, 25π/18, 29π/18</b> — six answers, matching the graph. <b>If you have fewer, you dropped some.</b>')}
{box('check', 'Range check kills impossible equations', '<p>y = 3 sin(2x) − 1 only takes values in [−4, 2]. So <span class="m">3 sin(2x) − 1 = 3</span> has <b>no solution</b> — check this before you start solving.</p>')}

<h3>General solutions (n ∈ Z)</h3>
<table>
<tr><th>Equation</th><th>General solution</th><th>Example</th></tr>
<tr><td class="m">sin x = a</td><td class="m">x = 2nπ + sin⁻¹(a) or x = (2n + 1)π − sin⁻¹(a)</td><td class="m">sin x = ½ → x = 2nπ + π/6 or (2n+1)π − π/6</td></tr>
<tr><td class="m">cos x = a</td><td class="m">x = 2nπ ± cos⁻¹(a)</td><td class="m">cos x = ½ → x = 2nπ ± π/3</td></tr>
<tr><td class="m">tan x = a</td><td class="m">x = nπ + tan⁻¹(a)</td><td class="m">tan x = 1 → x = nπ + π/4</td></tr>
</table>
{box('check', 'Put n = 0, 1, −1 back in', '<p>Always write <b>n ∈ Z</b>. Then substitute n = 0, 1, −1 — the values that land in the domain should match your restricted-domain answers.</p>')}
{box('trap', 'Factorise before you read the translation', '<p><span class="m">sin(2x − π/3)</span> is <b>not</b> a shift of π/3. Write it as <span class="m">sin(2(x − π/6))</span>: the shift is <b>π/6 to the right</b>. Any time n ≠ 1, take n out of the bracket first.</p>')}

{EXTRA_S2}
<div class="try">
<h4>Try it yourself — Section 2</h4>
<ol>
<li>How many solutions does <span class="m">cos(2x) = 0.3</span> have for x ∈ [0, 2π]?</li>
<li>Solve <span class="m">cos x = −½</span> for x ∈ [0, 2π].</li>
<li>State the amplitude, period and range of <span class="m">y = −2 cos(3x) + 5</span>.</li>
</ol>
</div>

<!-- ======================= 3 ======================= -->
<h2 class="pb"><span class="num">3</span> Composite functions and transformations</h2>

<h3>Composite functions f(g(x)) — think of two machines</h3>
<div class="figrow">{machine}</div>
<table>
<tr><th>Fact</th><th>Rule</th><th>What it means</th></tr>
<tr><td>Order</td><td class="m">f(g(x))</td><td>do <b>g first</b>, then f (also written f ∘ g)</td></tr>
<tr><td>Exists when</td><td class="m">ran g ⊆ dom f</td><td>everything g puts out must be allowed into f</td></tr>
<tr><td>Domain</td><td class="m">dom f(g(x)) = dom g</td><td>after any restriction you had to make</td></tr>
<tr><td>Not symmetric</td><td class="m">f(g(x)) ≠ g(f(x))</td><td>one can exist while the other does not</td></tr>
</table>
<div class="grid2">
{ex('f(x) = √x, g(x) = x − 3 (dom R).<br>ran g = R, dom f = [0, ∞). R ⊄ [0, ∞) → f(g(x)) <b>does not exist</b>.<br><b>Fix:</b> restrict dom g to [3, ∞). Then ran g = [0, ∞) ✓ and f(g(x)) = √(x − 3).', 'Example — it fails, then fix it')}
{ex('f(x) = x², g(x) = x − 1, dom g = [0, 4].<br>Step 1: ran g = [−1, 3].<br>Step 2: square that set → <b>[0, 9]</b>, <b>not</b> [1, 9], because x = 1 gives 0, the minimum.', 'Example — range of a composite')}
</div>
{box('trap', 'It is ran g ⊆ dom f, not dom g ⊆ dom f', '<p>The test is on the <b>outputs</b> of the inside function. Write down ran g, write down dom f, then compare those two sets.</p>')}

<h3>The transformation rule  y = a f(b(x + c)) + d</h3>
<table>
<tr><th>Letter</th><th>Effect</th><th>Exam wording</th><th>Example from y = f(x)</th></tr>
<tr><td class="m">a</td><td>multiplies every <b>y</b> by a (a &lt; 0 also flips)</td><td>dilation of factor |a| from the x-axis</td><td class="m">y = 3f(x): 3 × taller</td></tr>
<tr><td class="m">b</td><td><b>divides</b> every <b>x</b> by b (b &lt; 0 also flips)</td><td>dilation of factor 1/|b| from the y-axis</td><td class="m">y = f(2x): squashed, factor ½</td></tr>
<tr><td class="m">c</td><td>moves left by c</td><td>translation of c units in the negative x direction</td><td class="m">y = f(x + 3): 3 left</td></tr>
<tr><td class="m">d</td><td>moves up by d</td><td>translation of d units in the positive y direction</td><td class="m">y = f(x) + 2: 2 up</td></tr>
</table>
<p>Image of a point: <span class="m">(p, q) → (p/b − c, aq + d)</span>. &nbsp;<b>Order:</b> dilations and reflections first, translations last.</p>
<table>
<tr><th colspan="3">Example: y = 2f(3(x − 1)) + 5 sends the point (2, 4) to …</th></tr>
<tr><th>Coordinate</th><th>Working</th><th>Result</th></tr>
<tr><td>x</td><td>divide by 3, then add 1 &nbsp;→ 2/3 + 1</td><td><b>5/3</b></td></tr>
<tr><td>y</td><td>multiply by 2, then add 5 &nbsp;→ 2 × 4 + 5</td><td><b>13</b></td></tr>
<tr><td colspan="2">Check with f(x) = x²: &nbsp;2(3(5/3 − 1))² + 5 = 2(2)² + 5</td><td>= 13 ✓</td></tr>
</table>
{box('trap', 'Dilation factors from the y-axis go upside down', '<p>f(2x) is a dilation of factor <b>½</b> from the y-axis, not 2 — the graph is squashed towards the y-axis. Vertical ones read straight off: 2f(x) is factor 2 from the x-axis.</p>')}
{box('trick', 'Asymptotes and endpoints move too', '<p>Apply the point rule to x = h and y = k as well. For y = 1/x → y = 2/(x − 3) + 4, the asymptotes x = 0, y = 0 move to <b>x = 3, y = 4</b>. Fastest way to sketch any transformed graph.</p>')}

{EXTRA_S3}
<div class="try">
<h4>Try it yourself — Section 3</h4>
<ol>
<li>f(x) = √x and g(x) = x + 2 with dom g = R. Does f(g(x)) exist? If not, give the largest domain of g that fixes it.</li>
<li>Find the image of the point (1, 3) under <span class="m">y = −f(2(x + 1)) + 4</span>.</li>
<li>Describe the transformations from y = sin x to <span class="m">y = sin(2x − π/3)</span>.</li>
{S3_TRY}
</ol>
</div>

{CALC}
{PROB}
{EXTRA}

<div class="ans pb">
<h3>Answers — Try it yourself</h3>
<div class="grid2">
<div>
<h4>Section 1</h4>
<p>1. x ≤ 4 and x ≠ −1 → <span class="m">(−∞, −1) ∪ (−1, 4]</span></p>
<p>2. (2x + 5)/(x + 1) = 2 + 3/(x + 1) → <b>x = −1, y = 2</b></p>
<p>3. x = −2: touches (turning point). x = 1: flattens and passes through (stationary point of inflection).</p>
<h4>Section 2</h4>
<p>1. 2x ∈ [0, 4π] → 2 cycles × 2 = <b>4</b> solutions</p>
<p>2. Base angle π/3, cos − in Q2, Q3 → <b>x = 2π/3, 4π/3</b></p>
<p>3. Amplitude 2, period 2π/3, range [3, 7]</p>
</div>
<div>
<h4>Section 3</h4>
<p>1. ran g = R ⊄ [0, ∞), so no. Restrict to <b>dom g = [−2, ∞)</b>.</p>
<p>2. x: 1 ÷ 2 − 1 = −½; &nbsp;y: −3 + 4 = 1 → <b>(−½, 1)</b></p>
<p>3. sin(2(x − π/6)): dilation of factor ½ from the y-axis, then translation of π/6 units in the positive direction of the x-axis.</p>
{S3_ANS}
</div>
</div>
<div class="grid2">{CALC_ANS}</div>
<div class="grid2">{PROB_ANS}</div>
<div class="grid2">{EXTRA_ANS}</div>
</div>

<div class="foot">PhDTutor · VCE Mathematical Methods Units 3 &amp; 4 · Formulas &amp; Tricks Made Easy (Sections 1–17)</div>
</body></html>
"""

out = pathlib.Path(__file__).parent.parent / "Methods-3-4-Formulas-Made-Easy.html"
out.write_text(html, encoding="utf-8")
print("wrote", out)
