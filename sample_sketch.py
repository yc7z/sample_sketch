import random

REPEATS = 100

def random_indexed_k_mer(s1, s2, k):
    l1 = len(s1)
    l2 = len(s2)
    
    i = -1
    event_occurs = 0
    # repeat until we draw a valid k_mer from the multiset
    while not (0 <= i <= l1 - k or l1 <= i <= l1 + l2 - k):
        i = random.randint(0, l1 + l2 - k)
    # the sample k_mer is from s1
    if i <= l1 - k:
        sample_k_mer = s1[i : (i + k)]
        k_mer_index_s1 = 1
        
        # compute the k_mer index of sample_k_mer in s1
        while i > 0:
            i -= 1
            if s1[i : (i + k)] == sample_k_mer:
                k_mer_index_s1 += 1
                
        # search within s2 for the indexed sample k-mer
        k_mer_index_s2 = 0
        for j in range(l2 - k + 1):
            if s2[j : (j + k)] == sample_k_mer:
                k_mer_index_s2 += 1
            if k_mer_index_s2 == k_mer_index_s1 and s2[j : (j + k)] == sample_k_mer:
                event_occurs = 1
                break
            
    else: # l1 <= i <= l1 + l2 -k, meaning the sampled k_mer is from s2
        x = i - l1
        sample_k_mer = s2[x : (x + k)]
        k_mer_index_s2 = 1
        
        # compute the k_mer index of sample_k_mer in s2
        while x > 0:
            x -= 1
            if s2[x : (x + k)] == sample_k_mer:
                k_mer_index_s2 += 1
                
        # search within s1 for the indexed sample k-mer
        k_mer_index_s1 = 0
        for y in range(l1 - k + 1):
            if s1[y : (y + k)] == sample_k_mer:
                k_mer_index_s1 += 1
            if k_mer_index_s1 == k_mer_index_s2 and s1[y : (y + k)] == sample_k_mer:
                event_occurs = 1
                break
            
    return event_occurs

def estimate_weighted_jaccard(s1, s2, k):
    occurences = 0
    for i in range(REPEATS):
        occurences += random_indexed_k_mer(s1, s2, k)
    p = occurences / REPEATS
    return p / (2 - p)


if __name__ == '__main__':
    s1 = 'AACCGGTT' * 30
    s2 = 'AACCGGTT' * 10
    print(estimate_weighted_jaccard(s1, s2, 4))
    
        