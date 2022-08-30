glossary = {"string": "a series of characters",
            "integers": "a whole number",
            "float": "any number with a decimal point",
            "comment": "a note in Python that isn't executed code"}

for word in glossary:
    print(f"{word.title()}:")
    print(f"   {glossary[word]}.\n")

glossary["tuple"] = "a list that cannot be changed"
glossary["list"] = "a collection of items in a particular order"

for word in glossary:
    print(f"{word.title()}:")
    print(f"   {glossary[word]}.\n")

input("\t\nPress Enter to exit.")
