shopping_list = {
    "piekarnia": ["chleb", "pączek", "bułki"],
    "warzywniak": ["marchew", "seler", "rukola"]
}
shopping_list["piekarnia"] = [f.capitalize() for f in shopping_list["piekarnia"]]
shopping_list["warzywniak"] = [f.capitalize() for f in shopping_list["warzywniak"]]
