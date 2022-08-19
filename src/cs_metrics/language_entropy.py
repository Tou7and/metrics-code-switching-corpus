import numpy as np                                                                                                                                

def compute_language_entropy(word_number_each_language, n_keep=4):
    """ Compute language entropy.
    
    maximum value depends on number of languages: log2(k)
    
    Guzmán, Gualberto A., et al. "Metrics for Modeling Code-Switching Across Corpora." INTERSPEECH. 2017.

    Args:
        word_number_each_language(list): word number (or token number) of each language, Ex. [50, 50] for 2 languges, 50 words each.

    Returns:
        languge_entropy(float)
    """
    # k = len(word_number_each_language)
    number_of_language = len(word_number_each_language)

    if number_of_language < 2:
        # "If only one language or no language, return zero.
        return 0.0

    total_words = sum(word_number_each_language)
        
    pj = [] 
    for word_number in word_number_each_language:
        tmp_pj = word_number/float(total_words)
        if tmp_pj == 0:
            tmp_pj = np.finfo(float).eps
        pj.append(tmp_pj)
    
    pj = np.array(pj)
    pj_log2 = np.log2(pj)

    language_entropy = 0.0
    for idx in range(number_of_language):
        language_entropy += pj[idx]*pj_log2[idx]

    language_entropy = (-1)*language_entropy
    language_entropy = round(language_entropy, n_keep)
    return language_entropy

if __name__ == "__main__":
    example = [500, 500]
    print(example, compute_language_entropy(example))
    example = [500, 1]
    print(example, compute_language_entropy(example))
    example = [5, 10]
    print(example, compute_language_entropy(example))

