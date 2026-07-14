#  Production-Grade Auction Management System 🔨

A secure, time-aware, and highly automated terminal-based auction ledger built using pure Python. This system functions as an in-memory transactional database engine designed to manage asset catalogs, handle live bidding math, enforce temporal limits, and provide robust administrative security controls natively without external dependencies.

---

## Core Architectural Pillars 🚀 

### 1. Advanced Security & Cooldown Gate
* **Brute-Force Protection:** Implements a strict credential validation protocol requiring an administrative login flag (`GlobeMaster`).
* **Progressive Lockout:** Tracks invalid access vectors dynamically. Upon reaching 5 failed attempts, the engine triggers a progressive 15-second system cooldown freeze to mitigate automated scripts.

### 2. In-Memory Relational Ledger (Catalog Management)
* **Dynamic Layout:** Manages product asset mappings via structured nested dictionaries acting as high-performance database tables.
* **Scannable UI:** The catalog renders an aligned grid layout displaying asset metrics, high-bid values, current buyers, and remaining lifespan flags.

### 3. Real-Time Valuation & Buyout Pipeline
* **Method 1 (Manual Settlement):** Provides administrative override privileges to manually close active listings, verify transaction logs, and transition asset states to terminal sold finality.
* **Method 2 (Automated Threshold Break):** Continuously validates input values against pre-configured peak asset evaluations. If a customer bids equal to or higher than the buyout metric, the engine automatically completes the purchase instantly.

### 4. Temporal Lock Gates (Relative Offset Timing)
* **Dynamic Deadlines:** Utilizes machine-clock synchronization (time.time()) to assign precise relative lifespans (in seconds) to new products, bypassing the limitations of static calendar dates during testing.
* **Automated Expiration:** The system intercepts economic input requests. If the millisecond timestamp breaches the dynamic deadline tracking token, the engine denies the transaction, updates the ledger state to `Expired`, and locks the pool.

---

## 🎨 Terminal User Interface Layout

The command-line interface is fully optimized for readability and quick scanning:
* **Strategic Typography:** Uses raw ANSI escape sequences (`\033[...]`) to highlight operational states natively.
* **Color Mapping:** Success routes flash in **Vibrant Green**, critical exceptions/lockouts print in **Bold Red**, index choices stand out in **Cyan**, and headers use **Bold Text Formatting**.

---

## 📊 Inventory Schema Mapping

The local memory storage perfectly mirrors standard relational database tables using this configuration structure:

| Python Dictionary Key | SQL Data Type Equivalent | Description |
| :--- | :--- | :--- |
| `item_id` (Dict Key) | `INT PRIMARY KEY` | Unique numerical identification identifier. |
| `name` | `VARCHAR(100)` | Textual catalog identity of the asset. |
| `highest_bid` | `DECIMAL(10, 2)` | The standing valuation price of the item. |
| `bidder` | `VARCHAR(50)` | Identity string of the leading customer. |
| `peak_price` | `DECIMAL(10, 2)` | Immediate buyout monetary target. |
| `expires_at` | `DOUBLE PRECISION` | Future epoch timestamp checkpoint for limits. |
| `status` | `VARCHAR(20)` | System state tracking (`Active`, `Sold`, `Expired`). |

---

## 🧪 Live Demonstration Playbook

To demonstrate the full execution path of this architecture during evaluation:

1.  **Test Security Gate:** Enter an incorrect credential sequence to showcase the system intercepting unauthorized access attempts.
2.  **Verify Catalog Grid:** Initialize the dashboard, select option `1`, and verify the structured ledger matrix rendering the items and active countdown indicators.
3.  **Execute Temporal Validation:** Add a new listing (option `2`) with a brief runtime window of `30` seconds. Execute a successful bid instantly to prove the transaction path. Allow the clock to expire, attempt a secondary bid, and observe the automated time-lock constraint blocking the operation.
4.  **Execute Value Finalization:** Perform an outbid operation exceeding the peak valuation target to demonstrate immediate automated market closure.