"""Algebra, algorithms, exam technique and formula-sheet sections (14–17)."""
from prob import box, ex

ALG = f"""
<h2><span class="num">14</span> Algebra: polynomials and simultaneous equations</h2>
<h3>Remainder and factor theorems</h3>
<table>
<tr><th>Theorem</th><th>Rule</th><th>Example: P(x) = 2x³ − 5x² + 3x − 7</th></tr>
<tr><td>Remainder</td><td class="m">P(x) ÷ (x − a) leaves P(a)</td><td>÷ (x − 2): P(2) = 16 − 20 + 6 − 7 = <b>−5</b></td></tr>
<tr><td>Divisor ax − b</td><td class="m">remainder = P(b/a)</td><td>÷ (2x − 1): use P(½), not P(2)</td></tr>
<tr><td>Factor</td><td class="m">(x − a) is a factor ⇔ P(a) = 0</td><td>"(x + 3) is a factor" means P(−3) = 0</td></tr>
</table>
{ex('Factorise 2x³ + 3x² − 8x + 3. Coefficients add to 0 → P(1) = 0, so (x − 1) is a factor.<br>Divide: 2x³ + 3x² − 8x + 3 = (x − 1)(2x² + 5x − 3) = <b>(x − 1)(2x − 1)(x + 3)</b> → roots 1, ½, −3.')}
{box('trick', 'Try x = 1 and x = −1 first', '<p>If the coefficients add to 0, then x = 1 is a root. If the coefficients with alternating signs add to 0, x = −1 is a root. Otherwise try ± factors of (constant ÷ leading coefficient).</p>')}

<h3>Sum and product of roots — answer without solving</h3>
<table>
<tr><th>Equation</th><th>Sum of roots</th><th>Product of roots</th><th>For 2x² − 7x + 3</th></tr>
<tr><td class="m">ax² + bx + c = 0</td><td class="m">α + β = −b/a</td><td class="m">αβ = c/a</td><td>sum 7/2, product 3/2</td></tr>
<tr><td colspan="3">Useful re-writes: <span class="m">α² + β² = (α + β)² − 2αβ</span>, &nbsp;<span class="m">1/α + 1/β = (α + β)/(αβ)</span></td><td>37/4 and 7/3</td></tr>
</table>

<h3>Line meets curve — count the meetings with Δ</h3>
<div class="grid2">
<table>
<tr><th>Δ = b² − 4ac</th><th>Line and curve…</th></tr>
<tr><td class="m">Δ &gt; 0</td><td>meet twice</td></tr>
<tr><td class="m">Δ = 0</td><td>touch once — <b>tangent</b></td></tr>
<tr><td class="m">Δ &lt; 0</td><td>don't meet</td></tr>
</table>
{ex('y = mx + 2 and y = x² + x + 3: x² + (1 − m)x + 1 = 0, Δ = (1 − m)² − 4.<br>Tangent when Δ = 0 → <b>m = −1 or m = 3</b>.')}
</div>

<h3>Simultaneous linear equations with a parameter</h3>
<p>For a₁x + b₁y = c₁ and a₂x + b₂y = c₂, the determinant is <span class="m">det = a₁b₂ − a₂b₁</span>.</p>
<table>
<tr><th>det</th><th>Lines are…</th><th>Solutions</th></tr>
<tr><td class="m">det ≠ 0</td><td>crossing (different gradients)</td><td>exactly one</td></tr>
<tr><td class="m" rowspan="2">det = 0</td><td>parallel and different</td><td>none</td></tr>
<tr><td>the same line</td><td>infinitely many</td></tr>
</table>
{ex('kx + 4y = k + 2 and x + ky = 2: det = k² − 4 = 0 at k = ±2.<br>k = 2: 2x + 4y = 4 and x + 2y = 2 → same line → <b>infinitely many</b>.<br>k = −2: x − 2y = 0 and x − 2y = 2 → parallel → <b>no solution</b>. Unique solution for k ∈ R \\ {−2, 2}.')}
{box('trap', 'det = 0 does not automatically mean "no solution"', '<p>It means parallel <b>or</b> identical. Substitute each value back and decide separately — that step is where the marks are.</p>')}

<div class="try">
<h4>Try it yourself — Section 14</h4>
<ol>
<li>Find the remainder when x³ + 2x² − 5 is divided by (x + 1).</li>
<li>(x − 2) is a factor of x³ + kx − 4. Find k.</li>
</ol>
</div>
"""

