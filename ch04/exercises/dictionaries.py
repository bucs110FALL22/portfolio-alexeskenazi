article = "Pokémon GO is one of the most successful mobile games of all time, breaking records like fastest to earn $100 million and most-downloaded in its first month of release. To date, it has grossed almost $2 billion in revenue and been downloaded 800 million times. Although no longer the global phenomenon it was in 2016, the game remains incredibly popular."

substitutions = {
    "Pokemon":"Monsters",
    "successful":"boring",
    "breaking":"destroying",
    "records":"happiness",
    "fastest":"tornados",
    "earn":"ruin",
    "$100":"lives",
    "million": "everyday",
    "downloaded": "loathed",
    "release":"beta",
    "billion":"USD",
    "phenomenon":"game",
    "popular": "dead" }

for key, value in substitutions.items():
   article = article.replace(key, value)
print(article)