# DATAVERSE Challenge: The VelocityMart

# Chaos

## 1. THE MANDATE

You are the **Interim Head of Operations** for VelocityMart. Average fulfillment times have
collapsed from 3.8 to 6.2 minutes, and safety incidents (picker collisions, product damage,
and spoilage) are skyrocketing. Your task is to rescue the Bangalore dark stores from
operational entropy. The executive team requires a **Strategic Intervention Plan** supported by
an interactive diagnostic tool (Dashboard) and a mathematically optimized slotting map for
Week 91.

## 2. THE CHALLENGE DATA

You are provided with 90 weeks of historical data. Warning: This data is "poisoned" with
sensor noise, human gaming, and structural corruption. Accuracy in data cleaning is as
important as the optimization itself.
● **sku_master.csv** : Product attributes including dimensions and fragility, but contains
hidden "decimal drift" errors.
● **order_history.csv** : Transactional logs showing high-velocity SKUs and significant
temporal spikes.
● **warehouse_constraints.csv** : The "Physical Truth" of the facility, including Weight limits,
Temperature zones, and Aisle Widths.
● **picker_movement.csv** : Noisy GPS logs including timestamps and travel distances,
containing evidence of illegal shortcuts.

## 3. COMPETITION PILLARS (150 Points)

### A. Data Forensics & Integrity (30 pts)

Document your cleaning pipeline thoroughly. You must identify and resolve:
● **Decimal Drift** : Which SKUs have weights recorded 10x higher than reality due to unit
errors?
● **The Shortcut Paradox** : Prove which pickers (e.g., Picker 07) appear "efficient" only
because they are skipping safety zones and barriers.
● **Ghost Inventory** : Identify SKUs currently assigned to bins that do not officially exist in
the warehouse topology.


### B. The Decision-Support Dashboard (40 pts)

Submit a link or screenshots of an interactive dashboard (Streamlit, PowerBI, Tableau, etc.). It
MUST visualize:
● **Heatmaps** : Identify "High-Collision Aisles" (specifically the bottleneck in Aisle B) during
the 19:00 peak hours.
● **Spoilage Risk** : The total inventory value currently violating temperature constraints (e.g.,
frozen items in ambient zones).
● **The Forklift Dead-zone** : Visualize the "Unspoken Physics" where forklift restocking
windows block picker access.

### C. The Strategic Slotting Map (40 pts)

Submit a final_slotting_plan.csv for Week 91. This will be processed through a private
simulation engine.
● **Relocation Efficiency** : You have a limited "Labor Budget." Moving a SKU costs points;
you must optimize for the highest impact moves, not just total perfection.
● **Hard Constraints** : Placing Ambient items in Frozen zones, or exceeding shelf weight
limits, results in an automatic 0 for this section.

### D. The Executive Pitch (40 pts)

A 5-slide memo addressing the VelocityMart Board:
● **The Chaos Score** : Propose and justify your own custom weighted metric for "Warehouse
Health."
● **Phase 1 Roadmap** : Which 50 SKUs would you move tonight to achieve the highest
immediate reduction in fulfillment time?
● **Sensitivity Analysis** : How resilient is your plan if order volumes spike by an additional
20%?

## 4. SUBMISSION GUIDELINES

Your final submission must consist of three distinct files:

1. **Report (PDF)** : Detailed forensic findings, data cleaning methodology, and Strategic
    Roadmap.
2. **Dashboard Link** : Link to the live dashboard (hosted on GitHub/Streamlit Cloud) and a
    recorded screen-share video demonstrating its features.
3. **Slotting Map (CSV)** : Must contain exactly two columns: SKU_ID and Bin_ID. This acts as
    the quantitative tie-breaker.
**Submission Link** : LINK
**Submission Process** : Upload the three files to the designated Drive link provided by the
competition host before the presentation deadline. Create a folder with your team name and


upload the above mentioned files.

## 5. THE TWIST: THE "UNSPOKEN" PHYSICS

During your initial walkthrough, the manager mentioned: _"The forklift can't enter Aisle B if
more than 2 pickers are already there."_ This specific rule is **not** explicitly coded in the CSV
constraints. Your slotting map and dashboard must account for this physical bottleneck to
avoid massive simulation penalties.


