import random  # Rastgele sayılar üretmek için gerekli modül

# Değer ve ağırlıklar içeren bir sınıf
class ObjFunc:
    def __init__(self):
        # Ağırlıklar
        self.w = [7, 5, 10, 15, 5, 3, 8, 4, 9, 12]
        # Değerler
        self.v = [10, 15, 5, 8, 20, 10, 7, 17, 5, 3]

    # Verilen çözümdeki toplam değeri ve ağırlığı hesaplar
    def fitness(self, x):
        f = 0  # Başlangıçta toplam değer sıfır
        w_total = 0  # Başlangıçta toplam ağırlık sıfır
        for i in range(len(x)):  # Çözüm boyunca iterasyon yapar
            f += x[i] * self.v[i]  # Değeri toplar
            w_total += x[i] * self.w[i]  # Ağırlığı toplar
            # Ağırlık sınırını aştığında ceza puanı verir
            if w_total > weight_limit:
                f = 1000  # Ceza değeri
                return f, w_total  # Toplam değer ve ağırlık döner
        return f, w_total  # Eğer sınırı aşmazsa, toplam değer ve ağırlık döner

# Rastgele bir çözüm üretir
def generate_random_solution():
    return [random.randint(0, 1) for _ in range(len(obj_func.v))]

# İki ebeveyn arasındaki crossover işlemi
def crossover(parent1, parent2):
    # Rastgele bir crossover noktası seçer
    crossover_point = random.randint(1, len(parent1) - 1)
    # İlk çocuk, ebeveynlerden birinin başı ve diğerinin sonu ile oluşturulur
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    # İkinci çocuk, ebeveynlerin tam tersi ile oluşturulur
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    
    # Çocukların ağırlıklarını hesaplar
    child1_weight = sum(child1[i] * obj_func.w[i] for i in range(len(child1)))
    child2_weight = sum(child2[i] * obj_func.w[i] for i in range(len(child2)))
    
    # Eğer çocukların ağırlıkları sınırı aşarsa, düzeltici bir işlem uygular
    if child1_weight > weight_limit:
        for i in range(len(child1)):
            if child1[i] == 1 and child1_weight > weight_limit:
                child1[i] = 0  # Çocukların ağırlığını azaltmak için bileşeni kaldırır
                child1_weight -= obj_func.w[i]
    
    if child2_weight > weight_limit:
        for i in range(len(child2)):
            if child2[i] == 1 and child2_weight > weight_limit:
                child2[i] = 0  # Aynı şekilde, sınırı aşan bileşeni kaldırır
                child2_weight -= obj_func.w[i]
    
    return child1, child2  # Düzeltmeden sonra çocukları döner

# ObjFunc sınıfını başlatır
obj_func = ObjFunc()

# Ağırlık sınırı belirlenir
weight_limit = 40

# Başlangıçta 10 rastgele çözüm üretir
solutions = [generate_random_solution() for _ in range(10)]

# Çözüm listesi boyunca adım adım ilerler
for i in range(0, len(solutions), 2):
    
    # İki ebeveyn seçer
    parent1 = solutions[i]
    parent2 = solutions[i+1]
    
    # Ebeveynlerden crossover ile iki çocuk oluşturur
    child1, child2 = crossover(parent1, parent2)
    
    # Çocukların fitness'ını ve ağırlığını hesaplar
    child1_fitness, child1_weight = obj_func.fitness(child1)
    child2_fitness, child2_weight = obj_func.fitness(child2)
    
    # Ebeveyn ve çocukların detaylarını yazdırır
    print("Parent 1:", parent1, "Weight:", obj_func.fitness(parent1)[1], "Fitness:", obj_func.fitness(parent1)[0])
    print("Parent 2:", parent2, "Weight:", obj_func.fitness(parent2)[1], "Fitness:", obj_func.fitness(parent2)[0])
    print("Child 1:", child1, "Weight:", child1_weight, "Fitness:", child1_fitness)
    print("Child 2:", child2, "Weight:", child2_weight, "Fitness:", child2_fitness)
    print()
