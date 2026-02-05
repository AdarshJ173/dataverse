# FINDING 5: WORKFORCE PERFORMANCE & DEMAND PATTERNS
**Report Date:** February 05, 2026
**Subject:** Human Factors, Efficiency Anomalies, and Order Velocity Analysis
**Data Universe:** 174,421 Pick Events / 436,052 Orders

---

## 1. Human Efficiency Benchmarks
We baselined the performance of the 12-person picking fleet. The operations are generally efficient, but specific anomalies point to process deviations.

### Fleet Averages (The "Normal" State)
| Metric | Benchmark Value | Interpretation |
| :--- | :--- | :--- |
| **Avg Travel Distance** | **33.5 m** | Efficient route planning |
| **Avg Pick Time** | **2.00 min** | Industry standard is 1.8-2.5m |
| **Avg Speed** | **16.8 m/min** | Brisk walking speed with cart |

---

## 2. Workforce Efficiency Anomaly: PICKER-07 Investigation
Our anomaly detection algorithm flagged **PICKER-07** as a statistical outlier. This is a classic case of "Goodhart's Law"—where a metric (Time) becomes a target, and the system is gamed.

### The Evidence File
| Metric | Fleet Avg | PICKER-07 | Variance | Z-Score |
| :--- | :--- | :--- | :--- | :--- |
| **Distance Traveled** | 35.0m | **17.5m** | **-50%** | **-2.81** (Anomaly) |
| **Time per Pick** | 2.00 min | 2.00 min | 0% | 0.00 |
| **Calculated Speed** | 17.5 m/min | **8.76 m/min** | **-50%** | -2.81 |

### The Forensic Conclusion
How can a picker travel **HALF** the distance but take the **SAME** amount of time?
1.  **Hypothesis A:** They are teleporting. (Impossible)
2.  **Hypothesis B:** They are extremely slow walkers but find magical routes. (Unlikely)
3.  **Hypothesis C:** They are cutting through **Restricted Safety Zones** (e.g., jumping conveyor belts or cutting through the loading dock) which shortens the distance but forces them to move slower/wait for checks.

**Verdict:** PICKER-07 is violating safety protocols to minimize walking, but not gaining any speed advantage. This is a **Safety Risk** with zero operational upside.

### Comparative Picker Table
| Picker ID | Avg Dist (m) | Avg Time (min) | Speed (m/min) | Total Picks | Integrity Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **PICKER-07** | **17.52** | **2.00** | **8.76** | **14,350** | SUSPECT |
| PICKER-01 | 34.85 | 2.00 | 17.42 | 14,557 | Verified |
| PICKER-11 | 34.89 | 2.00 | 17.45 | 14,526 | Verified |
| PICKER-08 | 35.00 | 2.00 | 17.50 | 14,643 | Verified |
| PICKER-12 | 34.96 | 2.00 | 17.48 | 14,437 | Verified |
| PICKER-06 | 34.93 | 2.00 | 17.46 | 14,459 | Verified |

---

## 3. Demand Velocity & Order Composition
Understanding the "Flow" of the business.

### Velocity Statistics
*   **Total Orders:** 436,052
*   **Unique Orders:** 998 (High re-order rate implies recurring bulk subscriptions)
*   **Avg Line Items:** **437 items/order**
    *   *Note:* This is exceptionally high for Quick Commerce. It suggests VelocityMart is functioning more as a **B2B Micro-Fulfillment Center** (supplying local bodegas) rather than a B2C Dark Store.

### Temporal Patterns
*   **Peak Day:** Friday & Saturday (Weekend Surge)
*   **Peak Hour:** 19:00 (Dinner Rush/Restock window)
*   **Lull Hour:** 03:00 - 05:00 (Ideal for Cycle Counting)

### Top 10 High-Velocity Products
These 10 items drive 2.4% of total volume.

| Rank | SKU | Category | Orders |
| :--- | :--- | :--- | :--- |
| 1 | SKU-10094 | Snacks | 643 |
| 2 | SKU-10646 | Beverages | 623 |
| 3 | SKU-10734 | Health | 608 |
| 4 | SKU-10144 | Groceries | 605 |
| 5 | SKU-10220 | Frozen | 603 |
| 6 | SKU-10551 | Snacks | 603 |
| 7 | SKU-10550 | Snacks | 602 |
| 8 | SKU-10298 | Snacks | 600 |
| 9 | SKU-10647 | Snacks | 600 |
| 10 | SKU-10758 | Dairy | 598 |

**Strategic Note:** 4 of the Top 10 are **Snacks**. This category should be moved to the front of the warehouse (Aisle A) to minimize travel time for 40% of picks.
