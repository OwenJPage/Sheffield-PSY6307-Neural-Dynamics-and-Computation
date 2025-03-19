# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent,md
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.7
#   kernelspec:
#     display_name: .venv
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Hodgkin-Huxley Model
# *Owen Page (2025), based on work by V Srinivasa Chakravarthy*
#
#

# %% [markdown]
# ## Import libraries
# We first need to import our required libraries. We will be using two libraries, NumPy and MatPlotLib.
#
# + **NumPy** - Used for creating and manipulating high-performance arrays/matrices, also provides a number of mathematical functions.
# + **MatPlotLib** - Allows us create graphs and figures from our data.
#
# We will give NumPy the alias `np` for readibility.
#
# From MatPlotLib we will only import the module `pyplot`, giving it the alias `plt`.

# %%
import numpy as np
from matplotlib import pyplot as plt

# %% [markdown]
# ## Defining program parameters

# %% [markdown]
# First we will define our time-related parameters:
#
# | Name      | Description                                | Units |
# | --------- | ------------------------------------------ | ----- |
# | `n_iter`  | The total number of iterations             | n/a   |
# | `t_max`   | The final time point                       | ms    |
# | `t_range` | Array containing all time points           | n/a   |
# | `dt`      | The amount time increases by per iteration | ms    |
#
# NumPy's `linspace` function is used to generate an array of evenly spaced numbers. The start point, end point, and number of entries is provided, additionally an optional keyword argument `retstep` is used to return step between each entry.
#

# %%
# dt should be 0.01 with these values
n_iter = 10_000
t_max = 100
t_range, dt = np.linspace(0, t_max, n_iter, retstep=True)

# %% [markdown]
#

# %%
imp_cur = 0.9  # Input current?

k_g_max = 0.36  # Max potassium conductance
k_v_equib = -77  # Potassium reversal potential

na_g_max = 1.20  # Max sodium conductance
na_v_equib = 50  # Sodium reversal potential

leak_g = 0.003  # Leak conductance
leak_v_equib = -54.387  # Leak reversal potential

cm = 0.01  # Membrane conductance

# %%
v = -64.9964
m = 0.0530
h = 0.5960
n = 0.3177

# %% [markdown]
#

# %%
na_g_hist = np.zeros([1, iter_count])
na_k_hist = np.zeros([1, iter_count])
v_hist = np.zeros([1, iter_count])
m_hist = np.zeros([1, iter_count])
h_hist = np.zeros([1, iter_count])
n_hist = np.zeros([1, iter_count])

# %% [markdown]
# ## Running the simulation

# %%
for i in range(iter_count):
    pass
