import random  # Rastgele sayı üretmek için gerekli modül

# Ağırlıklar ve değerler listesi, ayrıca maksimum ağırlık limiti
weights = [7, 5, 10, 15, 5, 3, 8, 4, 9, 12]
values = [10, 14, 5, 8, 20, 10, 7, 17, 5, 3]
max_weight = 40  # Maksimum toplam ağırlık sınırı

# Rastgele bir çözüm oluşturma fonksiyonu
def generate_random_solution():
    """0 ve 1'lerden oluşan bir liste üreterek rastgele bir çözüm oluşturur."""
    return [random.randint(0, 1) for _ in range(len(weights))]

# Bir çözümün fitness'ını hesaplama fonksiyonu
def calculate_fitness(solution):
    """Çözümün toplam değerini ağırlık sınırı içinde hesaplar."""
    total_weight = sum(solution[i] * weights[i] for i in range(len(weights)))  # Toplam ağırlık
    total_value = sum(solution[i] * values[i] for i in range(len(values)))  # Toplam değer

    if total_weight > max_weight:  # Eğer toplam ağırlık sınırı aşarsa
        return 1000  # Yüksek ceza değeri
    else:
        return total_value  # Aksi halde toplam değeri döndürür

# Tek nokta crossover ile iki parent'tan çocuk oluşturma fonksiyonu
def single_point_crossover(parent1, parent2):
    """Tek nokta crossover ile iki çocuk çözüm oluşturur."""
    crossover_point = random.randint(1, len(parent1) - 1)  # Crossover noktası
    # İlk çocuk, birinci parent'ın başı ve ikinci parent'ın sonu ile oluşturulur
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    # İkinci çocuk, ikinci parent'ın başı ve birinci parent'ın sonu ile oluşturulur
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2  # İki çocuğu döndürür

# Bir çözümü belirli bir mutasyon oranı ile mutasyona uğratma fonksiyonu
def mutate(solution, mutation_rate):
    """Belirli bir olasılıkla bir çözümde mutasyon uygular."""
    mutated_solution = solution.copy()  # Orijinal çözümün bir kopyası
    for i in range(len(solution)):  # Çözümdeki her bir bileşeni kontrol eder
        if random.random() < mutation_rate:  # Mutasyon olasılığına göre değiştir
            mutated_solution[i] = 1 - mutated_solution[i]  # 0'ı 1'e, 1'i 0'a çevir
    return mutated_solution  # Mutasyona uğramış çözümü döndürür

# Bir çözümü ve fitness'ını okunaklı bir formatta yazdırma fonksiyonu
def print_solution(solution, fitness):
    """Çözümü ve fitness'ını okunaklı bir formatta yazdırır."""
    print(f"Çözüm: {solution}")
    print(f"Toplam Ağırlık: {sum(solution[i] * weights[i] for i in range(len(weights)))}")  # Toplam ağırlık
    print(f"Toplam Değer: {fitness}")  # Toplam değer/fayda

# Nüfus boyutu ve başlangıç populasyonunu oluşturma
population_size = 10  # Başlangıç populasyonu boyutu
population = [generate_random_solution() for _ in range(population_size)]  # Rastgele çözümler

# Crossover ve mutasyon işlemleriyle beş döngü
for i in range(5):
    # Nüfustan rastgele iki ebeveyn seç
    parent1, parent2 = random.choices(population, k=2)  # Rastgele iki ebeveyn
    
    # Ebeveynlerin çözüm ve fitness'ını yazdır
    print(f"\n**Ebeveyn 1:**")
    print_solution(parent1, calculate_fitness(parent1))  # Ebeveyn 1'in detayları
    print(f"\n**Ebeveyn 2:**")
    print_solution(parent2, calculate_fitness(parent2))  # Ebeveyn 2'nin detayları

    # Ebeveynlerden crossover ile iki çocuk oluştur
    child1, child2 = single_point_crossover(parent1, parent2)
    
    # Çocukların çözüm ve fitness'ını yazdır
    print(f"\n**Çocuk 1:**")
    print_solution(child1, calculate_fitness(child1))  # Çocuk 1'in detayları
    print(f"\n**Çocuk 2:**")
    print_solution(child2, calculate_fitness(child2))  # Çocuk 2'nin detayları

    # Mutasyon oranı ve mutasyon işlemi
    mutation_rate = 0.1  # Mutasyon oranı
    child1 = mutate(child1, mutation_rate)  # Çocuk 1'e mutasyon uygula
    child2 = mutate(child2, mutation_rate)  # Çocuk 2'ye mutasyon uygula
    
    # Mutasyondan sonra çocukları populasyona ekle
    population.extend([child1, child2])

# En iyi çözümü ve fitness'ını bul
best_solution = max(population, key=calculate_fitness)  # En iyi çözüm
best_fitness = calculate_fitness(best_solution)  # En iyi çözümün fitness'ı

# En iyi çözümü yazdır
print("\nEn İyi Çözüm:")
print_solution(best_solution, best_fitness)  # En iyi çözümün detayları
