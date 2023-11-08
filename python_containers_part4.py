scores = [
   {
     'name': 'name of the player',
     'points': 25  # points the player scored
   }
 ]
scores.append({
    "name": "Bob",
    "points": 50
})

for score in scores:
    print(f"{score['name']} scored {score['points']}")