ALGO = f"""
<h2><span class="num">15</span> Algorithms and pseudocode</h2>
<table>
<tr><th>Pseudocode</th><th>Means</th></tr>
<tr><td class="m">s ← s + i</td><td>work out the right side with the current values, then store it in s</td></tr>
<tr><td class="m">if … then … else … end if</td><td>exactly one branch runs</td></tr>
<tr><td class="m">for i from 1 to 5</td><td>runs 5 times (a to b runs <b>b − a + 1</b> times)</td></tr>
<tr><td class="m">while i &lt; 5 do</td><td>condition checked <b>before</b> each pass — may never run</td></tr>
<tr><td class="m">print s</td><td>inside the loop = one value per pass; after it = one value</td></tr>
</table>
<h3>Trace a loop in a table</h3>
<div class="grid2">
<div>
<p class="m">s ← 0<br>for i from 1 to 5 do<br>&nbsp;&nbsp;s ← s + i²<br>end for<br>print s</p>
<p class="small">Sum accumulators start at 0; product accumulators start at 1.</p>
</div>
<table>
<tr><th>i</th><td class="c">1</td><td class="c">2</td><td class="c">3</td><td class="c">4</td><td class="c">5</td></tr>
<tr><th>s</th><td class="c">1</td><td class="c">5</td><td class="c">14</td><td class="c">30</td><td class="c"><b>55</b></td></tr>
</table>
</div>

<h3>Finding roots: bisection vs Newton's method (f(x) = x² − 5, root √5 ≈ 2.2361)</h3>
<div class="grid2">
<div>
<table>
<tr><th colspan="3">Bisection on [2, 3]: keep the half with a sign change</th></tr>
<tr><th>midpoint m</th><th>f(m)</th><th>new interval</th></tr>
<tr><td class="c">2.5</td><td class="c">1.25</td><td class="c">[2, 2.5]</td></tr>
<tr><td class="c">2.25</td><td class="c">0.0625</td><td class="c">[2, 2.25]</td></tr>
<tr><td class="c">2.125</td><td class="c">−0.484</td><td class="c">[2.125, 2.25]</td></tr>
<tr><td class="c">2.1875</td><td class="c">−0.215</td><td class="c">[2.1875, 2.25]</td></tr>
</table>
<p class="small">Width after n steps = (b − a)/2ⁿ. Slow but <b>always</b> works (needs a sign change).</p>
</div>
<div>
<table>
<tr><th colspan="2">Newton: xₙ₊₁ = xₙ − f(xₙ)/f′(xₙ), x₀ = 2</th></tr>
<tr><td>x₁</td><td class="c">2.25</td></tr>
<tr><td>x₂</td><td class="c">2.236111</td></tr>
<tr><td>x₃</td><td class="c">2.2360680 ✓</td></tr>
</table>
<p class="small">Very fast, but <b>fails</b> if f′(xₙ) = 0, can cycle, or can find a different root if x₀ is badly chosen.</p>
</div>
</div>

<h3>Other algorithms you need</h3>
<table>
<tr><th>Algorithm</th><th>Key fact</th><th>Example</th></tr>
<tr><td>Horner's method</td><td>nest the polynomial: multiply by x, add the next coefficient</td><td class="m">2x³ − 6x² + 2x − 1 at x = 3: 2 → 0 → 2 → 5</td></tr>
<tr><td>Linear search</td><td>check items one by one (any list)</td><td>1000 items → up to 1000 checks</td></tr>
<tr><td>Binary search</td><td>list must be <b>sorted</b>; check the middle, discard half</td><td>1000 items → at most 10 checks</td></tr>
<tr><td>Nested loops</td><td>n × n passes = n²</td><td>n = 6 → 36 (triangular j ≤ i → 21)</td></tr>
</table>
{box('trap', 'Off-by-one errors', '<p>for 3 to 9 runs <b>7</b> times · while i &lt; n runs one fewer time than while i ≤ n · n strips need <b>n + 1</b> ordinates.</p>')}

<div class="try">
<h4>Try it yourself — Section 15</h4>
<ol>
<li>p ← 1; for i from 1 to 4 do p ← p × i. What is p at the end?</li>
<li>Do one Newton step for f(x) = x² − 3 from x₀ = 2.</li>
</ol>
</div>
"""

