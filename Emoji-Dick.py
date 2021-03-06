dicto = [
('Apple', '🍏'),
('apple', '🍏'),
(' arm', '💪'),
('Arm', '💪'),
('Boat', '⛵'),
('boat', '⛵'),
('BOAT', '⛵'),
('BOOKS', '📚'),
('books', '📚'),
('Books', '📚'),
('book','📘'),
('Book', '📘'),
('BOOK', '📘'),
(' bed', ' 🛏️'),
('Bed', '🛏️'),
('Candle', '🕯️'),
('candle', '🕯️'),
('Coffin', '⚰️'),
('coffin', '⚰️'),
('church', '⛪'),
('Church', '⛪'),
('christmas', '🎄'),
('Christmas', '🎄'),
('CHRISTMAS', '🎄'),
('death', '💀'),
('Death', '💀'),
('DEATH', '💀'),
('Devil', '👿'),
('devil', '👿'),
('DEVIL', '👿'),
('eyes', '👀'),
('Eyes', '👀'),
('ELEPHANT', '🐘'),
('Elephant', '🐘'),
('elephant', '🐘'),
('fish', '🐟'),
('Fish', '🐟'),
('Globe', '🌎'),
('globe', '🌎'),
('GLOBE', '🌎'),
('King', '🤴'),
('king.', '🤴'),
('kiss', '💋'),
('Kiss', '💋'),
('LAMP','🪔'),
('Lamp','🪔'),
('lamp','🪔'),
(' leg', '🦵'),
('Leg', '🦵'),
('Flame', '🔥'),
('FLAME', '🔥'),
('flame', '🔥'),
('FIRE', '🔥'),
('Fire', '🔥'),
('fire', '🔥'),
('fingers', '🖐️'),
('Fingers', '🖐️'),
('FINGERS', '🖐️'),
('finger', '☝️'),
('FINGER', '☝️'),
('Finger', '☝️'),
('Lightning', '⚡'),
('lightning', '⚡'),
('Money', '💰'),
('money', '💰'),
('MONEY', '💰'),
(' heart', ' ❤️ '),
(' Heart', ' ❤️ '),
(' hand', '✋'),
(' Hand', '✋'),
('Hat.', '🎩.'),
(' hat.', ' 🎩.'),
(' hat,', ' 🎩,'),
(' hat-', ' 🎩-'),
('HAT.', '🎩.'),
('House', '🏠'),
('house', '🏠'),
('MOBY-DICK', '🐳'),
('Moby Dick', '🐳'),
('Moby-Dick', '🐳'),
('Monkey', '🐵'),
('monkey', '🐵'),
('MANX', '🇮🇲'),
('Manx', '🇮🇲'),
('manx', '🇮🇲'),
('MOON', '🌕'),
('Moon', '🌕'),
('moon', '🌕'),
('Mermaid', '🧜‍♀️'),
('mermaid', '🧜‍♀️'),
('Merman', '🧜‍♂️'),
('merman', '🧜‍♂️'),
('Queen', '👸'),
('SCHOOLMASTER', '👨‍🏫'),
('Schoolmaster', '👨‍🏫'),
('schoolmaster', '👨‍🏫'),
('school', '🏫'),
('School', '🏫'),
('SCHOOL', '🏫'),
('Shark', '🦈'),
('shark', '🦈'),
('Ship', '🚢'),
(' ship', '🚢'),
(' -ship', '-🚢'),
('SHIP', '🚢'),
('Squid', '🦑'),
('squid', '🦑'),
('storm', '⛈️'),
('Storm', '⛈️'),
('SNOW', '❄️'),
('Snow', '❄️'),
('snow', '❄️'),
('STARBUCK', '⭐💲'),
('Starbuck', '⭐💲'),
('starbuck', '⭐💲'),
('sunrise', '🌅'),
('Sunrise', '🌅'),
('Sunset', '🌇'),
('sunset', '🌇'),
('SKULL', '💀'),
('Skull', '💀'),
('skull', '💀'),
('sword', '🗡️'),
('Sword', '🗡️'),
('SWORD', '🗡️'),
('twine', '🧵'),
('waves', '🌊'),
('Waves', '🌊'),
('Wave', '🌊'),
('wave', '🌊'),
('whaler', '🐋er'),
('Whaler', '🐋er'),
('WHALER', '🐋ER'),
('Whale', '🐋'),
('WHALE', '🐋'),
('whale', '🐋'),
('white', '⬜'),
('White', '⬜'),
('WHITE', '⬜'),
('Wine', '🍷'),
('wine', '🍷')
]

with open('source.html', 'r', encoding='utf8') as book:
  text = book.read()

for word in dicto:
  text = text.replace(word[0], word[1])

with open('Emoji-Dick.html', 'w', encoding='utf8') as output:
  output.write(text)