import random

class AntColony:
    def __init__(self, distances, cities, n_ants, n_iterations, decay, alpha=1, beta=2):
        # Başlangıç parametreleri
        self.distances = distances  # Şehirler arasındaki mesafeleri temsil eden matris
        self.cities = cities  # Şehirlerin isimleri
        self.n_ants = n_ants  # Karınca sayısı
        self.n_iterations = n_iterations  # Iterasyon sayısı
        self.decay = decay  # Feromon azalması oranı
        self.alpha = alpha  # Feromonun etkisi
        self.beta = beta  # Mesafenin etkisi
        self.n_cities = len(distances)  # Şehir sayısı
        # Başlangıç feromon değeri: feromonlar başlangıçta düşük bir değerde başlar
        self.pheromone = [[1 / (self.n_cities * self.n_cities) for _ in range(self.n_cities)] for _ in range(self.n_cities)]

    def run(self):
        # Ana çalışma fonksiyonu
        shortest_path = None  # En kısa yol
        shortest_distance = float('inf')  # En kısa mesafe
        for _ in range(self.n_iterations):
            paths = self.generate_paths()  # Yeni yollar oluştur
            self.update_pheromone(paths)  # Feromonları güncelle
            shortest_path, shortest_distance = self.update_shortest(paths, shortest_path, shortest_distance)  # En kısa yolu güncelle
            self.pheromone = self.decay_pheromone(self.pheromone)  # Feromonları azalt
        return shortest_path, shortest_distance  # En kısa yol ve mesafeyi döndür

    def generate_paths(self):
        # Tüm karıncalar için yollar oluştur
        paths = []
        for _ in range(self.n_ants):
            path = self.generate_path()  # Bir yol oluştur
            paths.append(path)
        return paths

    def generate_path(self):
        # Bir karınca için yol oluştur
        path = []
        visited = set()  # Ziyaret edilen şehirler kümesi
        start = random.choice(self.cities)  # Rastgele başlangıç şehri
        current_city = start
        path.append(current_city)
        visited.add(current_city)
        while len(visited) < self.n_cities:
            next_city = self.select_next_city(current_city, visited)  # Sonraki şehri seç
            path.append(next_city)
            visited.add(next_city)
            current_city = next_city
        path.append(start)  # Turu tamamla
        return path

    def select_next_city(self, current_city, visited):
        # Bir sonraki şehri olasılıklarına göre seç
        probabilities = self.calculate_probabilities(current_city, visited)  # Olasılıkları hesapla
        next_city = random.choices(self.cities, weights=probabilities)[0]  # Bir sonraki şehri seç
        return next_city

    def calculate_probabilities(self, current_city, visited):
        # Bir sonraki şehir için olasılıkları hesapla
        probabilities = []
        pheromone_row = self.pheromone[self.cities.index(current_city)]
        for city in self.cities:
            if city in visited:
                probabilities.append(0)  # Zaten ziyaret edilen şehirlerin olasılığı 0
            else:
                distance = self.distances[self.cities.index(current_city)][self.cities.index(city)]
                pheromone = pheromone_row[self.cities.index(city)]
                heuristic = 1 / distance  # Heuristik bilgi (ters mesafe)
                probability = (pheromone ** self.alpha) * (heuristic ** self.beta)  # Olasılığı hesapla
                probabilities.append(probability)
        total = sum(probabilities)
        probabilities = [p / total for p in probabilities]  # Olasılıkları normalize et
        return probabilities

    def update_pheromone(self, paths):
        # Feromonları güncelle
        for i in range(self.n_cities):
            for j in range(self.n_cities):
                if i != j:
                    self.pheromone[i][j] *= (1 - self.decay)  # Feromon azalması
                    for path in paths:
                        city_indices = [self.cities.index(city) for city in path]
                        if (i, j) in zip(city_indices[:-1], city_indices[1:]) or (j, i) in zip(city_indices[:-1], city_indices[1:]):
                            self.pheromone[i][j] += 1 / len(path)  # Feromon güncellemesi

    def decay_pheromone(self, pheromone):
        # Feromonları azalt
        return [[max(pheromone[i][j] * self.decay, 0.001) for j in range(self.n_cities)] for i in range(self.n_cities)]  # Feromonu minimum değere düşür

    def update_shortest(self, paths, shortest_path, shortest_distance):
        # En kısa yolu ve mesafeyi güncelle
        for path in paths:
            distance = self.calculate_distance(path)  # Yolu hesapla
            if distance < shortest_distance:
                shortest_path = path  # En kısa yolu güncelle
                shortest_distance = distance
        return shortest_path, shortest_distance

    def calculate_distance(self, path):
        # Bir yolun toplam mesafesini hesapla
        distance = 0
        for i in range(len(path) - 1):
            distance += self.distances[self.cities.index(path[i])][self.cities.index(path[i + 1])]  # Toplam mesafeyi hesapla
        return distance


# Örnek kullanım:
if __name__ == "__main__":
    # Şehirler arasındaki mesafeler (simetrik matris)
    distances = [
        [0, 5, 8, 3, 7, 1],
        [5, 0, 2, 10, 8, 4],
        [8, 2, 0, 3, 10, 5],
        [3, 10, 3, 0, 2, 7],
        [7, 8, 10, 2, 0, 6],
        [1, 4, 5, 7, 6, 0]
    ]
    
    cities = ['A', 'B', 'C', 'D', 'E', 'F']
    
    ant_colony = AntColony(distances, cities, n_ants=10, n_iterations=100, decay=0.1)
    shortest_path, shortest_distance = ant_colony.run()
    print("Shortest Path:", shortest_path)
    print("Shortest Distance:", shortest_distance)
