from unicodedata import name


broadway_musicals = {
    "1776": "American Airlines Theatre",
    "Aladdin": "New Amsterdam Theatre",
    "Almost Famous": "Bernard B. Jacobs Theatre",
    "A Beautiful Noise, The Neil Diamond Musical": "Broadhurst Theatre",
    "Beetlejuice": "Marquis Theatre",
    "The Book of Mormon": "Eugene O'Neill Theatre",
    "Camelot": "Vivian Beaumont Theater",
    "Chicago": "Ambassador Theatre",
    "Come From Away": "Gerald Schoenfeld Theatre",
    "Dear Evan Hansen": "Music Box Theatre",
    "Funny Girl": "August Wilson Theatre",
    "Hadestown": "Walter Kerr Theatre",
    "Hamilton": "Richard Rodgers Theatre",
    "Into the Woods": "St. James Theatre",
    "& Juliet": "Stephen Sondheim Theatre",
    "Kimberly Akimbo": "Booth Theatre",
    "KPOP": "Circle in the Square Theatre",
    "The Lion King": "Minskoff Theatre",
    "MJ The Musical": "Neil Simon Theatre",
    "Moulin Rouge! The Musical": "Al Hirschfeld Theatre",
    "Mr. Saturday Night": "Nederlander Theater",
    "The Music Man": "Winter Garden Theatre",
    "The Phantom of the Opera": "Majestic Theatre",
    "SIX: The Musical": "Brooks Atkinson Theatre",
    "Some Like It Hot": "Sam S. Shubert Theatre",
    "A Strange Loop": "Lyceum Theatre",
    "Wicked": "Gershwin Theatre"
}

print(f"Tickets are now available for the following Broadway musicals: ")
for musical_name in broadway_musicals:
    print(musical_name)

musical = input("\nWhich Broadway musical would you like to see? ")
theatre = broadway_musicals[musical]

print(f"\nEnjoy {musical} playing at the {theatre}.")

input("\n\tPress ENTER to exit")
