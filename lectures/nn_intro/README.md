# NN step by step
# Motivation

Based on the great work of https://karpathy.ai/zero-to-hero.html

Most of us probably know high level how NNs are supposed to work. Some of us can call them / train them in high level framework like tensorflow or pytorch. But I think lot of us are missing the place in the middle - how the training works on implementation level in basic terms.

+ this is great opportunity to practice non-trivial python!

We will create API similar to Pytorch

# Components
1. Graph propagating analytic operations
2. "backpropagation" aka gradient
3. Graph = bunch of neurons defined by their analytical operations
4. Training: weight init, feed forward, loss function, backprop
4. MLP: architecture
5. Application to data (e.g. classification task) https://github.com/karpathy/micrograd/blob/master/demo.ipynb

# TODO
- [ ] Improve with examples and descriptions from https://bclarkson-code.github.io/posts/llm-from-scratch-scalar-autograd/post.html
