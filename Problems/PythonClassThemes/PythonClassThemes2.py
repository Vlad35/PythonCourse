class ConversationTopics:
    def __init__(self, topics):
        self.topics = topics

    def add_theme(self, value):
        self.topics.append(value)

    def shift_one(self):
        self.topics.insert(0, self.topics.pop())

    def reverse_order(self):
        self.topics.reverse()

    def get_themes(self):
        return self.topics

    def get_first(self):
        return self.topics[0]


topics = ['politics', 'weather', 'sports', 'movies']
conversation = ConversationTopics(topics)

print(conversation.get_themes())

conversation.add_theme('food')
print(conversation.get_themes())

conversation.shift_one()
print(conversation.get_themes())

conversation.reverse_order()
print(conversation.get_themes())

print(conversation.get_first())
