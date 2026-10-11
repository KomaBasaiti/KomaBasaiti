"""Extra content for sections 1–3, plus coordinate geometry and calculus (sections 4–8)."""
import math

from svg import graph, C1, C2, C3, C4, INK
from prob import box, ex

E = math.e
ln = math.log
MUTED = "#6b7a78"

# ---------------------------------------------------------------- extras for 1–3
EXTRA_S1 = f"""
<h3>Combining functions: sums, products and power functions</h3>
<div class="grid2">
<table>
<tr><th>Combination</th><th>Rule</th></tr>
<tr><td>(f + g)(x), (fg)(x)</td><td class="m">domain = dom f ∩ dom g</td></tr>
<tr><td>even × even, odd × odd</td><td>even</td></tr>
<tr><td>even × odd</td><td>odd</td></tr>
<tr><td>even + odd (e.g. x³ + x²)</td><td>usually <b>neither</b></td></tr>
</table>
<table>
<tr><th>Power function</th><th>Domain</th><th>Range</th></tr>
<tr><td class="m">y = √x = x^(1/2)</td><td class="m">[0, ∞)</td><td class="m">[0, ∞)</td></tr>
<tr><td class="m">y = ∛x = x^(1/3)</td><td class="m">R</td><td class="m">R</td></tr>
<tr><td class="m">y = 1/x = x⁻¹</td><td class="m">R \\ {{0}}</td><td class="m">R \\ {{0}}</td></tr>
<tr><td class="m">y = 1/x² = x⁻²</td><td class="m">R \\ {{0}}</td><td class="m">(0, ∞)</td></tr>
</table>
</div>
{ex('dom(√x + √(2 − x)): √x needs x ≥ 0, √(2 − x) needs x ≤ 2. Overlap (∩, not ∪) → <b class="m">[0, 2]</b>.')}
<p class="small">Tip: rewrite roots and fractions in index form (√x = x^½, 1/x² = x⁻²) before you differentiate or integrate.</p>
"""

EXTRA_S2 = f"""
{box('trick', 'Double-angle formulas (handy, but optional in Methods)', '<p><span class="m">sin(2θ) = 2 sin θ cos θ</span> &nbsp;·&nbsp; <span class="m">cos(2θ) = cos²θ − sin²θ = 1 − 2sin²θ = 2cos²θ − 1</span>. Methods questions are written so you can avoid these, so never rely on them.</p>')}
<h3>Transforming trig graphs — what changes what</h3>
<table>
<tr><th>Change</th><th>Affects</th><th>Example</th></tr>
<tr><td>a (stretch up/down)</td><td>amplitude and range only</td><td class="m">y = −2 sin x: amplitude 2, flipped</td></tr>
<tr><td>n (stretch sideways)</td><td><b>period only</b></td><td class="m">y = sin 3x: period 2π/3</td></tr>
<tr><td>b (shift sideways)</td><td>neither period nor range</td><td class="m">y = sin(x − π/4): π/4 right</td></tr>
<tr><td>c (shift up/down)</td><td>range and mean line</td><td class="m">y = sin x + 2: range [1, 3]</td></tr>
</table>
"""

inv_fig = graph([{"f": lambda x: math.exp(x), "dom": (-3, 1.9)},
                 {"f": lambda x: math.log(x) if x > 0 else float("nan"), "dom": (0.03, 6), "color": C4},
                 {"f": lambda x: x, "dash": True, "color": "#9aa9a7", "width": 1.2}],
                (-3, 6), (-3, 6), 220, 200,
                points=[(0, 1, True, C1), (1, 0, True, C4), (1, E, True, C1), (E, 1, True, C4)],
                labels=[(1.5, 5.6, "y = eˣ", "end", C1), (5.9, 2.1, "y = logₑ x", "end", C4),
                        (5.4, 4.7, "y = x", "end", MUTED), (0.2, 1.3, "(0, 1)", "start", C1),
                        (1.1, -0.6, "(1, 0)", "start", C4), (1.15, 2.8, "(1, e)", "start", C1), (2.75, 0.55, "(e, 1)", "start", C4)],
                title="inverses reflect in y = x")

