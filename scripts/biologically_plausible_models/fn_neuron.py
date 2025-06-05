# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # FitzHugh-Nagumo Model

# %%
import numpy as np
from matplotlib import pyplot as plt

# %%
n_iter = 250
t_max = 25
t_range, dt = np.linspace(0, t_max, n_iter, retstep=True)

v = -1.2
w = -0.625

input_current = np.zeros(n_iter, dtype=np.float64)
input_current[0:49] = 0.3

v_hist = np.empty(n_iter, dtype=np.float64)
w_hist = np.empty(n_iter, dtype=np.float64)

# %%
for i, (t, I) in enumerate(np.stack((t_range, input_current), axis=1)):
    dv = v - (v**3 / 3) - w + I
    dw = 0.08 * v - 0.064 * w + 0.056

    v += dv * dt
    w += dw * dt

    v_hist[i] = v
    w_hist[i] = w

    test = 4


# %%
plt.plot(t_range, v_hist, label="v")
plt.plot(t_range, w_hist, label="w")
plt.legend()
plt.show()
