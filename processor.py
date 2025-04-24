from models import Receipt
import math
import re
from datetime import datetime

def calculate_points(receipt: Receipt) -> int:
    points = 0

    # Rule a
    points += len(re.findall(r'[a-zA-Z0-9]', receipt.retailer))

    # Rule b
    if receipt.total.endswith(".00"):
        points += 50

    # Rule c
    if (float(receipt.total) * 100) % 25 == 0:
        points += 25

    # Rule d
    points += (len(receipt.items) // 2) * 5

    # Rule e
    for item in receipt.items:
        desc = item.shortDescription.strip()
        if len(desc) % 3 == 0:
            points += math.ceil(float(item.price) * 0.2)

    # Rule g
    purchase_date = datetime.strptime(receipt.purchaseDate, "%Y-%m-%d")
    if purchase_date.day % 2 == 1:
        points += 6

    # Rule h
    purchase_time = datetime.strptime(receipt.purchaseTime, "%H:%M")
    if 14 <= purchase_time.hour < 16:
        points += 10

    return points
