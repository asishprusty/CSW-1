# Program to check voting eligibility using filter() and dictionary comprehension

# Sample input: list of tuples (name, age, nationality)
voters = [("Amit", 22, "Indian"),
          ("John", 30, "USA"),
          ("Neha", 17, "Indian"),
          ("Ravi", 19, "Indian")]

# a) Use filter() to extract eligible voters (age ≥ 18 and nationality = "Indian")
eligible_voters = list(filter(lambda v: v[1] >= 18 and v[2].lower() == "indian", voters))

# Extract only names of eligible voters
eligible_names = [v[0] for v in eligible_voters]

# b) Count and display total number of eligible voters
print("Eligible:", eligible_names)
print("Count:", len(eligible_names))

# c) Build dictionary using dictionary comprehension
result = {
    "Eligible": [v[0] for v in voters if v[1] >= 18 and v[2].lower() == "indian"],
    "Not Eligible": [v[0] for v in voters if not (v[1] >= 18 and v[2].lower() == "indian")]
}

print(result)
