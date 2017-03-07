<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
<!doctype html><html><head><meta charset='utf-8'>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/2.4.1/github-markdown.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.9.0/styles/default.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.6.0/katex.min.css">
<link rel="stylesheet" href="https://gitcdn.xyz/repo/goessner/mdmath/master/css/mdmath.css">
</head><body class="markdown-body">
<h3>Model Evaluation and Validation</h3>
<p>In the bike sharing project, the data was split into training, validation, and test sets. In this section we'll learn why this is needed, and how to find out how well your model is doing, and score it. In particular, you will cover:</p>
<ul>
<li>How to create a test set for your models.</li>
<li>How to use confusion matrices to evaluate false positives, and false negatives.</li>
<li>How to measure accuracy and other model metrics.</li>
<li>How to evaluate regression.</li>
<li>How to detect whether you are overfitting or underfitting based on the complexity of your model.</li>
<li>How to use cross validation to ensure your model is generalizable.</li>
</ul>
<p>Regression and Classification</p>
<pre><code>Regression returns numeric value

Classification returns a state
</code></pre>
<p>How do we find a model that generalizes well?</p>
<pre><code>To do this we
</code></pre>
<section><eqn><span class="katex-display"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>c</mi><mn>2</mn></msup><mo>=</mo><msup><mi>a</mi><mn>2</mn></msup><mo>+</mo><msup><mi>b</mi><mn>2</mn></msup></mrow><annotation encoding="application/x-tex"> c^2 = a^2 + b^2 </annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height:0.8641079999999999em;"></span><span class="strut bottom" style="height:0.9474379999999999em;vertical-align:-0.08333em;"></span><span class="base displaystyle textstyle uncramped"><span class="mord"><span class="mord mathit">c</span><span class="vlist"><span style="top:-0.413em;margin-right:0.05em;"><span class="fontsize-ensurer reset-size5 size5"><span style="font-size:0em;">​</span></span><span class="reset-textstyle scriptstyle uncramped"><span class="mord mathrm">2</span></span></span><span class="baseline-fix"><span class="fontsize-ensurer reset-size5 size5"><span style="font-size:0em;">​</span></span>​</span></span></span><span class="mrel">=</span><span class="mord"><span class="mord mathit">a</span><span class="vlist"><span style="top:-0.413em;margin-right:0.05em;"><span class="fontsize-ensurer reset-size5 size5"><span style="font-size:0em;">​</span></span><span class="reset-textstyle scriptstyle uncramped"><span class="mord mathrm">2</span></span></span><span class="baseline-fix"><span class="fontsize-ensurer reset-size5 size5"><span style="font-size:0em;">​</span></span>​</span></span></span><span class="mbin">+</span><span class="mord"><span class="mord mathit">b</span><span class="vlist"><span style="top:-0.413em;margin-right:0.05em;"><span class="fontsize-ensurer reset-size5 size5"><span style="font-size:0em;">​</span></span><span class="reset-textstyle scriptstyle uncramped"><span class="mord mathrm">2</span></span></span><span class="baseline-fix"><span class="fontsize-ensurer reset-size5 size5"><span style="font-size:0em;">​</span></span>​</span></span></span></span></span></span></span></eqn></section>
<section><eqn><span class="katex-display"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mrow></mrow><mi>s</mi></msub><mi>u</mi><mi>m</mi></mrow><annotation encoding="application/x-tex"> \_sum </annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.58056em;vertical-align:-0.15em;"></span><span class="base displaystyle textstyle uncramped"><span class="mord"><span></span><span class="vlist"><span style="top:0.15em;margin-right:0.05em;"><span class="fontsize-ensurer reset-size5 size5"><span style="font-size:0em;">​</span></span><span class="reset-textstyle scriptstyle cramped"><span class="mord mathit">s</span></span></span><span class="baseline-fix"><span class="fontsize-ensurer reset-size5 size5"><span style="font-size:0em;">​</span></span>​</span></span></span><span class="mord mathit">u</span><span class="mord mathit">m</span></span></span></span></span></eqn></section>

</body></html>