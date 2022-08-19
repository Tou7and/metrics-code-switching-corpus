def compute_i_index(lang_id_list, n_keep=4):
    """ Compute I index based on lang-id list.

    Args:
        lang_id_list(list): ex. 硬 train 一 發 >> ['ZH', 'EN', 'ZH', 'ZH']

    Returns:
        i_index(float)   
    """
    total_word = len(lang_id_list)
    total_switch = 0
    if total_word <= 1:
        return 0.0

    for idx in range(total_word - 1):
        jdx = idx +1 
        lang_id_current = lang_id_list[idx]
        lang_id_next = lang_id_list[jdx]
        if lang_id_current != lang_id_next:
            total_switch += 1

    i_index = float(total_switch) / float(total_word - 1) 
    i_index = round(i_index, n_keep)
    # print("total switch: ", total_switch)
    # print("total length: ", total_word)
    return i_index

if __name__ == "__main__":
    print(compute_i_index(['z', 'e', 'z', 'e']))
    print(compute_i_index(['z', 'z', 'z', 'e']))
    print(compute_i_index(['z', 'z', 'z', 'z']))

