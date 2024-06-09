import math  # Matematiksel işlemler için
import random  # Rastgele sayı üretmek için
import copy  # Derin kopya için

# Mesafe matrisini tanımlayın (şehirler arası mesafeleri temsil eder)
dist = [[0, 2, 4, 3, 5],
        [2, 0, 7, 6, 2],
        [4, 7, 0, 3, 4],
        [3, 6, 3, 0, 8],
        [5, 2, 4, 8, 0]]  # 5 şehir arası mesafeler

# Bir rotanın toplam mesafesini hesaplayan fonksiyon
def evaluate(current):
    """
    Verilen bir rota için toplam mesafeyi hesaplar.

    Args:
        current: Şehirlerin rotası (liste formatında)

    Returns:
        total_distance: Toplam mesafe
    """
    total_distance = 0  # Toplam mesafe için başlangıç değeri
    # Rotadaki ardışık şehirlerin mesafesini toplayarak toplam mesafeyi hesapla
    for i in range(len(current) - 1):
        total_distance += dist[current[i] - 1][current[i + 1] - 1]  # İndeksleri doğru ayarla
    print(total_distance)  # Hesaplanan toplam mesafeyi yazdır
    return total_distance  # Toplam mesafeyi döndür


# Rotadaki iki şehri rastgele yer değiştiren fonksiyon
def movement(current):
    """
    Rotadaki iki rastgele şehri yer değiştirir.

    Args:
        current: Şehirlerin mevcut rotası (liste formatında)

    Returns:
        new_solution: İki şehir yer değiştirilmiş yeni rota
    """
    # Mevcut rotayı değiştirmemek için derin kopya yapın
    new_solution = copy.deepcopy(current)
    # Rotadaki iki rastgele şehri seçin ve yer değiştirin
    i, j = random.sample(range(len(current)), 2)  # Eşsiz iki indeks seç
    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]  # İki şehri değiştir
    return new_solution  # Yeni rotayı döndür


# Benzetilmiş Tavlama algoritmasını uygulayan fonksiyon
def simulated_annealing():
    """
    Gezgin Satıcı Problemi (TSP) için Benzetilmiş Tavlama algoritmasını uygular.
    """
    dimension = len(dist)  # Mesafe matrisindeki boyut (şehir sayısı)
    # 1'den şehir sayısına kadar şehir listesini oluşturun
    city_list = list(range(1, dimension + 1))
    # Rastgele bir başlangıç ​​rotası oluşturun
    current_solution = random.sample(city_list, dimension)

    # Başlangıç ​​rotasını en iyi çözüm olarak kabul edin
    best_solution = current_solution.copy()
    best_fitness = evaluate(best_solution)  # En iyi rotanın toplam mesafesini hesapla

    # Benzetilmiş tavlama algoritması için başlangıç sıcaklık ve diğer parametreler
    temperature = 100.0  # Başlangıç sıcaklığı
    cooling_rate = 0.99  # Sıcaklık düşüş oranı
    iterations = 10  # Her döngüde kaç iterasyon yapılacak
    acceptance_parameter = 10  # Kabul edilen yeni çözümlerin sayısı

    # Algoritma boyunca iterasyon yapın
    for _ in range(iterations):  # Ana döngü
        for _ in range(acceptance_parameter):  # Her iterasyon için kabul parametresi kadar çalış
            # Rotada rastgele iki şehri yer değiştirerek yeni bir çözüm oluşturun
            new_solution = movement(current_solution)
            # Yeni çözümün toplam mesafesini hesaplayın
            new_fitness = evaluate(new_solution)

            # Eğer yeni çözüm daha iyiyse, kabul edin
            delta_fitness = new_fitness - best_fitness  # Fitness farkı
            if delta_fitness < 0:  # Kesin iyileştirme durumu
                current_solution = new_solution  # Yeni çözümü mevcut çözüm yapın
                best_solution = new_solution.copy()  # En iyi çözümü güncelleyin
                best_fitness = new_fitness  # En iyi fitness'ı güncelleyin
            else:
                # Daha kötü çözümleri kabul etmek için bir olasılık hesaplayın
                probability = math.exp(-delta_fitness / temperature)  # Benzetilmiş tavlama prensibi
                if random.random() < probability:  # Rastgele bir olasılıkla kabul edin
                    current_solution = new_solution  # Kabul edilen çözümü güncelleyin

        # Sıcaklığı düşürmek için soğutma oranını kullanın
        temperature *= cooling_rate

    # En iyi çözümü ve toplam mesafesini yazdırın
    print("Best Solution:", best_solution)
    print("Best Fitness:", best_fitness)  # Toplam mesafesi

# Benzetilmiş Tavlama algoritmasını çalıştırmak için kontrol edici kod
if __name__ == "__main__":
    simulated_annealing()  # Ana fonksiyonu çalıştır
