# FINDING 4: OPERATIONAL RISKS & CONSTRAINTS ANALYSIS
**Report Date:** February 05, 2026
**Subject:** High-Risk Operational Bottlenecks & Safety Violations
**Analysis Vector:** Spatial Congestion & Thermal Compliance

---

## 1. The "Forklift Dead-zone" (Aisle B Analysis)
We discovered a critical flaw in the warehouse layout logic: **Resource Contention between Humans and Machines.**

### The Physics of the Constraint
*   **Forklift Width:** 1.8m
*   **Aisle Width:** 2.5m
*   **Picker Width (with cart):** 0.8m
*   **The Math:** $1.8m + 2(0.8m) = 3.4m$ (Required) vs $2.5m$ (Available).
*   **The Rule:** A Forklift CANNOT enter Aisle B if $>1$ picker is present.

### The Peak Hour Reality (19:00 - 20:00)
We analyzed picker movement logs for the peak hour of 7 PM.

| Metric | Value | Implications |
| :--- | :--- | :--- |
| **Pickers in Aisle B** | **>2 for 60 mins** | Blockage Condition = TRUE |
| **Forklift Access Window** | **0.0 minutes** | Restocking is PHYSICALLY IMPOSSIBLE |
| **Stock-out Probability** | **100%** | By 8 PM, high-velocity items will be empty |

**Conclusion:** The warehouse is effectively operating at partial capacity because its replenishment artery is severed during the hours it is needed most.

### Top Congestion Hotspots (The "Traffic Jam")
| Rank | Aisle | Movements/Hr | Status |
| :--- | :--- | :--- | :--- |
| 1 | **A01** | **3,028** | Gridlock |
| 2 | **C08** | 711 | Heavy |
| 3 | **D02** | 673 | Heavy |
| 4 | **E22** | 610 | Heavy |
| 5 | **B21** | 575 | Heavy |
| 6 | **B25** | 556 | Heavy |

---

## 2. Temperature Compliance (Financial Risk Assessment)
The second major risk is **Spoilage**. Inventory is currently stored in zones that violate its thermal requirements.

### The Risk Ledger
| Risk Category | Count | % of Total | Est. Value |
| :--- | :--- | :--- | :--- |
| **Total Inventory** | 800 SKUs | 100% | ₹400,000 |
| **All Violations** | 490 SKUs | 61.3% | ₹245,000 |
| **CRITICAL Violations** | **290 SKUs** | **36.3%** | **₹145,000** |

**"Critical" Definition:**
*   **Frozen (-18°C) → Ambient (25°C):** Product liquefies in < 60 mins.
*   **Refrigerated (4°C) → Ambient (25°C):** Bacterial growth in < 4 hours.

### The "Kill List" (Top 15 Critical Items)
These items are currently destroying value. **Immediate Move Required.**

| SKU ID | Category | Requirement | Current Zone (Ambient) | Slot |
| :--- | :--- | :--- | :--- | :--- |
| **SKU-10000** | Frozen | Frozen | Ambient | F05-B-01 |
| **SKU-10001** | Groceries | Refrigerated | Ambient | A19-F-19 |
| **SKU-10004** | Dairy | Frozen | Ambient | B24-B-05 |
| **SKU-10005** | Snacks | Frozen | Ambient | F19-E-14 |
| **SKU-10009** | Snacks | Frozen | Ambient | F22-B-09 |
| **SKU-10010** | Groceries | Frozen | Ambient | B03-C-14 |
| **SKU-10011** | Health | Frozen | Ambient | A04-D-17 |
| **SKU-10012** | Health | Frozen | Ambient | A01-E-17 |
| **SKU-10013** | Health | Refrigerated | Ambient | A01-F-01 |
| **SKU-10015** | Groceries | Frozen | Ambient | A22-B-07 |
| **SKU-10016** | Beverages | Frozen | Ambient | A01-F-01 |
| **SKU-10019** | Dairy | Frozen | Ambient | F09-E-13 |
| **SKU-10020** | Groceries | Frozen | Ambient | D19-A-16 |
| **SKU-10023** | Health | Refrigerated | Ambient | E16-A-03 |
| **SKU-10024** | Groceries | Refrigerated | Ambient | F07-B-01 |

---

## 3. Zone Utilization vs Capacity
Why are items in the wrong zones? Is it lack of space?

| Zone | Utilization % | Status |
| :--- | :--- | :--- |
| **Ambient** | 5.8% | Empty |
| **Chilled** | 4.2% | Empty |
| **Frozen** | 4.2% | Empty |

**Insight:** The zones are **NOT FULL.** Utilization is < 6% across the board. The misplaced items are purely a result of **Bad Process**, not **Lack of Capacity**. This is a training issue, not a real estate issue.
