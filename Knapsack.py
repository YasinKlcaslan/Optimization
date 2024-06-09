import random  # Rastgele sayı üretmek için gerekli modül

# Çanta probleminin maksimum ağırlık sınırı
max_w = 40

# Eşyaların ağırlık listesi
w = [7, 5, 10, 15, 5, 3, 8, 4, 9, 12]

# Eşyaların değer listesi
v = [10, 15, 5, 8, 20, 10, 7, 17, 5, 3]


# Rastgele bir çözüm (ikili dizge) oluşturmak için fonksiyon
def generate_random_solution(m):
    """
    Rastgele bir ikili dizge oluşturur.

    Args:
        m: Dizi uzunluğu (eşya sayısı)

    Returns:
        Rastgele ikili dizge (çözüm)
    """
    binary_list = []  # İkili dizgeyi tutmak için boş bir liste
    for _ in range(m):  # Dizi uzunluğunca rastgele değerler oluştur
        binary_list.append(random.randint(0, 1))  # 0 veya 1 ekle
    return binary_list  # Oluşturulan rastgele çözümü döndür


# Çözümün fitness değerini hesaplamak için fonksiyon
def calculate_fitness_value(x):
    """
    Çözümün fitness değerini hesaplar.

    Args:
        x: Çözüm (ikili dizge)

    Returns:
        Fitness değeri
    """
    s_v = 0  # Toplam değer
    s_w = 0  # Toplam ağırlık
    for i in range(len(x)):  # Çözümün her bir elemanını kontrol et
        s_v += x[i] * v[i]  # Eğer 1 ise değeri ekle
        s_w += x[i] * w[i]  # Eğer 1 ise ağırlığı ekle
    return s_v if s_w <= max_w else 1000  # Eğer toplam ağırlık sınırı aşılırsa, fitness 1000

# İki ebeveynden çaprazlama ile yeni bir çocuk çözüm oluşturmak için fonksiyon
def crossover(x1, x2):
    """
    Çaprazlama işlemini gerçekleştirir.

    Args:
        x1: Ebeveyn 1 çözümü (ikili dizge)
        x2: Ebeveyn 2 çözümü (ikili dizge)

    Returns:
        Çocuk çözümü (ikili dizge)
    """
    c = [0] * len(x1)  # Çocuk çözüm için boş bir liste
    p = random.randint(2, 8)  # Rastgele bir kesme noktası seç
    # Çocuğa ilk p geni birinci ebeveynden kopyala
    c[:p] = x1[:p]
    # Çocuğa geri kalan genleri ikinci ebeveynden kopyala
    c[p:] = x2[p:]
    return c  # Yeni çocuk çözümü döndür


# Çanta problemini çözmek için ana fonksiyon
def knapsack_solver(m):
    """
    Çanta problemini çözer.

    Args:
        m: Dizi uzunluğu (eşya sayısı)

    Returns:
        En iyi çözüm (ikili dizge), En iyi fitness değeri
    """
    # Başlangıçta rastgele bir çözüm oluştur
    current_solution = generate_random_solution(m)
    # Mevcut çözümü en iyi çözüm olarak kabul et
    best_solution = current_solution
    best_fitness = calculate_fitness_value(current_solution)  # Fitness'ı hesapla

    # 1000 döngü boyunca çaprazlama yap ve en iyi çözümü bul
    for _ in range(1000):
        # Mevcut çözümle rastgele yeni bir çözümü çaprazla
        new_solution = crossover(current_solution, generate_random_solution(m))
        new_fitness = calculate_fitness_value(new_solution)  # Yeni çözümün fitness'ını hesapla

        # Eğer yeni çözüm, en iyi çözümden daha yüksek fitness'a sahipse, onu en iyi çözüm yap
        if new_fitness > best_fitness:
            best_solution = new_solution
            best_fitness = new_fitness

        current_solution = new_solution  # Mevcut çözümü güncelle

    # En iyi çözümü ve fitness'ını döndür
    return best_solution, best_fitness


# Çanta problemini çözmek için düğüm sayısını belirle
m = 10  # Eşya sayısı
# En iyi çözümü ve fitness'ını bul
best_solution, best_fitness = knapsack_solver(m)

# En iyi çözümü ve fitness'ını yazdır
print(f"Best Solution: {best_solution}")
print(f"Best Fitness: {best_fitness}")
