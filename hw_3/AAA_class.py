from typing import List
from math import log

from hw_3.count_vectorizer import CountVectorizer


class TfidfTransformer:
    """TfidfTransformer"""

    @staticmethod
    def tf_transform(count_matrix: List[List[int]]) -> List[List[float]]:
        """
        Generate tf matrix from term-word frequency
        :param count_matrix: count_matrix (term word frequency)
        :return: tf matrix
        """
        tf_matrix_out = []
        for vector in count_matrix:
            tf_matrix_out.append([freq / sum(vector) for freq in vector])
        return tf_matrix_out

    @staticmethod
    def idf_transform(count_matrix: List[List[int]]) -> List[float]:
        """
        Generate idf matrix from term-word frequency
        :param count_matrix: term-word frequency matrix
        :return: idf matrix
        """
        vector_idf_transform = []
        zip_generator_col = zip(*count_matrix)
        for _ in range(len(count_matrix[0])):
            current_sum = sum([1 for x in next(zip_generator_col) if x])
            vector_idf_transform.append(log((len(count_matrix) + 1)
                                            / (current_sum + 1)) + 1)
        return vector_idf_transform

    def fit_transform(self, count_matrix: List[List[int]]) \
            -> List[List[float]]:
        """
        Sequent usage of fit&transform into tf-idf matrix
        :param count_matrix: term-word frequency matrix
        :return: Tf-idf matrix
        """
        tf_matrix = self.tf_transform(count_matrix)
        idf_matrix = self.idf_transform(count_matrix)
        tf_idf_matrix = []
        for vector in tf_matrix:
            current_vector = []
            zipped_vector_col = zip(vector, idf_matrix)
            for tf, idf in zipped_vector_col:
                current_vector.append(tf * idf)
            tf_idf_matrix.append(current_vector)
        return tf_idf_matrix


class TfifdVectorizer(CountVectorizer):
    """TfIdf Vectorizer"""

    def __init__(self):
        super().__init__()
        self.tfidf = TfidfTransformer()

    def fit_transform(self, text_corpus: List[str]) -> List[List[float]]:
        count_matrix = super().fit_transform(text_corpus)
        return self.tfidf.fit_transform(count_matrix)


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = TfifdVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(count_matrix)
