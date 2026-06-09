import math

def calculate_diversity_indices(species_counts):
    total_n = sum(species_counts)
    if total_n == 0:
        return {'shannon': 0, 'margalef': 0, 'simpson': 0, 'richness': 0}
    
    S = len(species_counts)
    shannon = 0
    simpson_d = 0
    
    for n in species_counts:
        if n > 0:
            p_i = n / total_n
            shannon -= p_i * math.log(p_i)
            simpson_d += p_i ** 2
            
    margalef = (S - 1) / (total_n - 1) if total_n > 1 else 0
    
    return {'shannon': round(shannon, 4), 'margalef': round(margalef, 4), 'simpson': round(1 - simpson_d, 4), 'richness': S}

if __name__ == '__main__':
    print(calculate_diversity_indices([10, 5, 2, 1]))
