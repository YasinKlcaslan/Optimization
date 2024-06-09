import numpy as np

class GreyWolfOptimizer:
    def __init__(self, fitness_function, num_dimensions, num_wolves=5, max_iterations=100, maxX=50, maxY=50):
        # Başlangıç parametreleri
        self.fitness_function = fitness_function  # Fitness fonksiyonu
        self.num_dimensions = num_dimensions  # Boyut sayısı
        self.num_wolves = num_wolves  # Kurt sayısı
        self.max_iterations = max_iterations  # Maksimum iterasyon sayısı
        self.maxX = maxX  # X ekseninde maksimum değer
        self.maxY = maxY  # Y ekseninde maksimum değer

    def optimize(self):
        # Başlangıç pozisyonlarını rastgele oluştur
        positions = np.random.uniform(0, self.maxX, (self.num_wolves, self.num_dimensions))
        fitness_values = np.array([self.fitness_function(pos) for pos in positions])

        # Alpha, Beta ve Delta kurtlarının pozisyonlarını ve fitness değerlerini belirle
        alpha_idx = np.argmax(fitness_values)
        beta_idx = np.argsort(fitness_values)[-2]
        delta_idx = np.argsort(fitness_values)[-3]

        alpha_position = positions[alpha_idx].copy()
        beta_position = positions[beta_idx].copy()
        delta_position = positions[delta_idx].copy()

        for t in range(self.max_iterations):
            # a parametresi her iterasyonda azalır
            a = 2 - 2 * t / self.max_iterations

            for i in range(self.num_wolves):
                # Her kurt için yeni pozisyonları hesapla
                A1 = 2 * a * np.random.uniform(0, 1, self.num_dimensions) - a
                C1 = 2 * np.random.uniform(0, 1, self.num_dimensions)
                D1 = np.abs(C1 * alpha_position - positions[i])
                X1 = alpha_position - A1 * D1

                A2 = 2 * a * np.random.uniform(0, 1, self.num_dimensions) - a
                C2 = 2 * np.random.uniform(0, 1, self.num_dimensions)
                D2 = np.abs(C2 * beta_position - positions[i])
                X2 = beta_position - A2 * D2

                A3 = 2 * a * np.random.uniform(0, 1, self.num_dimensions) - a
                C3 = 2 * np.random.uniform(0, 1, self.num_dimensions)
                D3 = np.abs(C3 * delta_position - positions[i])
                X3 = delta_position - A3 * D3

                # Yeni pozisyonu hesapla
                positions[i] = (X1 + X2 + X3) / 3

            # Pozisyonları sınırlamalar dahilinde tut
            positions = np.clip(positions, 0, self.maxX)

            # Yeni fitness değerlerini hesapla
            fitness_values = np.array([self.fitness_function(pos) for pos in positions])

            # Alpha, Beta ve Delta kurtlarının pozisyonlarını ve fitness değerlerini güncelle
            alpha_idx = np.argmax(fitness_values)
            beta_idx = np.argsort(fitness_values)[-2]
            delta_idx = np.argsort(fitness_values)[-3]

            alpha_position = positions[alpha_idx].copy()
            beta_position = positions[beta_idx].copy()
            delta_position = positions[delta_idx].copy()

            best_fitness = fitness_values[alpha_idx]
            best_position = alpha_position
            print(f"Iteration {t + 1}: Best fitness = {best_fitness}, Best position = {best_position}")

        return best_position, best_fitness

# Fitness fonksiyonu: Dostların düşmanlara olan toplam mesafesini en aza indirir
def fitness_function(position):
    enemies = [(10, 15), (20, 15), (18, 5)]  # Düşmanların pozisyonları
    friends = [(position[0], position[1]), (position[2], position[3]), (position[4], position[5]), (position[6], position[7]), (position[8], position[9])]  # Dostların pozisyonları
    fitness = 0
    for enemy in enemies:
        shortest_distance = float('inf')
        for friend in friends:
            distance = np.sqrt((friend[0] - enemy[0])**2 + (friend[1] - enemy[1])**2)
            if distance < shortest_distance:
                shortest_distance = distance
        fitness += shortest_distance
    return -fitness  # En küçük mesafe en iyi fitness değeri olduğu için negatif işaretliyoruz

# Grey Wolf Optimizer'ı çalıştır
optimizer = GreyWolfOptimizer(fitness_function, num_dimensions=10)
best_position, best_fitness = optimizer.optimize()
print()
print("Best position:", best_position)  # En iyi pozisyonu yazdır
print("Best fitness value:", -best_fitness)  # En iyi fitness değerini yazdır (pozitif olarak)
