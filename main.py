import csv
import os
from GetPeopleCount import GetPeopleCount

CSV_FILE = "gym_count.csv"


def save_to_csv(timestamp, count):
    file_exists = os.path.exists(CSV_FILE)

    with open(CSV_FILE, "a", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["timestamp", "count"])

        writer.writerow([timestamp, count])


def main():
    result = GetPeopleCount()

    if result is None:
        print("沒有抓到體適能中心人數")
        return

    timestamp, count = result
    save_to_csv(timestamp, count)

    print(f"[{timestamp}] 已儲存人數：{count}")


if __name__ == "__main__":
    main()