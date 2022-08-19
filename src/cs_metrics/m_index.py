import numpy as np                                                                                                                                

def compute_m_index(word_number_each_language, n_keep=4):
    """ Compute M index.

    Guzmán, Gualberto A., et al. "Metrics for Modeling Code-Switching Across Corpora." INTERSPEECH. 2017.
    """
    k = len(word_number_each_language)
    if k < 2:
        # print("If only one language or no language, the M-index is zero.")
        return 0.0

    total_words = 0
    for word_number in word_number_each_language:
        total_words += word_number

    sum_pj_square = 0.0
    for word_number in word_number_each_language:
        pj_square = (float(word_number)/float(total_words))**2
        sum_pj_square += pj_square

    numerator = (1.0 - sum_pj_square)
    denomeinator = (k-1.0)*sum_pj_square
    m_index = round(numerator/denomeinator, 4)
    return m_index

if __name__ == "__main__":
    example = [500, 500]
    print(example, compute_m_index(example))
    example = [500, 1]
    print(example, compute_m_index(example))
    example = [5, 10]
    print(example, compute_m_index(example))

