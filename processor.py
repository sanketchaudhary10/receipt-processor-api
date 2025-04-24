from models import Receipt
import math
import re
from datetime import datetime

def calculate_points(receipt: Receipt) -> int:
    total = 0

    rule_a = len(re.findall(r'[a-zA-Z0-9]', receipt.retailer))
    print("Rule a:", rule_a)

    rule_b = 50 if receipt.total.endswith(".00") else 0
    print("Rule b:", rule_b)

    rule_c = 25 if (float(receipt.total) * 100) % 25 == 0 else 0
    print("Rule c:", rule_c)

    rule_d = (len(receipt.items) // 2) * 5
    print("Rule d:", rule_d)

    rule_e = 0
    for item in receipt.items:
        desc = item.shortDescription.strip()
        if len(desc) % 3 == 0:
            added_points = math.ceil(float(item.price) * 0.2)
            rule_e += added_points
    print("Rule d:", rule_d)

    purchase_date = datetime.strptime(receipt.purchaseDate, "%Y-%m-%d")
    rule_g = 6 if purchase_date.day % 2 == 1 else 0
    print("Rule g:", rule_g)

    purchase_time = datetime.strptime(receipt.purchaseTime, "%H:%M")
    rule_h = 10 if 14 <= purchase_time.hour < 16 else 0
    print("Rule h:", rule_h)

    total = rule_a + rule_b + rule_c + rule_d + rule_e + rule_g + rule_h
    print("Total points calculated:", total)

    return total


