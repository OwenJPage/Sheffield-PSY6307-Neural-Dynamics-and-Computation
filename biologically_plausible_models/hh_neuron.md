---
jupyter:
  jupytext:
    formats: ipynb,py:percent,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.7
  kernelspec:
    display_name: .venv
    language: python
    name: python3
---

# Hodgkin-Huxley Model
*Owen Page (2025), based on work by V Srinivasa Chakravarthy*



```python
import numpy as np
```

## Defining program parameters

```python
imp_cur = 0.9 # Input current?

k_g_max = 0.36 # Max potassium conductance
k_v_equib = -77 # Potassium reversal potential

na_g_max = 1.20 # Max sodium conductance
na_v_equib = 50 # Sodium reversal potential

leak_g = 0.003 # Leak conductance
leak_v_equib = -54.387 # Leak reversal potential

cm = 0.01 # Membrane conductance
```

```python
dt = 0.01
t_max = 100
t_range = np.arange(0, t_max, dt, dtype=float)
iter_count = len(t_range)

v = -64.9964
m = 0.0530
h = 0.5960
n = 0.3177

na_g_hist = np.zeros([1, iter_count])
na_k_hist = np.zeros([1, iter_count])
v_hist = np.zeros([1, iter_count])
m_hist = np.zeros([1, iter_count])
h_hist = np.zeros([1, iter_count])
n_hist = np.zeros([1, iter_count])
```

```python
for i in range(iter_count):
    pass
```