EXTRA_S3 = f"""
<h3>Describing transformations in words</h3>
<table>
<tr><th>Rule change</th><th>Correct exam wording</th></tr>
<tr><td class="m">y = 3f(x)</td><td>dilation of factor 3 <b>from the x-axis</b> (= parallel to the y-axis)</td></tr>
<tr><td class="m">y = f(2x)</td><td>dilation of factor ½ <b>from the y-axis</b> (= parallel to the x-axis)</td></tr>
<tr><td class="m">y = −f(x)</td><td>reflection <b>in</b> the x-axis (not "about" or "across")</td></tr>
<tr><td class="m">y = f(−x)</td><td>reflection in the y-axis</td></tr>
<tr><td class="m">y = f(x − 2)</td><td>translation of 2 units in the positive direction of the x-axis</td></tr>
</table>
<p class="small">List dilations and reflections first, then translations. Matrix form (same information): <span class="m">[x′, y′] = [[1/b, 0], [0, a]]·[x, y] + [−c, d]</span>.</p>

<h3>Inverse functions f⁻¹</h3>
<div class="grid2">
<div>
<table>
<tr><th>Fact</th><th>Rule</th></tr>
<tr><td>Exists only if</td><td>f is <b>one-to-one</b> (passes the horizontal line test)</td></tr>
<tr><td>Find the rule</td><td>swap x and y, then solve for y</td></tr>
<tr><td>Domain and range</td><td class="m">dom f⁻¹ = ran f, ran f⁻¹ = dom f</td></tr>
<tr><td>Graph</td><td>reflect y = f(x) in the line y = x</td></tr>
<tr><td>Points, asymptotes</td><td>(a, b) → (b, a); x = h ↔ y = h</td></tr>
<tr><td>Check</td><td class="m">f(f⁻¹(x)) = x</td></tr>
</table>
</div>
<div class="fig">{inv_fig}</div>
</div>
<table>
<tr><th>f(x)</th><th>Swap and solve</th><th>f⁻¹(x)</th><th>dom f⁻¹ (= ran f)</th></tr>
<tr><td class="m">2x − 5</td><td class="m">x = 2y − 5</td><td class="m">(x + 5)/2</td><td class="m">R</td></tr>
<tr><td class="m">(x − 1)³ + 2</td><td class="m">x − 2 = (y − 1)³</td><td class="m">(x − 2)^(1/3) + 1</td><td class="m">R</td></tr>
<tr><td class="m">e^(2x) − 1</td><td class="m">x + 1 = e^(2y)</td><td class="m">½ logₑ(x + 1)</td><td class="m">(−1, ∞)</td></tr>
<tr><td class="m">x², x ≥ 0</td><td class="m">x = y², y ≥ 0</td><td class="m">√x</td><td class="m">[0, ∞)</td></tr>
</table>
{box('trap', 'f⁻¹ is NOT 1 ÷ f', '<p>The −1 is not a power. f(x) = x + 2 has f⁻¹(x) = x − 2, not 1/(x + 2). Same with sin⁻¹ (inverse sine) vs 1/sin.</p>')}
{box('trap', 'Not one-to-one? Restrict the domain first', '<p>f(x) = x² − 4x + 1 turns at x = 2, so restrict to [2, ∞) or (−∞, 2]. Then recompute the range on that piece — it becomes the domain of f⁻¹.</p>')}
{box('trick', 'Where do f and f⁻¹ meet?', '<p>If f is <b>increasing</b>, solve f(x) = x: e.g. √(x + 2) = x gives (2, 2). If f is decreasing they can also meet off the line y = x — then solve f(x) = f⁻¹(x).</p>')}
"""

S3_TRY = '<li>Find f⁻¹ for f(x) = e^(x) + 3 and state its domain.</li>'
S3_ANS = '<p>4. Swap: x = eʸ + 3 → <b>f⁻¹(x) = logₑ(x − 3)</b>, domain = ran f = <b>(3, ∞)</b></p>'

# ---------------------------------------------------------------- 4 coordinate geometry
coord_fig = graph([{"f": lambda x: 2 * x, "dom": (-0.5, 6)},
                   {"f": lambda x: -x / 2 + 7.5, "dom": (0, 7.5), "color": C4, "dash": True}],
                  (-0.8, 7.5), (-0.8, 11.5), 250, 210,
                  points=[(1, 2, True, INK), (5, 10, True, INK), (3, 6, True, C2)],
                  lines=[(1, 2, 5, 2, C3), (5, 2, 5, 10, C3)],
                  labels=[(0.8, 2.6, "A(1, 2)", "end"), (4.8, 10.6, "B(5, 10)", "end"), (3.25, 5.5, "M(3, 6)", "start", C2),
                          (3, 1.2, "run = 4", "middle", C3), (5.2, 6, "rise = 8", "start", C3),
                          (7.3, 3.6, "⊥ bisector", "end", C4)],
                  title="A(1, 2) to B(5, 10)")

