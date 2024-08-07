filter = [
    'Title',
    'Year',
    'Released',
    'Runtime',
    'Genre',
    'Director',
    'Writer',
    'Actors',
    'Plot',
    'Language',
    'Country',
    'Awards',
    'Poster',
    'Metascore',
    'imdbVotes',
    'BoxOffice'
]

common_search_words = [
    'love', 'man', 'woman', 'life', 'day', 'night', 'world', 'time', 'story', 'war',
    'death', 'city', 'family', 'dream', 'home', 'friend', 'girl', 'boy', 'heart', 
    'adventure', 'murder', 'mystery', 'secret', 'journey', 'child', 'hope', 'fear', 
    'shadow', 'light', 'dark', 'road', 'end', 'beginning', 'power', 'king', 'queen', 
    'prince', 'princess', 'hero', 'legend', 'soul', 'ghost', 'hunter', 'beast', 
    'monster', 'fight', 'battle', 'escape', 'quest', 'island', 'sea', 'ocean', 
    'river', 'mountain', 'valley', 'forest', 'rain', 'storm', 'fire', 'wind', 'earth',
    'moon', 'star', 'sky', 'sun', 'planet', 'galaxy', 'universe', 'alien', 'robot', 
    'machine', 'castle', 'vampire', 'zombie', 'witch', 'wizard', 'magic', 'spell', 
    'curse', 'potion', 'ring', 'sword', 'shield', 'knight', 'dragon', 'treasure', 
    'gold', 'silver', 'diamond', 'pearl', 'flower', 'tree', 'garden', 'park', 'train', 
    'ship', 'boat', 'car', 'bicycle', 'journey', 'destiny', 'fate', 'luck', 'chance', 
    'truth', 'lie', 'secret', 'whisper', 'echo', 'voice', 'silence', 'scream', 'fear',
    'love', 'betrayal', 'sacrifice', 'revenge', 'honor', 'glory', 'victory', 'defeat', 
    'battle', 'warrior', 'soldier', 'spy', 'agent', 'detective', 'cop', 'crime', 
    'justice', 'law', 'order', 'chaos', 'peace', 'freedom', 'liberty', 'nation', 
    'country', 'state', 'empire', 'republic', 'kingdom', 'realm', 'dynasty', 'tribe', 
    'clan', 'family', 'brother', 'sister', 'mother', 'father', 'child', 'baby', 
    'infant', 'toddler', 'teen', 'adult', 'elder', 'ancestor', 'descendant', 'friend', 
    'enemy', 'ally', 'neighbor', 'stranger', 'foreigner', 'alien', 'immigrant', 
    'refugee', 'citizen', 'subject', 'leader', 'ruler', 'king', 'queen', 'emperor', 
    'dictator', 'president', 'governor', 'mayor', 'chief', 'boss', 'captain', 
    'commander', 'general', 'admiral', 'pilot', 'driver', 'rider', 'walker', 
    'runner', 'jumper', 'swimmer', 'diver', 'climber', 'explorer', 'adventurer', 
    'traveler', 'tourist', 'visitor', 'guest', 'host', 'owner', 'tenant', 'occupant', 
    'resident', 'citizen', 'villager', 'townsman', 'city', 'metropolis', 'capital', 
    'village', 'town', 'settlement', 'community', 'society', 'culture', 'civilization', 
    'tribe', 'clan', 'group', 'team', 'squad', 'gang', 'band', 'party', 'faction', 
    'alliance', 'union', 'coalition', 'organization', 'association', 'club', 'society', 
    'company', 'corporation', 'business', 'enterprise', 'firm', 'agency', 'bureau', 
    'office', 'department', 'division', 'branch', 'unit', 'section', 'team', 
    'committee', 'board', 'council', 'assembly', 'congress', 'parliament', 'senate', 
    'house', 'court', 'jury', 'tribunal', 'judge', 'magistrate', 'justice', 'lawyer', 
    'attorney', 'advocate', 'counsel', 'barrister', 'solicitor', 'prosecutor', 
    'defender', 'defendant', 'plaintiff', 'litigant', 'witness', 'testimony', 
    'evidence', 'proof', 'fact', 'truth', 'lie', 'deception', 'fraud', 'trick', 
    'hoax', 'scam', 'swindle', 'cheat', 'falsification', 'forgery', 'counterfeit', 
    'imposture', 'sham', 'fake', 'phony', 'pretender', 'imitation', 'copy', 'clone', 
    'replica', 'duplicate', 'match', 'twin', 'counterpart', 'partner', 'companion', 
    'associate', 'colleague', 'ally', 'accomplice', 'confederate', 'conspirator', 
    'plotter', 'schemer', 'intriguer', 'manipulator', 'operator', 'player', 'actor', 
    'performer', 'entertainer', 'artist', 'musician', 'singer', 'dancer', 'composer', 
    'painter', 'sculptor', 'writer', 'author', 'poet', 'novelist', 'playwright', 
    'screenwriter', 'director', 'producer', 'filmmaker', 'cinematographer', 
    'photographer', 'editor', 'designer', 'stylist', 'fashion', 'model', 'star', 
    'celebrity', 'icon', 'legend', 'myth', 'folktale', 'fairytale', 'fantasy', 
    'fiction', 'nonfiction', 'biography', 'autobiography', 'memoir', 'history', 
    'chronicle', 'account', 'report', 'narrative', 'story', 'tale', 'yarn', 
    'anecdote', 'fable', 'parable', 'allegory', 'epic', 'saga', 'romance', 'thriller', 
    'mystery', 'horror', 'adventure', 'action', 'comedy', 'drama', 'tragedy', 'melodrama', 
    'satire', 'farce', 'parody', 'spoof', 'burlesque', 'lampoon', 'caricature', 'travesty', 
    'mimicry', 'mockery', 'mock', 'copy', 'imitation', 'simulation', 'replication', 
    'duplication', 'reproduction', 'emulation', 'counterfeit', 'forgery', 'fake', 
    'sham', 'scam', 'fraud', 'deception', 'trick', 'hoax', 'swindle', 'cheat', 'charlatan', 
    'impostor', 'pretender', 'phony', 'fake', 'fraud', 'conman', 'swindler', 'trickster', 
    'hustler', 'scammer', 'schemer', 'plotter', 'conspirator', 'intriguer', 'manipulator', 
    'operator', 'player', 'gambler', 'bettor', 'punter', 'wagerer', 'better', 'risk-taker', 
    'adventurer', 'explorer', 'pioneer', 'trailblazer', 'innovator', 'visionary', 'genius', 
    'prodigy', 'whiz', 'wizard', 'guru', 'maestro', 'master', 'expert', 'specialist', 
    'authority', 'professional', 'veteran', 'old-timer', 'senior', 'elder', 'patriarch', 
    'matriarch', 'ancestor', 'forebear', 'forefather', 'foremother', 'predecessor', 'progenitor', 
    'originator', 'creator', 'founder', 'pioneer', 'trailblazer', 'explorer', 'adventurer', 
    'innovator', 'visionary', 'genius', 'prodigy', 'whiz', 'wizard', 'guru', 'maestro', 'master', 
    'expert', 'specialist', 'authority', 'professional', 'veteran', 'old-timer', 'senior', 
    'elder', 'patriarch', 'matriarch', 'ancestor', 'forebear', 'forefather', 'foremother', 
]