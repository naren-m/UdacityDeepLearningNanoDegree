##Intro to Deep Learning

###Week 2 

####Further reading

Backpropagation is fundamental to deep learning.
* From Andrej Karpathy: [Yes, you should understand backprop](https://ipython.org/ipython-doc/1/interactive/nbconvert.html)
* Also from Andrej Karpathy, [a lecture from Stanford's CS231n course](https://www.youtube.com/watch?v=59Hbtz7XgjM)

<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <mi>H</mi>
  <mo stretchy="false">(</mo>
  <mi>y</mi>
  <mo>,</mo>
  <mrow class="MJX-TeXAtom-ORD">
    <mover>
      <mi>y</mi>
      <mo stretchy="false">&#x005E;<!-- ^ --></mo>
    </mover>
  </mrow>
  <mo stretchy="false">)</mo>
  <mo>=</mo>
  <munder>
    <mo>&#x2211;<!-- ∑ --></mo>
    <mi>i</mi>
  </munder>
  <msub>
    <mi>y</mi>
    <mi>i</mi>
  </msub>
  <mi>log</mi>
  <mo>&#x2061;<!-- ⁡ --></mo>
  <mfrac>
    <mn>1</mn>
    <mrow class="MJX-TeXAtom-ORD">
      <mover>
        <msub>
          <mi>y</mi>
          <mi>i</mi>
        </msub>
        <mo stretchy="false">&#x005E;<!-- ^ --></mo>
      </mover>
    </mrow>
  </mfrac>
  <mo>=</mo>
  <mo>&#x2212;<!-- − --></mo>
  <munder>
    <mo>&#x2211;<!-- ∑ --></mo>
    <mi>i</mi>
  </munder>
  <msub>
    <mi>y</mi>
    <mi>i</mi>
  </msub>
  <mi>log</mi>
  <mo>&#x2061;<!-- ⁡ --></mo>
  <mrow class="MJX-TeXAtom-ORD">
    <mover>
      <msub>
        <mi>y</mi>
        <mi>i</mi>
      </msub>
      <mo stretchy="false">&#x005E;<!-- ^ --></mo>
    </mover>
  </mrow>
</math>

**Quick intro resources**

1. [Introduction to pandas in 10 Minutes](http://pandas.pydata.org/pandas-docs/stable/10min.html#min)
2. [Tensor flow in 5 Minutes](https://www.youtube.com/watch?v=2FmcHiLCwTU&t=84s)
3. [Stanford TensorFlow Tutorial](https://cs224d.stanford.edu/lectures/CS224d-Lecture7.pdf)
4. [TensorFlow Examples on GitHub](https://github.com/aymericdamien/TensorFlow-Examples)
5. [MNIST For ML Beginners](https://www.tensorflow.org/tutorials/mnist/beginners/)
6. [O'Reilly Hello, TensorFlow!](https://www.oreilly.com/learning/hello-tensorflow)
7. [A Visual and Interactive Guide to the Basics of Neural Networks](https://jalammar.github.io/visual-interactive-guide-basics-neural-networks/)