COORD = f"""
<h2><span class="num">4</span> Coordinate geometry (straight lines)</h2>
<p class="small">Not a section on the official sheet — but used everywhere: tangents, normals, intersections, transformations.</p>
<div class="grid2">
<div>
<table>
<tr><th>Find</th><th>Formula</th><th>A(1, 2), B(5, 10)</th></tr>
<tr><td>Gradient</td><td class="m">m = (y₂ − y₁)/(x₂ − x₁)</td><td>8/4 = <b>2</b></td></tr>
<tr><td>Midpoint</td><td class="m">((x₁+x₂)/2, (y₁+y₂)/2)</td><td><b>(3, 6)</b></td></tr>
<tr><td>Distance</td><td class="m">√((x₂−x₁)² + (y₂−y₁)²)</td><td>√80 = <b>4√5</b></td></tr>
<tr><td>Line</td><td class="m">y − y₁ = m(x − x₁)</td><td>y − 2 = 2(x − 1) → <b>y = 2x</b></td></tr>
</table>
</div>
<div class="fig">{coord_fig}</div>
</div>
<table>
<tr><th>Lines are…</th><th>Gradients</th><th>Example with y = 2x + 1</th></tr>
<tr><td>parallel</td><td class="m">m₁ = m₂</td><td class="m">y = 2x − 7</td></tr>
<tr><td>perpendicular</td><td class="m">m₁ × m₂ = −1 (flip and change sign)</td><td class="m">y = −½x + 4</td></tr>
<tr><td>horizontal / vertical</td><td class="m">m = 0 → y = k; &nbsp; undefined → x = k</td><td class="m">y = 3, x = −2</td></tr>
<tr><td>angle with the x-axis</td><td class="m">tan θ = m</td><td class="m">m = 1 → θ = 45°</td></tr>
</table>
{ex('Perpendicular bisector of AB: passes through M(3, 6) with gradient −½ (flip 2, change sign).<br>y − 6 = −½(x − 3) → <b>y = −½x + 7.5</b>.')}
{ex('Where do y = 2x and x + y = 6 meet? Substitute: x + 2x = 6 → x = 2, y = 4 → <b>(2, 4)</b>.', 'Example — intersection')}
{box('trick', 'Intercepts in two seconds', '<p>For ax + by = c: cover the y-term → x-intercept c/a; cover the x-term → y-intercept c/b. 3x + 2y = 12 → (4, 0) and (0, 6).</p>')}

<div class="try">
<h4>Try it yourself — Section 4</h4>
<ol>
<li>Find the gradient, midpoint and length of the segment from P(−2, 1) to Q(4, 9).</li>
<li>Find the equation of the line through (2, −1) perpendicular to y = 3x + 5.</li>
</ol>
</div>
"""

# ---------------------------------------------------------------- 5 exponentials and logs
expg = graph([{"f": lambda x: 2 * math.exp(x - 1) - 6, "dom": (-3, 3.2)}], (-3, 3.4), (-7.5, 6), 220, 160,
             asym=[("h", -6)], points=[(1 + ln(3), 0, True, C1), (0, 2 / E - 6, True, C1)],
             labels=[(3.3, -6.9, "y = −6", "end", C2), (1.9, 0.6, "(1 + logₑ3, 0)", "end", C1), (0.15, -4.7, "(0, 2/e − 6)", "start", C1)],
             title="y = 2e^(x − 1) − 6")
logg = graph([{"f": lambda x: ln(2 * x - 4) + 1 if x > 2 else float("nan"), "dom": (2.001, 7)}], (-0.5, 7), (-4, 4), 220, 160,
             asym=[("v", 2)], points=[(2 + 1 / (2 * E), 0, True, C4)],
             labels=[(2.15, 3.4, "x = 2", "start", C2), (2.5, -0.8, "(2 + 1/(2e), 0)", "start", C4)],
             title="y = logₑ(2x − 4) + 1")

