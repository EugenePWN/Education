import numpy as np

class Word2Vec:
    def __init__(self, sentences, vector_size=100, window=5, learning_rate=0.01, epochs=10):
        self.sentences = sentences
        self.vector_size = vector_size
        self.window = window
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.word_to_index = {}
        self.index_to_word = {}
        self.vocabulary_size = 0
        self.embeddings = None

    def build_vocabulary(self):
        unique_words = sorted(set(self.sentences))
        self.vocabulary_size = len(unique_words)
        self.word_to_index = {word: i for i, word in enumerate(unique_words)}
        self.index_to_word = {i: word for word, i in self.word_to_index.items()}

    def initialize_embeddings(self):
        self.embeddings = np.random.uniform(low=-0.5/self.vector_size, high=0.5/self.vector_size,
                                             size=(self.vocabulary_size, self.vector_size))

    def train(self):
        for epoch in range(self.epochs):
            for sentence in self.sentences:
                words = sentence.split()
                for i, target_word in enumerate(words):
                    target_index = self.word_to_index[target_word]
                    context_words = words[max(0, i - self.window):i] + words[i+1:i+self.window+1]
                    for context_word in context_words:
                        context_index = self.word_to_index[context_word]
                        predicted = np.dot(self.embeddings[target_index], self.embeddings[context_index])
                        error = predicted - 1  
                        self.embeddings[target_index] -= self.learning_rate * error * self.embeddings[context_index]
                        self.embeddings[context_index] -= self.learning_rate * error * self.embeddings[target_index]

    def get_word_vector(self, word):
        return self.embeddings[self.word_to_index[word]]

def train(data: str):
    sentences = data.split()
    word2vec = Word2Vec(sentences=sentences)
    word2vec.build_vocabulary()
    word2vec.initialize_embeddings()
    word2vec.train()
    w2v_dict = {word: word2vec.get_word_vector(word) for word in word2vec.word_to_index}
    return w2v_dict

data = "Даня лох"

w2v_dict = train(data)
print(w2v_dict)