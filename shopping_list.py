shopping_list = {
    "piekarnia": ["chleb", "pączek", "bułki"],
    "warzywniak": ["marchew", "seler", "rukola"]
}
shopping_list["piekarnia"] = [f.capitalize() for f in shopping_list["piekarnia"]]
shopping_list["warzywniak"] = [f.capitalize() for f in shopping_list["warzywniak"]]

count = 0
for key, value in shopping_list.items():
    if isinstance(value, list):
         count += len(value)