EXPLOG = f"""
<h2><span class="num">5</span> Exponentials and logarithms</h2>
<div class="grid2">
<table>
<tr><th colspan="2">Index laws (same base only)</th></tr>
<tr><td class="m">aᵐ × aⁿ = aᵐ⁺ⁿ</td><td class="m">2³ × 2⁴ = 2⁷</td></tr>
<tr><td class="m">aᵐ ÷ aⁿ = aᵐ⁻ⁿ</td><td class="m">e⁵ ÷ e² = e³</td></tr>
<tr><td class="m">(aᵐ)ⁿ = aᵐⁿ</td><td class="m">(x²)³ = x⁶</td></tr>
<tr><td class="m">a⁰ = 1, a⁻ᵐ = 1/aᵐ</td><td class="m">2⁻³ = 1/8</td></tr>
<tr><td class="m">a^(m/n) = (ⁿ√a)ᵐ</td><td class="m">8^(2/3) = 2² = 4</td></tr>
</table>
<table>
<tr><th colspan="2">Log laws (logₑ = ln)</th></tr>
<tr><td class="m">logₐ y = x ⇔ aˣ = y</td><td>a log is an index</td></tr>
<tr><td class="m">log(mn) = log m + log n</td><td class="m">ln 6 = ln 2 + ln 3</td></tr>
<tr><td class="m">log(m/n) = log m − log n</td><td class="m">ln 5 − ln 2 = ln 2.5</td></tr>
<tr><td class="m">log(mᵖ) = p log m</td><td class="m">ln 8 = 3 ln 2</td></tr>
<tr><td class="m">log 1 = 0, logₐ a = 1</td><td class="m">e^(ln k) = k, ln(eˣ) = x</td></tr>
<tr><td>change of base</td><td class="m">logₐ b = ln b / ln a</td></tr>
</table>
</div>
{box('trap', 'There is no law for the log of a sum', '<p><span class="m">ln(m + n) ≠ ln m + ln n</span> and <span class="m">ln m × ln n ≠ ln(mn)</span>. Laws only work on a product, quotient or power <b>inside one log</b>.</p>')}

<h3>Solving exponential and log equations</h3>
<table>
<tr><th>Type</th><th>Method</th><th>Example</th></tr>
<tr><td>same base</td><td>equate the powers</td><td class="m">8ˣ = 2^(x+4) → 3x = x + 4 → x = 2</td></tr>
<tr><td>one exponential</td><td><b>isolate first</b>, then take ln</td><td class="m">2e^(3x) = 7 → e^(3x) = 7/2 → x = ⅓ ln(7/2)</td></tr>
<tr><td>quadratic in eˣ</td><td>let A = eˣ, reject A ≤ 0</td><td class="m">e^(2x) − 5eˣ + 6 = 0 → A = 2, 3 → x = ln 2, ln 3</td></tr>
<tr><td>logs</td><td>collapse to one log, then "unlog"</td><td class="m">ln x + ln(x − 3) = ln 4 → x² − 3x − 4 = 0</td></tr>
</table>
{box('trap', 'Check every log answer in the ORIGINAL equation', '<p>x² − 3x − 4 = 0 gives x = 4 or x = −1. But ln(−1) is undefined, so <b>x = 4 only</b>. Likewise 2 ln x = ln 9 gives x = 3 only, while ln(x²) = ln 9 gives x = ±3.</p>')}

<h3>Graphs of exponentials and logs</h3>
<table>
<tr><th></th><th>y = A e^(b(x + c)) + d</th><th>y = A logₑ(b(x + c)) + d</th></tr>
<tr><td>Asymptote</td><td>horizontal <b>y = d</b></td><td>vertical, where b(x + c) = 0</td></tr>
<tr><td>Domain</td><td class="m">R</td><td>solve b(x + c) &gt; 0</td></tr>
<tr><td>Range</td><td class="m">(d, ∞) if A &gt; 0; (−∞, d) if A &lt; 0</td><td class="m">R</td></tr>
<tr><td>Key point of the basic graph</td><td class="m">eˣ: (0, 1), (1, e)</td><td class="m">ln x: (1, 0), (e, 1)</td></tr>
</table>
<div class="figrow">{expg}{logg}</div>
<p class="small">eˣ and logₑ x are inverses — see the reflection graph in Section 3. If A and d have the same sign, the exponential graph has <b>no x-intercept</b>.</p>

<h3>Growth and decay</h3>
<table>
<tr><th>Model</th><th>Formula</th><th>Example: P = 500e^(0.04t)</th></tr>
<tr><td>growth / decay</td><td class="m">P = P₀e^(kt) (k &gt; 0 grows, k &lt; 0 decays)</td><td>starts at 500</td></tr>
<tr><td>doubling time / half-life</td><td class="m">t = ln 2 / |k|</td><td>ln 2 / 0.04 ≈ <b>17.3</b></td></tr>
<tr><td>time to multiply by m</td><td class="m">t = ln m / k</td><td>triples at ln 3 / 0.04 ≈ 27.5</td></tr>
<tr><td>find k from data</td><td>substitute a known point, then ln</td><td>P(10) = 800 → e^(10k) = 1.6 → k = ln 1.6 / 10</td></tr>
</table>
{box('trick', 'Doubling time ignores the starting amount', '<p>P₀ cancels in P₀e^(kt) = 2P₀, so the doubling time is always ln 2 ÷ k. Also: any base can be turned into e: <span class="m">aˣ = e^(x ln a)</span>.</p>')}

<div class="try">
<h4>Try it yourself — Section 5</h4>
<ol>
<li>Solve 3e^(2x) − 1 = 11, giving an exact answer.</li>
<li>Solve e^(2x) − eˣ − 6 = 0.</li>
<li>State the asymptote and range of y = −3e^x + 2.</li>
</ol>
</div>
"""

# ---------------------------------------------------------------- 6 differentiation
fail_figs = "".join([
    graph([{"f": lambda x: x * x, "dom": (-1.6, 1)}, {"f": lambda x: x + 1.2, "dom": (1.0001, 2)}], (-1.7, 2.1), (-0.5, 3.4), 135, 105,
          points=[(1, 1, True, C1), (1, 2.2, False, C1)], title="jump: not continuous"),
    graph([{"f": abs}], (-1.6, 1.6), (-0.4, 1.7), 135, 105, points=[(0, 0, True, C2)], title="corner: y = |x|"),
    graph([{"f": lambda x: math.copysign(abs(x) ** (1 / 3), x)}], (-1.6, 1.6), (-1.4, 1.4), 135, 105, points=[(0, 0, True, C2)], title="vertical tangent: y = ∛x"),
])

