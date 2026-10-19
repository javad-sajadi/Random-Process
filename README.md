# Stochastic & Random Processes: Computational Laboratory

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-blue.svg)](https://numpy.org/)
[![SciPy](https://img.shields.io/badge/SciPy-Applied%20Mathematics-darkblue.svg)](https://scipy.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A comprehensive computational laboratory implementing numerical simulations, empirical convergence theorems, and statistical properties of fundamental **Stochastic and Random Processes**.

---

## 📌 Project Overview

This repository contains over 180 computational experiments exploring both discrete-time and continuous-time stochastic systems.

### Covered Stochastic Systems
1. **Geometric & Negative Binomial Stopping Times:** Simulation of waiting times for Bernoulli success events, distribution limits, and empirical expectation matching.
2. **Poisson Point Processes:** Homogeneous Poisson counting processes $N(t)$, exponential inter-arrival times $\Delta t \sim \mathrm{Exp}(\lambda)$, and superposition theorems.
3. **Discrete-Time Random Walks:** 1D symmetric and asymmetric random walks, recurrence properties, first hitting times, and reflection principles.
4. **Continuous Brownian Motion (Wiener Process):** Increments $W(t + \Delta t) - W(t) \sim \mathcal{N}(0, \Delta t)$, path continuity, and variance scaling.
5. **Markov Chains:** Transition matrix state convergence, stationary distribution solving, and ergodic limit theorems.

---

## 🚀 Quick Start

### 1. Installation
```bash
git clone https://github.com/javad-sajadi/Random-Process.git
cd Random-Process
pip install -r requirements.txt
```

### 2. Run the Benchmark Simulation Suite
Generates multi-panel simulation trajectories for Geometric, Poisson, Random Walk, and Brownian motion processes:
```bash
python stochastic_simulations.py
```

### 3. Interactive Jupyter Notebook
Explore the detailed 180+ interactive derivations and simulations:
```bash
jupyter notebook ClassWork.ipynb
```

---

## 📁 Repository Structure

```
.
├── ClassWork.ipynb               # 180+ interactive stochastic process experiments and derivations
├── stochastic_simulations.py     # Modular simulation suite for Poisson, Geometric, and Brownian processes
├── requirements.txt              # Environment dependencies (NumPy, SciPy, Matplotlib)
└── .gitignore                    # Git ignore rules for cached artifacts and checkpoints
```

---

## 📜 Author & License
- **Author:** [Javad Sajadi](https://github.com/javad-sajadi)
- **License:** MIT License