EXAM = f"""
<h2><span class="num">16</span> Exam technique</h2>
<table>
<tr><th>The question says…</th><th>You must…</th></tr>
<tr><td><b>Show that</b></td><td>show every step from the given information to the printed answer; never start from the answer</td></tr>
<tr><td><b>Hence</b></td><td>use the previous part — another method can score 0</td></tr>
<tr><td><b>Hence or otherwise</b></td><td>any method, but "hence" is usually quicker</td></tr>
<tr><td><b>Exact value</b></td><td>surds, π, e, ln, fractions — <b>no decimals</b> (π/6, not 0.5236)</td></tr>
<tr><td><b>Correct to n decimal places</b></td><td>round only at the very end, show exactly n places</td></tr>
<tr><td><b>State / write down</b></td><td>no working needed</td></tr>
<tr><td><b>Explain / justify</b></td><td>a sentence naming the reason ("because f′ &gt; 0 on…")</td></tr>
<tr><td><b>Sketch</b></td><td>label intercepts, turning points, asymptotes (dashed, with equations), endpoints (open/closed)</td></tr>
</table>
<div class="grid2">
<div>
<h3>Marks and time</h3>
<table>
<tr><td>1 mark</td><td>one step or fact</td></tr>
<tr><td>2 marks</td><td>method + answer</td></tr>
<tr><td>3+ marks</td><td>lay out each step separately</td></tr>
<tr><td>Pace</td><td>≈ 1 mark per 1.5 minutes</td></tr>
<tr><td>Multiple choice</td><td>≈ 1 min each; never leave one blank</td></tr>
</table>
</div>
<div>
<h3>CAS habits</h3>
<table>
<tr><td>Radian mode</td><td>always, every exam</td></tr>
<tr><td>Define f(x) first</td><td>then reuse it for d/dx, solve, ∫</td></tr>
<tr><td>Restrict trig solves</td><td class="m">solve(…) | 0 ≤ x ≤ 2π</td></tr>
<tr><td>Store values</td><td>don't retype long decimals</td></tr>
<tr><td>Write what you typed</td><td>e.g. "solve(f′(x) = 0, x)" earns the method mark</td></tr>
</table>
</div>
</div>
{box('trick', 'Multiple choice: substitute a number', '<p>Put x = 0, 1 or π/2 into the question and each option — usually only one matches. Or eliminate options using one feature you are sure of (domain, asymptote, sign).</p>')}
{box('trap', 'The most common avoidable losses', '<p>① A decimal where an exact value was asked. ② Rounding too early. ③ Answering a slightly different question (x-value vs maximum value). ④ Forgetting endpoints on a closed interval. ⑤ Missing units. ⑥ Leaving a later part blank — follow-through marks exist, so always attempt it.</p>')}
{box('check', 'Before you move on', '<p>Substitute your answer back · differentiate your antiderivative · is the probability between 0 and 1? · is the area positive? · did you answer the question that was asked?</p>')}

<h2><span class="num">17</span> What the official formula sheet gives you — and what it doesn't</h2>
<div class="grid2">
<table>
<tr><th style="background:#e8f3f1">✓ ON the sheet (read it off)</th></tr>
<tr><td>Mensuration: cylinder, cone, pyramid, sphere volume, triangle ½bc sin A</td></tr>
<tr><td>Derivative/antiderivative pairs: xⁿ, (ax + b)ⁿ, e^(ax), logₑ x, sin, cos, tan (derivative only)</td></tr>
<tr><td>Product, quotient and chain rules</td></tr>
<tr><td>Newton's method and the trapezium rule</td></tr>
<tr><td>Probability: complement, addition, conditional, E(X), Var(X), binomial, pdf mean/variance</td></tr>
<tr><td>Sample proportions: P̂ = X/n, E(P̂) = p, sd(P̂), the confidence interval</td></tr>
</table>
<table>
<tr><th style="background:#fdecea">✗ NOT on the sheet (memorise!)</th></tr>
<tr><td>Exact trig values, ASTC, trig graph features, general solutions</td></tr>
<tr><td>Index laws, log laws, change of base</td></tr>
<tr><td>Quadratic formula, discriminant, remainder and factor theorems</td></tr>
<tr><td>Transformation rules, inverse functions, composite rule ran g ⊆ dom f</td></tr>
<tr><td>Tangent/normal equations, stationary point tests, average value, area between curves</td></tr>
<tr><td>Independence test, z = (x − μ)/σ, 68–95–99.7, z-values 1.645 / 1.96 / 2.576</td></tr>
<tr><td>logₑ|x| (the sheet only gives logₑ x for x &gt; 0), bisection, left/right rectangles</td></tr>
</table>
</div>
{box('check', 'Get this year\'s sheet', '<p>Download the current sheet from vcaa.vic.edu.au, check it against the lists above, and practise with it beside you. Exam 1 and Exam 2 use the same sheet.</p>')}
"""

EXTRA = ALG + ALGO + EXAM

EXTRA_ANS = """
<div>
<h4>Section 14</h4>
<p>1. P(−1) = −1 + 2 − 5 = <b>−4</b></p>
<p>2. P(2) = 8 + 2k − 4 = 0 → <b>k = −2</b></p>
</div>
<div>
<h4>Section 15</h4>
<p>1. p = 1 × 2 × 3 × 4 = <b>24</b></p>
<p>2. x₁ = 2 − (4 − 3)/(2 × 2) = <b>1.75</b></p>
</div>
"""