DIFF = f"""
<h2><span class="num">6</span> Differentiation</h2>
<h3>Standard derivatives</h3>
<div class="grid2">
<table>
<tr><th>f(x)</th><th>f′(x)</th><th>Example</th></tr>
<tr><td class="m">xⁿ</td><td class="m">nxⁿ⁻¹</td><td class="m">x⁻³ → −3x⁻⁴</td></tr>
<tr><td class="m">e^(kx)</td><td class="m">k e^(kx)</td><td class="m">e^(5x) → 5e^(5x)</td></tr>
<tr><td class="m">logₑ(kx)</td><td class="m">1/x</td><td class="m">ln(3x) → 1/x</td></tr>
<tr><td class="m">logₑ(ax + b)</td><td class="m">a/(ax + b)</td><td class="m">ln(2x+1) → 2/(2x+1)</td></tr>
</table>
<table>
<tr><th>f(x)</th><th>f′(x)</th><th>Example</th></tr>
<tr><td class="m">sin(kx)</td><td class="m">k cos(kx)</td><td class="m">sin 2x → 2cos 2x</td></tr>
<tr><td class="m">cos(kx)</td><td class="m">−k sin(kx)</td><td class="m">cos 3x → −3sin 3x</td></tr>
<tr><td class="m">tan(kx)</td><td class="m">k / cos²(kx)</td><td class="m">tan x → 1/cos²x</td></tr>
<tr><td class="m">aˣ</td><td class="m">aˣ ln a</td><td class="m">2ˣ → 2ˣ ln 2</td></tr>
</table>
</div>
<p class="small">Calculus only works in <b>radians</b>. Rewrite √x as x^½ and 1/x³ as x⁻³ first.</p>

<h3>The three rules</h3>
<table>
<tr><th>Rule</th><th>Formula</th><th>Example</th></tr>
<tr><td><b>Chain</b> (function inside a function)</td><td class="m">dy/dx = dy/du × du/dx</td><td class="m">(2x + 1)⁵ → 5(2x + 1)⁴ × 2 = 10(2x + 1)⁴</td></tr>
<tr><td><b>Product</b> (u × v)</td><td class="m">(uv)′ = u′v + uv′</td><td class="m">x²e^(3x) → 2xe^(3x) + 3x²e^(3x) = xe^(3x)(2 + 3x)</td></tr>
<tr><td><b>Quotient</b> (u ÷ v)</td><td class="m">(u/v)′ = (u′v − uv′)/v²</td><td class="m">x/(x + 1) → ((x + 1) − x)/(x + 1)² = 1/(x + 1)²</td></tr>
</table>
<div class="grid2">
{box('trick', 'Simplify before you differentiate', '<p>(x³ + 2x)/x = x² + 2 → derivative 2x. No quotient rule needed. Log laws work too: ln(x²√x) = (5/2) ln x → 5/(2x).</p>')}
{box('trick', 'Spot f′/f', '<p>If the top is the derivative of the bottom, it came from a log: d/dx ln(x² + 3x) = (2x + 3)/(x² + 3x).</p>')}
</div>
{box('trap', 'ln(kx) differentiates to 1/x — the k disappears', '<p>ln(kx) = ln k + ln x, and ln k is a constant. But ln(ax + b) → a/(ax + b), where the a stays. Also: quotient rule order is u′v − uv′ (swap it and every sign flips).</p>')}

<h3>First principles and the meaning of f′</h3>
<table>
<tr><th>Idea</th><th>Formula</th></tr>
<tr><td>Derivative (first principles)</td><td class="m">f′(x) = lim (h→0) [f(x + h) − f(x)] / h</td></tr>
<tr><td>Instantaneous rate = gradient of tangent</td><td class="m">f′(a)</td></tr>
<tr><td>Average rate = gradient of chord</td><td class="m">[f(b) − f(a)] / (b − a)</td></tr>
<tr><td>Second derivative</td><td class="m">f″(x) = d²y/dx² (NOT (dy/dx)²)</td></tr>
</table>
{ex('f(x) = x² + 3x by first principles: f(x + h) − f(x) = 2xh + h² + 3h. Divide by h: 2x + h + 3. Let h → 0: <b>f′(x) = 2x + 3</b>.')}

<h3>Where is f NOT differentiable? Look for these three shapes</h3>
<div class="figrow">{fail_figs}</div>
<p>Differentiable ⇒ continuous, but continuous does <b>not</b> mean differentiable (y = |x| is continuous at 0 but has a corner). For a hybrid function: check values match first, then gradients.</p>
{box('check', 'Gradient of an inverse: use the image point', '<p>(f⁻¹)′(b) = 1 / f′(a) where f(a) = b. f(x) = x³ + 1: f(1) = 2, f′(1) = 3 → (f⁻¹)′(<b>2</b>) = 1/3 (at x = 2, not x = 1).</p>')}

<div class="try">
<h4>Try it yourself — Section 6</h4>
<ol>
<li>Differentiate: (a) (3x − 2)⁴ &nbsp; (b) x sin x &nbsp; (c) e^(x²) &nbsp; (d) ln(5x)</li>
<li>Differentiate x² / (x + 1) using the quotient rule.</li>
</ol>
</div>
"""

# ---------------------------------------------------------------- 7 applications
tn_fig = graph([{"f": lambda x: x * x}, {"f": lambda x: 6 * x - 9, "color": C2, "width": 1.5},
                {"f": lambda x: -x / 6 + 9.5, "color": C4, "width": 1.5}], (-1, 6.5), (-2, 14), 230, 170,
               points=[(3, 9, True, INK)],
               labels=[(3.3, 8.2, "(3, 9)", "start"), (4.6, 13, "tangent y = 6x − 9", "end", C2), (6.4, 9.2, "normal", "end", C4)],
               title="y = x² at x = 3")
sp_fig = graph([{"f": lambda x: x ** 3 - 3 * x}], (-2.3, 2.6), (-3, 3.4), 230, 170,
               points=[(-1, 2, True, C3), (1, -2, True, C3)],
               labels=[(-1, 2.5, "local max (−1, 2)", "middle", C3), (1, -2.7, "local min (1, −2)", "middle", C3)],
               title="y = x³ − 3x")


def arrow_cell(s):
    return {"+": '<span style="color:#1f6f68;font-size:13pt">↗</span>', "0": '<span style="font-size:13pt">→</span>',
            "-": '<span style="color:#c0392b;font-size:13pt">↘</span>'}[s]


