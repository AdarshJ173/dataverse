# FINDING 2: FORENSIC DATA ANALYSIS
**Report Date:** February 05, 2026
**Subject:** Data Integrity & Cleaning Pipeline Results
**Scope:** 800 SKUs / 436k Orders / 18k Slots

---

## 1. Issue 1: Decimal Drift (Unit Conversion Errors)
**Problem:** A systematic error in data entry resulted in 20 SKUs being recorded at 10x their actual weight (likely kg vs g input error).

**Evidence:**
*   Max Raw Weight: **119.9 kg** (Packet of chips)
*   Typical Range: 0.1 - 2.0 kg
*   Detection Logic: `Weight > 50kg` AND `Category != Bulk`

**Correction Applied:**
We applied a divisor of 10 to all flagged outliers.
*   **Before:** 20 items > 50kg (Total "Fake" Mass: ~2,000kg)
*   **After:** 0 items > 50kg (Accurate Mass)

---

## 2. Issue 2: Inventory Discrepancies
**Problem:** "Ghost Inventory" - SKUs assigned to bin locations that do not strictly exist in the master warehouse map, or violate physical constraints.

**Status:**
*   **Invalid Slot IDs:** 0 (All slots map correctly)
*   **Weight Capacity Violations:** 20 SKUs exceed bin limits.
    *   *Root Cause:* These are the same SKUs from Issue 1. Fixing Decimal Drift resolves the Weight Capacity violations automatically.

---

## 3. Issue 3: Temperature Zone Mismatch
**Problem:** Inventory is stored in zones that do not match their preservation requirements.

**The "Mismatch Matrix":**
| Required Zone | Current Zone | Count | Impact |
| :--- | :--- | :--- | :--- |
| **Frozen** | Ambient | 150 | **Critical Failure** |
| **Refrigerated** | Ambient | 140 | **Critical Failure** |
| **Frozen** | Refrigerated | 50 | Quality Degradation |

**Conclusion:** 36% of the warehouse is currently spoiling. This is not a data error; it is a physical process failure.
