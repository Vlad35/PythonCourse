class ConversationTopics:
    def __init__(self, topics):
        self.topics = topics
    
    def add_theme(self, value):
        self.topics.append(value)
    
    def shift_one(self):
        self.topics.insert(0, self.topics.pop())
    
    def reverse_other(self):
        self.topics = self.topics[::-1]
    
    def get_themes(self):
        return self.topics
    
    def get_first(self):
        return self.topics[0]

topics = ['politics', 'weather', 'sports', 'movies']
conversation = ConversationTopics(topics)

print(conversation.get_themes()) # ['politics', 'weather', 'sports', 'movies']

conversation.add_theme('food')
print(conversation.get_themes()) # ['politics', 'weather', 'sports', 'movies', 'food']

conversation.shift_one()
print(conversation.get_themes()) # ['food', 'politics', 'weather', 'sports', 'movies']

conversation.reverse_other()
print(conversation.get_themes()) # ['movies', 'sports', 'weather', 'politics', 'food']

print(conversation.get_first()) # 'movies'