APPS = f"""
<h2><span class="num">7</span> Applications of differentiation</h2>
<h3>Tangents and normals</h3>
<div class="grid2">
<div>
<table>
<tr><th>Line</th><th>Equation at x = a</th></tr>
<tr><td>Tangent</td><td class="m">y − f(a) = f′(a)(x − a)</td></tr>
<tr><td>Normal (⊥ tangent)</td><td class="m">y − f(a) = −1/f′(a) · (x − a)</td></tr>
<tr><td>If f′(a) = 0</td><td>tangent y = f(a), normal x = a</td></tr>
</table>
{ex('y = x² at x = 3: point (3, 9), gradient f′(3) = 6.<br>Tangent: y − 9 = 6(x − 3) → <b>y = 6x − 9</b><br>Normal: y − 9 = −⅙(x − 3) → <b>y = −x/6 + 19/2</b><br>Check: 6 × (−⅙) = −1 ✓')}
</div>
<div class="fig">{tn_fig}</div>
</div>

<h3>Stationary points: f′(x) = 0 — then test the sign</h3>
<div class="grid2">
<table>
<tr><th>Sign of f′ (left, at, right)</th><th class="c">Shape</th><th>Type</th></tr>
<tr><td class="m">+ &nbsp;0&nbsp; −</td><td class="c">{arrow_cell('+')}{arrow_cell('0')}{arrow_cell('-')}</td><td>local maximum</td></tr>
<tr><td class="m">− &nbsp;0&nbsp; +</td><td class="c">{arrow_cell('-')}{arrow_cell('0')}{arrow_cell('+')}</td><td>local minimum</td></tr>
<tr><td class="m">+ &nbsp;0&nbsp; +</td><td class="c">{arrow_cell('+')}{arrow_cell('0')}{arrow_cell('+')}</td><td>stationary point of inflection</td></tr>
<tr><td class="m">− &nbsp;0&nbsp; −</td><td class="c">{arrow_cell('-')}{arrow_cell('0')}{arrow_cell('-')}</td><td>stationary point of inflection</td></tr>
</table>
<div class="fig">{sp_fig}</div>
</div>
{ex('y = x³ − 3x: f′(x) = 3x² − 3 = 0 → x = ±1. f″(x) = 6x: f″(−1) = −6 &lt; 0 → <b>max (−1, 2)</b>; f″(1) = 6 &gt; 0 → <b>min (1, −2)</b>.<br>Strictly increasing on <span class="m">(−∞, −1) ∪ (1, ∞)</span>, strictly decreasing on <span class="m">(−1, 1)</span>.')}

<table>
<tr><th>Second derivative</th><th>Means</th></tr>
<tr><td class="m">f″ &gt; 0</td><td>concave up ∪ ("holds water") → a stationary point here is a min</td></tr>
<tr><td class="m">f″ &lt; 0</td><td>concave down ∩ ("spills water") → a stationary point here is a max</td></tr>
<tr><td class="m">f″ changes sign</td><td><b>point of inflection</b> (e.g. y = x³ − 3x² at (1, −2))</td></tr>
<tr><td class="m">f″(a) = 0</td><td><b>no conclusion</b> — use the sign test</td></tr>
</table>
{box('trap', 'f″(a) = 0 proves nothing', '<p>y = x⁴ has f″(0) = 0 at a minimum; y = x³ has f″(0) = 0 at an inflection. Same f″, different answers — always fall back on the sign table.</p>')}

<h3>Absolute max / min on a closed interval</h3>
<table>
<tr><th colspan="5">f(x) = x³ − 3x on [−2, 3] — check stationary points AND endpoints</th></tr>
<tr><th>x</th><td class="c">−2 (end)</td><td class="c">−1 (stat.)</td><td class="c">1 (stat.)</td><td class="c">3 (end)</td></tr>
<tr><th>f(x)</th><td class="c">−2</td><td class="c">2</td><td class="c">−2</td><td class="c"><b>18</b></td></tr>
</table>
<p>Absolute max <b>18</b> at x = 3 (an endpoint!). Absolute min <b>−2</b> at x = −2 and x = 1.</p>

<h3>Optimisation — the 6-step recipe</h3>
<div class="flow">
<div class="step"><b>1</b>Write the quantity</div><div class="arrow">→</div>
<div class="step"><b>2</b>Use the constraint to get one variable</div><div class="arrow">→</div>
<div class="step"><b>3</b>State the domain</div><div class="arrow">→</div>
<div class="step"><b>4</b>Solve f′ = 0</div><div class="arrow">→</div>
<div class="step"><b>5</b>Justify max/min</div><div class="arrow">→</div>
<div class="step"><b>6</b>Answer in context + units</div>
</div>
{ex('Open box, square base s, volume 32 cm³. Height h = 32/s², so surface S = s² + 4sh = s² + 128/s, domain s &gt; 0.<br>S′ = 2s − 128/s² = 0 → s³ = 64 → s = 4. S″(4) = 2 + 256/64 = 6 &gt; 0 → minimum.<br><b>Minimum surface area 48 cm² when the base is 4 cm.</b>')}

<h3>Rates of change and related rates</h3>
<table>
<tr><th>Idea</th><th>Rule</th></tr>
<tr><td>Related rates (chain rule)</td><td class="m">dV/dt = dV/dr × dr/dt</td></tr>
<tr><td>Sphere / circle</td><td class="m">dV/dr = 4πr², dA/dr = 2πr</td></tr>
<tr><td>Reciprocal</td><td class="m">dt/dx = 1 ÷ (dx/dt)</td></tr>
</table>
{ex('A sphere is inflated at 100 cm³/s. How fast is r growing when r = 5?<br>dr/dt = (dV/dt) ÷ (dV/dr) = 100 ÷ (4π × 25) = <b>1/π cm/s</b>. (Differentiate first, substitute r = 5 last.)')}

<div class="try">
<h4>Try it yourself — Section 7</h4>
<ol>
<li>Find the tangent to y = x³ at x = 1.</li>
<li>Find and classify the stationary points of y = x³ − 6x² + 9x.</li>
<li>Find the absolute maximum of f(x) = x² − 4x on [0, 5].</li>
</ol>
</div>
"""

