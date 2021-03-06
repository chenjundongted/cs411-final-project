import csv
import json

data = []

with open("data/listings.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        amenities = list(map(lambda x: x.strip("\""), row["amenities"][1:-1].split(",")))
        amenities = list(filter(lambda x: "translation missing" not in x, amenities))
        data.append({
            "name": row["name"],
            "rating": row["review_scores_rating"],
            "amenities": amenities,
            "latitude": row["latitude"],
            "longitude": row["longitude"],
            "reviews_per_month": row["reviews_per_month"],
            "minimum_nights": row["minimum_nights"],
            "neighborhood": row["neighbourhood_cleansed"],
            "airbnb_url": row["listing_url"],
            "image_url": row["picture_url"],
            "price": row["price"]
        })

with open("data/listings.json", "w") as f:
    f.write(json.dumps(data))

print(len(data))
