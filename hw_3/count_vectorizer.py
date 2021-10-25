from typing import List
from collections import Counter


class CountVectorizer:
    """Vectorize text corpus"""

    def __init__(self, delimiter: str = ' '):
        self.delimiter = delimiter
        self._feature_names = []
        self._corpus = []
        self._feature_frequency = []

    def __len__(self):
        return len(self._feature_names)

    def fit(self, text_corpus: List[str]) -> None:
        """
        Tokenize text corpus into features by @self.delimiter.
        Get counts of any feature in sentence.

        :param text_corpus - list of sentences to be processed

        O(N * max(M_i))
        """
        features = []
        for txt_index, text in enumerate(text_corpus):
            list_of_words = text.lower().split(self.delimiter)
            self._feature_frequency.append(Counter(list_of_words))
            self._corpus.append(list_of_words)
            for word in list_of_words:
                if word not in features:
                    features.append(word)
            self._feature_names = features

    def transform(self) -> List[List[int]]:
        """
        Generate count matrix - each row corresponds to sentence in corpus.
        Each column corresponds to feature-tokens from the whole corpus.

        :return: count matrix for text corpus
        """
        count_matrix_out = []
        if len(self._corpus) == 0:
            raise ValueError('Use fit method before transform!')
        for txt_index, _ in enumerate(self._corpus):
            current_counter = []
            for feature in self._feature_names:
                current_counter.append(self._feature_frequency[txt_index][feature])
            count_matrix_out.append(current_counter)
        return count_matrix_out

    def fit_transform(self, text_corpus: List[str]) -> List[List[int]]:
        """
        Pipeline of consistent fit & transform

        :return: count matrix for text corpus
        """
        self.fit(text_corpus)
        return self.transform()

    def get_feature_names(self) -> List[str]:
        """
        Get list of tokens from corpus
        """
        if len(self._feature_names) == 0:
            raise ValueError('The list of tokens is empty. Use fit method before getting features')
        return self._feature_names


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    assert count_matrix == [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                            [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
    print(count_matrix)
    feature_list = vectorizer.get_feature_names()
    assert feature_list == ['crock', 'pot', 'pasta', 'never', 'boil',
                            'again', 'pomodoro', 'fresh', 'ingredients',
                            'parmesan', 'to', 'taste']
    print(feature_list)
