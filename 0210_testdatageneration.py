import csv
import random
from datetime import date, timedelta
from pathlib import Path

def random_date(start: date, end: date) -> date:
    delta_days = (end - start).days
    return start + timedelta(days=random.randint(0, delta_days))

def generate_sales_csv(
    n: int,
    out_path: str,
    duplicate_rate: float = 0.0,
    seed: int = 42,
    start_date: date = date(2024, 1, 1),
    end_date: date = date(2024, 12, 31),
    amount_min: float = 1.00,
    amount_max: float = 500.00,
    unique_product: bool = True,   # ★追加
) -> None:
    if not (0.0 <= duplicate_rate <= 1.0):
        raise ValueError("duplicate_rate must be between 0.0 and 1.0")

    random.seed(seed)

    out_file = Path(out_path)
    out_file.parent.mkdir(parents=True, exist_ok=True)

    unique_ids = list(range(n))
    written_ids = []

    with out_file.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["sale_id", "sale_date", "amount", "product"])

        for i in range(n):
            # sale_id: 一部だけ重複させる
            if written_ids and random.random() < duplicate_rate:
                sale_id = random.choice(written_ids)
            else:
                sale_id = unique_ids[i]

            sale_dt = random_date(start_date, end_date).isoformat()
            amount = round(random.uniform(amount_min, amount_max), 2)

            # ★ product をユニークにする
            # どんなに sale_id が重複しても product は i（行番号）でユニーク保証
            if unique_product:
                product = f"Product_{i:06d}"
            else:
                product = f"Product_{random.randint(0, 9):02d}"  # 例：重複ありにしたい場合

            writer.writerow([sale_id, sale_dt, f"{amount:.2f}", product])
            written_ids.append(sale_id)

    print(f"Generated: {out_file} (n={n}, duplicate_rate={duplicate_rate}, unique_product={unique_product})")


if __name__ == "__main__":
    sizes = [100, 1_000, 10_000, 100_000]

    # ユニーク product
    for n in sizes:
        generate_sales_csv(n, f"data/sales_{n}_product.csv", duplicate_rate=0.0, seed=42, unique_product=True)

    # sale_id は 1% 重複、product はユニーク
#    for n in sizes:
#        generate_sales_csv(n, f"data/sales_{n}_product.csv", duplicate_rate=0.01, seed=99, unique_product=True)