# ---------------------------------------------------------------- 8 integration
area_fig = graph([{"f": lambda x: x ** 3}], (-1.4, 2.3), (-1.6, 8.5), 220, 170,
                 shade=[(lambda x: x ** 3, -1, 0, C2), (lambda x: x ** 3, 0, 2, C1)],
                 labels=[(-0.6, -1.3, "−1/4", "middle", C2), (1.45, 1.2, "+4", "middle", C1)],
                 title="y = x³ on [−1, 2]")
between_fig = graph([{"f": lambda x: x}, {"f": lambda x: x * x, "color": C4}], (-0.3, 1.4), (-0.3, 1.6), 220, 170,
                    shade=[(lambda x: x, 0, 1, C3, lambda x: x * x)],
                    labels=[(1.35, 1.45, "y = x (upper)", "end", C1), (1.35, 1.0, "y = x² (lower)", "end", C4)],
                    title="area between y = x and y = x²")
trap_fig = graph([{"f": lambda x: x * x}], (-0.2, 2.3), (-0.4, 4.6), 220, 170,
                 lines=[(0, 0, 0.5, 0.25, C2), (0.5, 0.25, 1, 1, C2), (1, 1, 1.5, 2.25, C2), (1.5, 2.25, 2, 4, C2),
                        (0.5, 0, 0.5, 0.25, C2), (1, 0, 1, 1, C2), (1.5, 0, 1.5, 2.25, C2), (2, 0, 2, 4, C2)],
                 labels=[(0.3, 3.6, "chords sit above the curve", "start", C2)],
                 title="trapezium rule on y = x², n = 4")

