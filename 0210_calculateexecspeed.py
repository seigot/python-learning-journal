import csv
import time
import math
from dataclasses import dataclass
from typing import List, Dict, Tuple, Callable


# -----------------------------
# Data model
# -----------------------------
@dataclass(frozen=True)
class SaleRecord:
    sale_id: int
    sale_date: str   # ISO "YYYY-MM-DD" (string compare works for max)
    amount: float
    product: str


# -----------------------------
# Load CSV
# -----------------------------
def load_sales_csv(path: str) -> List[SaleRecord]:
    records: List[SaleRecord] = []
    with open(path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(
                SaleRecord(
                    sale_id=int(row["sale_id"]),
                    sale_date=row["sale_date"],
                    amount=float(row["amount"]),
                    product=row["product"],
                )
            )
    return records


# -----------------------------
# Operations to benchmark
# -----------------------------
def get_latest_sale(records: List[SaleRecord]) -> SaleRecord:
    # Latest by date (O(N))
    return max(records, key=lambda r: r.sale_date)

def compute_total_revenue(records: List[SaleRecord]) -> float:
    # Sum amounts (O(N))
    return sum(r.amount for r in records)

def has_duplicate_sale_ids(records: List[SaleRecord]) -> bool:
    # Set-based duplicate check (O(N) average)
    seen = set()
    for r in records:
        if r.sale_id in seen:
            return True
        seen.add(r.sale_id)
    return False

def search_sale_by_id_linear(records: List[SaleRecord], target_id: int) -> SaleRecord | None:
    # Linear scan (O(N))
    for r in records:
        if r.sale_id == target_id:
            return r
    return None


# -----------------------------
# Benchmark helpers
# -----------------------------
def time_call(fn: Callable[[], object], runs: int = 5) -> float:
    """Return average time in milliseconds."""
    total = 0.0
    for _ in range(runs):
        start = time.perf_counter()
        fn()
        end = time.perf_counter()
        total += (end - start)
    return (total / runs) * 1000.0

def regression_slope_loglog(ns: List[int], ts_ms: List[float]) -> float:
    """
    Estimate slope in log-log space (time ~ N^slope).
    - slope ~ 1 : O(N)
    - slope ~ 0 : O(1) (or dominated by constants)
    - slope ~ 2 : O(N^2)
    """
    xs = [math.log(n) for n in ns]
    ys = [math.log(max(t, 1e-12)) for t in ts_ms]  # avoid log(0)
    x_mean = sum(xs) / len(xs)
    y_mean = sum(ys) / len(ys)
    num = sum((x - x_mean) * (y - y_mean) for x, y in zip(xs, ys))
    den = sum((x - x_mean) ** 2 for x in xs)
    return num / den if den != 0 else float("nan")

def markdown_table(headers: List[str], rows: List[List[str]]) -> str:
    line1 = "| " + " | ".join(headers) + " |"
    line2 = "| " + " | ".join(["---"] * len(headers)) + " |"
    lines = [line1, line2]
    for r in rows:
        lines.append("| " + " | ".join(r) + " |")
    return "\n".join(lines)


# -----------------------------
# Main
# -----------------------------
def main():
    files = [
        ("100", "data/sales_100_product.csv"),
        ("1000", "data/sales_1000_product.csv"),
        ("10000", "data/sales_10000_product.csv"),
        ("100000", "data/sales_100000_product.csv"),
    ]

    Ns: List[int] = [int(label) for label, _ in files]

    # Store times per operation
    times: Dict[str, List[float]] = {
        "Load (CSV -> list)": [],
        "Retrieve latest sale": [],
        "Compute total revenue": [],
        "Check duplicate sale IDs": [],
        "Search sale by ID (linear)": [],
    }

    # For each dataset size, load + run ops
    for label, path in files:
        n = int(label)

        # Measure load time (includes IO + parse)
        load_ms = time_call(lambda: load_sales_csv(path), runs=3)
        records = load_sales_csv(path)  # load once for the remaining ops
        times["Load (CSV -> list)"].append(load_ms)

        # Choose an ID to search: existing (best to test typical successful search)
        # Since your IDs are unique and generated 0..n-1 (duplicate_rate=0),
        # pick one near the end to approximate worst-case for linear search.
        target_id = n - 1

        times["Retrieve latest sale"].append(time_call(lambda: get_latest_sale(records), runs=5))
        times["Compute total revenue"].append(time_call(lambda: compute_total_revenue(records), runs=5))
        times["Check duplicate sale IDs"].append(time_call(lambda: has_duplicate_sale_ids(records), runs=5))
        times["Search sale by ID (linear)"].append(time_call(lambda: search_sale_by_id_linear(records, target_id), runs=5))

    # -----------------------------
    # Table 1: Raw timings (ms)
    # -----------------------------
    headers = ["Operation", "N=100", "N=1,000", "N=10,000", "N=100,000"]
    rows = []
    for op, ts in times.items():
        rows.append([
            op,
            f"{ts[0]:.4f}",
            f"{ts[1]:.4f}",
            f"{ts[2]:.4f}",
            f"{ts[3]:.4f}",
        ])

    print("\n=== Performance Trends: Execution Time (ms, avg) ===")
    print(markdown_table(headers, rows))

    # -----------------------------
    # Table 2: Big-O expectation vs observed trend (log-log slope)
    # -----------------------------
    expected = {
        "Load (CSV -> list)": "O(N)",
        "Retrieve latest sale": "O(N)",
        "Compute total revenue": "O(N)",
        "Check duplicate sale IDs": "O(N) avg",
        "Search sale by ID (linear)": "O(N)",
    }

    headers2 = ["Operation", "Expected Big-O", "Observed slope (log-log)", "Aligns? (trend)"]
    rows2 = []
    for op, ts in times.items():
        slope = regression_slope_loglog(Ns, ts)
        # Simple heuristic alignment check
        exp = expected[op]
        if "O(N)" in exp:
            aligns = "Yes" if 0.7 <= slope <= 1.3 else "Maybe/No"
        elif "O(1)" in exp:
            aligns = "Yes" if -0.2 <= slope <= 0.3 else "Maybe/No"
        else:
            aligns = "Maybe"

        rows2.append([op, exp, f"{slope:.2f}", aligns])

    print("\n=== Big-O Alignment (trend-based) ===")
    print(markdown_table(headers2, rows2))

if __name__ == "__main__":
    main()
