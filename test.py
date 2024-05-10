import requests

# /joke request
response = requests.post(
    "http://localhost:8000/joke/invoke",
    json={'input': {'topic': 'roosters'}}
)
print(response.json())
print('\n\n\n\n\n\n\n')



content = """
Once upon a time, in a land far beyond the reaches of the common map, where the forests whispered secrets through their leaves and the mountains touched the skies with their snow-capped fingers, there was a village that thrived in harmony with nature. This village was known as Eldoria, a place where magic was as common as the stones and rivers, and where every creature, big or small, had a role in the great tapestry of life.

In Eldoria, there lived a young woman named Aria. Aria was not like the other villagers; she possessed a unique gift, the ability to communicate with the animals. From the smallest ant to the mightiest eagle, Aria understood their languages, and in turn, they understood her. This gift was a sacred bond, passed down through her family for generations, and with it came a responsibility to maintain the balance of nature.

Aria lived a peaceful life, aiding her fellow villagers by resolving disputes between humans and animals, healing injured creatures, and guiding lost travelers through the forest. However, peace in Eldoria was not to last. Dark clouds began to gather on the horizon, both figuratively and literally. A great evil had awakened in the depths of the Darkwood, a forest so dense and shadowed that light itself seemed to avoid its grasp.

The villagers spoke of a darkness that crept through the woods, corrupting everything it touched. Animals became aggressive, plants withered, and anyone who ventured into the Darkwood was never seen again. Fear gripped Eldoria, and for the first time in centuries, the harmony between man and nature was at risk.

Determined to save her village and restore balance, Aria embarked on a quest into the heart of the Darkwood. Accompanied by her loyal companions, a wise old owl named Theron and a courageous wolf named Fenrir, Aria faced challenges that tested her strength, wisdom, and heart. She encountered creatures corrupted by the darkness, puzzles that challenged her intellect, and truths that questioned her beliefs.

As Aria ventured deeper into the Darkwood, she discovered that the source of the corruption was an ancient spirit, one that had been twisted by a betrayal long forgotten. This spirit, in its pain and rage, sought to destroy Eldoria and all that represented the harmony it had once cherished.

Realizing that violence could not heal the spirit's wounds, Aria sought to understand its pain, to listen to its story. Through her gift of communication, she learned of the betrayal that had turned the spirit's heart to stone. Aria felt a deep compassion for the spirit, and with the support of Theron and Fenrir, she worked to heal the ancient wounds.

In the end, Aria's kindness and understanding prevailed. The spirit, freed from its centuries of pain and anger, chose to become the guardian of the Darkwood, ensuring that the corruption would never return. The balance between man and nature was restored, and Aria returned to Eldoria a hero.

However, Aria knew that her journey had changed her. She had faced the darkness, both within the forest and within herself, and emerged stronger. Aria continued to live in Eldoria, her bond with the natural world deeper than ever. She knew that as long as the villagers remembered to listen to the whispers of the forest, harmony would prevail.

And so, Eldoria thrived once more, a testament to the enduring power of understanding and compassion. The villagers remembered Aria's journey for generations, a story of courage, friendship, and the unbreakable bond between humans and nature. In the heart of the village, a statue was erected in her honor, a reminder of the young woman who had ventured into the darkness and brought light back to Eldoria.

Thus ends the tale of Aria, the Whisperer of the Wild, a story that echoes through the ages, reminding us all of the delicate balance that exists between man and nature, and the strength that lies in understanding and empathy.
"""

# /summary request
response = requests.post(
    "http://localhost:8000/summary/invoke",
    json={'input': {'content': str(content)}}
)
print(response.json())
print('\n\n\n\n\n\n\n')


false_fact = "ducks have long blue fur like tigers and big trunks like dolphins"
true_fact = "penguins cannot fly and tigers cannot fly either. they both can swim."
# /fact-check request
response = requests.post(
    "http://localhost:8000/fact-check/invoke",
    json={'input': {'info': str(false_fact)}}
)
print(response.json())
print("\n\n")
response = requests.post(
    "http://localhost:8000/fact-check/invoke",
    json={'input': {'info': str(true_fact)}}
)
print(response.json())
print('\n\n\n\n\n\n\n')


update = "source-lightning has a new UI option! Try it out!"
# marketing team
response = requests.post(
    "http://localhost:8000/sourcebox-marketing-team/invoke",
    json={'input': {'update': str(update)}}
)
print(response.json())
print('\n\n\n\n\n\n\n')









