from pathlib import Path
import csv

scores_path = Path.home() / "practice_files" / "scores.csv"
# print(scores_path.exists())

with scores_path.open(mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    # scores = [row for row in reader]
    scores = list(row for row in reader)

# print(scores)

high_scores = {}

for item in scores:
    name = item["name"]
    score = int(item["score"])

    if name not in high_scores:
        high_scores[name] = score
    else:
        high_scores[name] = max(high_scores[name], score)

# print(high_scores)

output_file = Path.home() / "practice_files" / "high_scores.csv"

with output_file.open(mode="w", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["index", "name", "high_score"])
    writer.writeheader()
    rows_list = []
    index = 1
    for name in high_scores:
        row_dict = {"index":index, "name":name, "high_score":high_scores[name]}
        # writer.writerow(row_dict)
        rows_list.append(row_dict)
        index += 1
    writer.writerows(rows_list)

with output_file.open(mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)