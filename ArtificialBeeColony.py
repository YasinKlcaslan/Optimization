import numpy as np

def objective_function(position):
    # Amaç fonksiyonu, hedef noktaya olan mesafeyi hesaplar
    target_point = np.array([10, 5, 8])
    return np.linalg.norm(position - target_point)

class WorkerBee:
    def __init__(self, dimensions):
        # İşçi arı başlangıç pozisyonunu rastgele oluşturur ve fitness değerini hesaplar
        self.position = np.random.uniform(-20, 20, dimensions)
        self.fitness = objective_function(self.position)

    def update_position(self, new_position):
        # İşçi arının pozisyonunu ve fitness değerini günceller
        self.position = new_position
        self.fitness = objective_function(new_position)

def bee_colony_algorithm(dimensions, num_bees, num_iterations, search_radius):
    # İşçi arıları oluştur
    bees = [WorkerBee(dimensions) for _ in range(num_bees)]
    
    for iteration in range(num_iterations):
        for bee in bees:
            # Rastgele bir yön belirle ve adım büyüklüğünü hesapla
            random_direction = np.random.uniform(-1, 1, dimensions)
            random_direction /= np.linalg.norm(random_direction)  # Yönü normalize et
            step = search_radius * random_direction  # Adım büyüklüğünü belirle
            new_position = bee.position + step  # Yeni pozisyonu hesapla
            new_fitness = objective_function(new_position)  # Yeni pozisyonun fitness değerini hesapla
            
            # Eğer yeni pozisyon daha iyi bir fitness değerine sahipse pozisyonu güncelle
            if new_fitness < bee.fitness:
                bee.update_position(new_position)
        
        # En iyi işçi arıyı bul
        best_bee = min(bees, key=lambda bee: bee.fitness)
        print(f"Iteration {iteration + 1}: Best Fitness = {best_bee.fitness}")
    
    # En iyi pozisyonu ve fitness değerini döndür
    return best_bee.position, best_bee.fitness

# Parametreler
dimensions = 3  # Boyut sayısı
num_bees = 20  # Arı sayısı
num_iterations = 100  # Iterasyon sayısı
search_radius = 2.0  # Arama yarıçapı

# Arı koloni algoritmasını çalıştır
best_position, best_fitness = bee_colony_algorithm(dimensions, num_bees, num_iterations, search_radius)

print()
print("Best Position:", best_position)  # En iyi pozisyonu yazdır
print("Best Fitness:", best_fitness)  # En iyi fitness değerini yazdır
print()
