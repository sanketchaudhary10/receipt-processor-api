from models import Receipt
import math
import re
from datetime import datetime

def calculate_points(receipt: Receipt) -> int:
    points = 0

    # Rule 1: 1 point per alphanumeric character in retailer name
    points += len(re.findall(r'[a-zA-Z0-9]', receipt.retailer))

    # Rule 2: 50 points if total is a round dollar amount
    if receipt.total.endswith(".00"):
        points += 50

    # Rule 3: 25 points if total is multiple of 0.25
    if (float(receipt.total) * 100) % 25 == 0:
        points += 25

    # Rule 4: 5 points for every 2 items
    points += (len(receipt.items) // 2) * 5

    # Rule 5: description length multiple of 3 → ceil(price * 0.2)
    for item in receipt.items:
        desc = item.shortDescription.strip()
        if len(desc) % 3 == 0:
            points += math.ceil(float(item.price) * 0.2)

    # Rule 6: Skip — LLM only

    # Rule 7: 6 points if day is odd
    purchase_date = datetime.strptime(receipt.purchaseDate, "%Y-%m-%d")
    if purchase_date.day % 2 == 1:
        points += 6

    # Rule 8: 10 points if time is between 2pm and 4pm (14:00–16:00)
    purchase_time = datetime.strptime(receipt.purchaseTime, "%H:%M")
    if 14 <= purchase_time.hour < 16:
        points += 10

    return points