INTEG = f"""
<h2><span class="num">8</span> Integration</h2>
<h3>Standard antiderivatives (add + c)</h3>
<div class="grid2">
<table>
<tr><th>f(x)</th><th>∫ f(x) dx</th></tr>
<tr><td class="m">xⁿ (n ≠ −1)</td><td class="m">xⁿ⁺¹/(n + 1)</td></tr>
<tr><td class="m">(ax + b)ⁿ</td><td class="m">(ax + b)ⁿ⁺¹ / (a(n + 1))</td></tr>
<tr><td class="m">1/x</td><td class="m">logₑ|x|</td></tr>
<tr><td class="m">1/(ax + b)</td><td class="m">(1/a) logₑ|ax + b|</td></tr>
<tr><td class="m">f′(x)/f(x)</td><td class="m">logₑ|f(x)|</td></tr>
</table>
<table>
<tr><th>f(x)</th><th>∫ f(x) dx</th></tr>
<tr><td class="m">e^(kx)</td><td class="m">e^(kx)/k</td></tr>
<tr><td class="m">sin(kx)</td><td class="m">−cos(kx)/k</td></tr>
<tr><td class="m">cos(kx)</td><td class="m">sin(kx)/k</td></tr>
<tr><td class="m">1/cos²(kx)</td><td class="m">tan(kx)/k</td></tr>
<tr><td class="m">1/√x</td><td class="m">2√x</td></tr>
</table>
</div>
{ex('∫(3x + 1)⁷ dx = (3x + 1)⁸/24 + c &nbsp;·&nbsp; ∫ 1/(2x + 3) dx = ½ logₑ|2x + 3| + c &nbsp;·&nbsp; ∫ x/(x² + 1) dx = ½ logₑ(x² + 1) + c')}
{box('check', 'Differentiate your answer back', '<p>You must get the integrand exactly. This catches a missing 1/a or a lost minus sign from sin in seconds.</p>')}

<h3>Definite integrals and area</h3>
<table>
<tr><th>Fact</th><th>Rule</th></tr>
<tr><td>Fundamental theorem</td><td class="m">∫ₐᵇ f(x) dx = F(b) − F(a) (no + c)</td></tr>
<tr><td>Swap terminals</td><td class="m">∫ₐᵇ f = −∫ (from b to a) f</td></tr>
<tr><td>Odd function on [−a, a]</td><td class="m">∫ = 0 &nbsp;(e.g. ∫₋₂² x³ dx = 0)</td></tr>
<tr><td>Area below the x-axis</td><td>counts as <b>negative</b> in the integral</td></tr>
<tr><td>Area between curves</td><td class="m">∫ (upper − lower) dx</td></tr>
<tr><td>Average value</td><td class="m">1/(b − a) × ∫ₐᵇ f(x) dx &nbsp;(x² on [0, 3] → 3)</td></tr>
</table>
<div class="figrow">{area_fig}{between_fig}</div>
{ex('y = x³ on [−1, 2]: the integral gives −1/4 + 4 = 15/4, but the <b>area</b> is 1/4 + 4 = <b>17/4</b>.<br>Between y = x and y = x²: they meet at x = 0, 1 → ∫₀¹ (x − x²) dx = 1/2 − 1/3 = <b>1/6</b>.')}
{box('trap', 'Integral ≠ area', '<p>∫₀^2π sin x dx = 0, but the area is 4. If the curve crosses the axis, find the zeros, integrate each piece, and add the absolute values. An area is never negative.</p>')}

<h3>Kinematics</h3>
<div class="flow">
<div class="step"><b>x</b>position (displacement)</div><div class="arrow">⇄</div>
<div class="step"><b>v</b>velocity = dx/dt</div><div class="arrow">⇄</div>
<div class="step"><b>a</b>acceleration = dv/dt</div>
</div>
<p class="small">Differentiate going → right, integrate going ← left (and find + c from the starting values). "At rest" means v = 0; "at the origin" means x = 0.</p>
{ex('v = 3t² − 12t on [0, 5]. v = 0 at t = 0 and t = 4, so split there.<br>∫₀⁴ v dt = −32, ∫₄⁵ v dt = 7. Displacement = −25, but <b>distance = 32 + 7 = 39</b>.')}

<h3>Estimating an integral</h3>
<div class="grid2">
<div>
<table>
<tr><th colspan="2">∫₀² x² dx = 8/3 ≈ 2.667, with n = 4 (h = 0.5)</th></tr>
<tr><td>Left rectangles</td><td>1.75 (under, x² increasing)</td></tr>
<tr><td>Right rectangles</td><td>3.75 (over)</td></tr>
<tr><td>Trapezium</td><td class="m">(h/2)[f₀ + 2f₁ + 2f₂ + 2f₃ + f₄] = 2.75</td></tr>
</table>
<p class="small">Trapezium = (left + right)/2. Concave up → trapezium <b>overestimates</b>; concave down → underestimates.</p>
</div>
<div class="fig">{trap_fig}</div>
</div>
{box('trick', 'Unknown terminal or + c', '<p>∫₀ᵏ 2x dx = 9 → k² = 9 → k = 3 (k &gt; 0). &nbsp;f′(x) = 6x, f(2) = 5 → f(x) = 3x² + c, 12 + c = 5 → <b>f(x) = 3x² − 7</b>.</p>')}

<div class="try">
<h4>Try it yourself — Section 8</h4>
<ol>
<li>Find: (a) ∫ (4x³ − 2/x) dx &nbsp; (b) ∫ e^(−2x) dx &nbsp; (c) ∫ cos(3x) dx</li>
<li>Find the area enclosed by y = x² − 4 and the x-axis.</li>
<li>Find the average value of y = 2x + 1 on [0, 4].</li>
</ol>
</div>
"""

CALC = COORD + EXPLOG + DIFF + APPS + INTEG

CALC_ANS = """
<div>
<h4>Section 4</h4>
<p>1. m = 8/6 = <b>4/3</b>; midpoint <b>(1, 5)</b>; length √(36 + 64) = <b>10</b></p>
<p>2. m = −1/3: y + 1 = −⅓(x − 2) → <b>y = −x/3 − 1/3</b></p>
<h4>Section 5</h4>
<p>1. e^(2x) = 4 → <b>x = ½ ln 4 = ln 2</b></p>
<p>2. A = eˣ: (A − 3)(A + 2) = 0, reject A = −2 → <b>x = ln 3</b></p>
<p>3. Asymptote <b>y = 2</b>, range <b>(−∞, 2)</b></p>
<h4>Section 6</h4>
<p>1. (a) 12(3x − 2)³ (b) sin x + x cos x (c) 2x e^(x²) (d) 1/x</p>
<p>2. (2x(x + 1) − x²)/(x + 1)² = <b>(x² + 2x)/(x + 1)²</b></p>
</div>
<div>
<h4>Section 7</h4>
<p>1. Point (1, 1), gradient 3 → <b>y = 3x − 2</b></p>
<p>2. y′ = 3(x − 1)(x − 3): <b>max (1, 4)</b>, <b>min (3, 0)</b></p>
<p>3. f(0) = 0, f(2) = −4, f(5) = 5 → absolute max <b>5</b> at x = 5</p>
<h4>Section 8</h4>
<p>1. (a) x⁴ − 2 ln|x| + c (b) −½e^(−2x) + c (c) ⅓ sin(3x) + c</p>
<p>2. Zeros at ±2: |∫₋₂² (x² − 4) dx| = <b>32/3</b></p>
<p>3. ¼ ∫₀⁴ (2x + 1) dx = ¼ × 20 = <b>5</b></p>
</div>
"""
