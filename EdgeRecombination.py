import random  # Rastgele sayı üretmek için gerekli modül

# Rastgele iki parent oluşturmak için kullanılan fonksiyon
def initialize_parents(n):
    # Birden n'e kadar olan tam sayıları kullanarak iki parent listesi oluştur
    parent1 = list(range(n))
    parent2 = list(range(n))
    # Parent listelerini rastgele karıştır
    random.shuffle(parent1)
    random.shuffle(parent2)
    return parent1, parent2  # İki parent listesini döndür

# Edge recombination (kenar rekombinasyonu) kullanarak parent'lardan komşu listesi oluşturma fonksiyonu
def edge_recombination(parent1, parent2):
    adjacency_list = {}  # Boş bir komşu listesi oluştur

    # Parent'ların her bir elemanı için komşu düğümleri bul
    for i in range(len(parent1)):
        neighbors = []  # Komşuları tutmak için bir liste
        index1 = parent1.index(parent1[i])  # Parent1'deki elemanın indeksini bul
        index2 = parent2.index(parent1[i])  # Parent2'deki elemanın indeksini bul

        # Parent1'deki elemanın sol ve sağ komşularını ekle
        neighbors.append(parent1[(index1 - 1) % len(parent1)])  # Sol komşu (mod kullanarak döngüsel indeks)
        neighbors.append(parent1[(index1 + 1) % len(parent1)])  # Sağ komşu
        
        # Parent2'deki elemanın sol ve sağ komşularını ekle
        neighbors.append(parent2[(index2 - 1) % len(parent2)])  # Sol komşu (mod kullanarak döngüsel indeks)
        neighbors.append(parent2[(index2 + 1) % len(parent2)])  # Sağ komşu

        # Komşuları tekrar etmeyen bir şekilde ekleyerek benzersiz bir komşu listesi oluştur
        unique_neighbors = list(set(neighbors))
        
        # Parent1'in elemanını ve benzersiz komşularını komşu listesine ekle
        adjacency_list[parent1[i]] = unique_neighbors

    # Parent'ların son elemanları için komşuları güncelle
    last_index1 = parent1[-1]  # Parent1'in son elemanı
    last_index2 = parent2[-1]  # Parent2'nin son elemanı

    # Son elemanlar için komşuları baştan ve sondan gelen değerlerle güncelle
    adjacency_list[last_index1].append(parent1[0])  # Başlangıç elemanı
    adjacency_list[last_index1].append(parent1[-2])  # Sondan ikinci eleman
    adjacency_list[last_index2].append(parent2[0])  # Parent2'nin başlangıç elemanı
    adjacency_list[last_index2].append(parent2[-2])  # Parent2'nin sondan ikinci elemanı

    return adjacency_list  # Oluşturulan komşu listesini döndür

# Test etmek için başlangıç ayarlarını belirle
n = 8  # Düğüm sayısı
parent1, parent2 = initialize_parents(n)  # Rastgele iki parent oluştur
print("Parent 1:", parent1)  # Parent1'i yazdır
print("Parent 2:", parent2)  # Parent2'yi yazdır

# Parent'lardan oluşturulan komşu listesini al
adjacency_list = edge_recombination(parent1, parent2)

# Komşu listesini yazdır
print("Adjacency List:")
for node, neighbors in adjacency_list.items():  # Her düğüm için komşuları listele
    print(node, ":", neighbors)  # Düğüm ve komşularını yazdır
