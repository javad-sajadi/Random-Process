"""
stochastic_simulations.py - Simulation Engine for Fundamental Stochastic & Random Processes
Author: Javad Sajadi
Repository: javad-sajadi/Random-Process

Provides computational simulators and analytical tools for:
  1. Geometric & Negative Binomial waiting times
  2. Poisson point processes & exponential inter-arrival times
  3. Discrete-time Random Walks and Markov Chain transitions
  4. Continuous Brownian Motion paths
"""

import argparse
import numpy as np
import matplotlib.pyplot as plt


def simulate_geometric_process(p: float = 0.2, n_samples: int = 1000):
    """Simulates Geometric distribution trials: number of Bernoulli failures before first success."""
    samples = np.random.geometric(p, size=n_samples)
    theoretical_mean = 1.0 / p
    empirical_mean = np.mean(samples)
    print(f"[Geometric (p={p})] Empirical Mean: {empirical_mean:.4f} | Theoretical Mean: {theoretical_mean:.4f}")
    return samples


def simulate_poisson_process(rate_lambda: float = 5.0, time_horizon: float = 10.0):
    """Simulates a homogeneous Poisson arrival process via exponential inter-arrival increments."""
    arrival_times = [0.0]
    current_time = 0.0
    while current_time < time_horizon:
        delta_t = np.random.exponential(1.0 / rate_lambda)
        current_time += delta_t
        if current_time <= time_horizon:
            arrival_times.append(current_time)

    counts = np.arange(len(arrival_times))
    print(f"[Poisson Process (lambda={rate_lambda})] Total events observed in [0, {time_horizon}]: {len(counts) - 1}")
    return np.array(arrival_times), counts


def simulate_random_walk(n_steps: int = 1000, p_up: float = 0.5):
    """Simulates 1D discrete random walk with step probability p_up."""
    steps = np.where(np.random.rand(n_steps) < p_up, 1, -1)
    trajectory = np.cumsum(np.insert(steps, 0, 0))
    print(f"[Random Walk (N={n_steps}, p={p_up})] Final position: {trajectory[-1]}")
    return trajectory


def simulate_brownian_motion(n_steps: int = 1000, total_time: float = 1.0):
    """Simulates standard 1D continuous Brownian Motion (Wiener Process)."""
    dt = total_time / n_steps
    increments = np.random.normal(0.0, np.sqrt(dt), size=n_steps)
    path = np.cumsum(np.insert(increments, 0, 0.0))
    time_grid = np.linspace(0.0, total_time, n_steps + 1)
    print(f"[Brownian Motion] Path simulated over t in [0, {total_time}] ({n_steps} intervals).")
    return time_grid, path


def run_all_simulations():
    """Runs and plots a multi-panel stochastic process diagnostic figure."""
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    # 1. Geometric Distribution
    geom_samples = simulate_geometric_process(p=0.15, n_samples=2000)
    axes[0, 0].hist(geom_samples, bins=30, density=True, color="#3498db", alpha=0.7, edgecolor="black")
    axes[0, 0].set_title("Geometric Waiting Time Distribution")
    axes[0, 0].set_xlabel("Trials until First Success")
    axes[0, 0].set_ylabel("Probability Density")
    axes[0, 0].grid(True, linestyle="--", alpha=0.5)

    # 2. Poisson Counting Process
    arr_times, counts = simulate_poisson_process(rate_lambda=3.0, time_horizon=15.0)
    axes[0, 1].step(arr_times, counts, where="post", color="#e74c3c", lw=2)
    axes[0, 1].set_title("Homogeneous Poisson Point Process")
    axes[0, 1].set_xlabel("Time (t)")
    axes[0, 1].set_ylabel("Cumulative Event Count N(t)")
    axes[0, 1].grid(True, linestyle="--", alpha=0.5)

    # 3. Random Walk Trajectories
    for i, col in enumerate(["#2ecc71", "#9b59b6", "#f39c12"]):
        rw = simulate_random_walk(n_steps=500, p_up=0.5)
        axes[1, 0].plot(rw, lw=1.5, color=col, label=f"Path {i+1}")
    axes[1, 0].set_title("1D Symmetric Random Walks")
    axes[1, 0].set_xlabel("Step (n)")
    axes[1, 0].set_ylabel("Position S_n")
    axes[1, 0].legend()
    axes[1, 0].grid(True, linestyle="--", alpha=0.5)

    # 4. Brownian Motion
    for i, col in enumerate(["#1abc9c", "#34495e", "#d35400"]):
        t_grid, b_path = simulate_brownian_motion(n_steps=1000, total_time=1.0)
        axes[1, 1].plot(t_grid, b_path, lw=1.2, color=col, label=f"W(t) #{i+1}")
    axes[1, 1].set_title("Continuous Brownian Motion (Wiener Process)")
    axes[1, 1].set_xlabel("Time (t)")
    axes[1, 1].set_ylabel("W(t)")
    axes[1, 1].legend()
    axes[1, 1].grid(True, linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.savefig("stochastic_processes_demo.png", dpi=150)
    print("Saved multi-panel diagnostic figure to 'stochastic_processes_demo.png'.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Stochastic & Random Processes Computational Suite")
    parser.add_argument("--run", action="store_true", help="Run benchmark simulations and generate figure")
    args = parser.parse_args()
    run_all_simulations()
