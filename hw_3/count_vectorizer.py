from typing import List
from collections import Counter


class CountVectorizer:
    """Vectorize corpus"""

    def __init__(self, delimiter: str = ' '):
        self.delimiter = delimiter
        self._feature_names = set()
        self._corpus = []
        self._feature_frequency = Counter()

    def __len__(self):
        return len(self._feature_names)

    def fit(self, text_corpus: List[str]):
        for text in text_corpus:
            list_of_words = text.lower().split(self.delimiter)
            self._feature_frequency.update(list_of_words)
            self._corpus.append(list_of_words)
        self._feature_names = set(self._feature_frequency.keys())

    def transform(self):
        pass

    def fit_transform(self, text_corpus: List[str]):
        self.fit(text_corpus)
        return self.transform()

    def get_feature_names(self):
        return self._feature_names
