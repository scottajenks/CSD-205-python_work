glossary = {"string": "a series of characters",
            "integers": "a whole number",
            "float": "any number with a decimal point",
            "comment": "a note in Python that isn't executed code"}

for word in glossary:
    print(f"{word.title()}:")
    print(f"   {glossary[word]}.\n")
