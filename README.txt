Optimizasyon Algoritmaları Kitaplığı
Bu depo, çeşitli optimizasyon algoritmalarının uygulamalarını içerir. Her algoritma kendi Python dosyasında uygulanır. Aşağıda her dosyanın ve içerdiği algoritmanın kısa bir açıklaması bulunmaktadır.

Dosya Açıklamaları

AntColonyOptimizer.py:
Bu dosya, Ant Colony Optimizer(ACO) algoritmasının uygulanmasını içerir. ACO, grafikler aracılığıyla iyi yollar bulmaya indirgenebilecek hesaplama problemlerini çözmeye yönelik olasılıksal bir tekniktir. Karıncaların kolonilerinden besin kaynaklarına giden yolları bulma davranışlarından ilham alıyor.

ArtificialBeeColony.py:
Bu dosya Artificial Bee Colony(ABC) algoritmasını uygular. ABC, bal arısı sürüsünün akıllı yiyecek arama davranışına dayanan bir optimizasyon algoritmasıdır. Sayısal problemleri optimize etmek için kullanılır ve yiyecek arayan bal arılarının doğal davranışlarından ilham alır.

Crossover.py:
Bu dosya genetik algoritmalarda kullanılan farklı crossover tekniklerini içerir. Crossover, yeni yavrular oluşturmak için iki ebeveynin genetik bilgilerini birleştiren bir genetik operatördür. Yaygın teknikler arasında tek noktalı, iki noktalı ve tekdüze geçiş bulunur.

EdgeRecombination.py:
Bu dosya, Traveler Salesman Problem(TSP) gibi problemler için genetik algoritmalarda kullanılan Edge Recombination operatörünü uygular. Bu operatör, yeni yavrular oluşturmak için ana çözümlerde bulunan kenarları korur.

GeneticAlgorithm.py:
Bu dosya bir Genetik Algoritmanın(GA) uygulanmasını içerir. GA, doğal seçilim sürecinden ilham alan bir meta-sezgiseldir. Aday çözümlerden oluşan bir popülasyonu en uygun çözüme doğru geliştirmek için seçme, çaprazlama ve mutasyon gibi teknikleri kullanır.

GreyWolfOptimizer.py:
Bu dosya Grey Wolf Optimizer(GWO) algoritmasını uygular. GWO, gri kurtların doğadaki sosyal hiyerarşisinden ve avlanma davranışlarından ilham alıyor. Gri kurtların liderlik hiyerarşisini ve avlanma mekanizmasını taklit ederek optimizasyon problemlerini çözmek için kullanılır.

Knapsack.py:
Bu dosya, çeşitli optimizasyon tekniklerini kullanarak Knapsack Problemine bir çözüm sunar. Knapsack Problemi, amacın bir sırt çantasına yerleştirilen öğelerin toplam değerini, kapasitesini aşmadan maksimuma çıkarmak olduğu kombinatoryal bir optimizasyon problemidir.

SimulatedAnnealing.py:
Bu dosya Simulated Annealing(SA) algoritmasının uygulamasını içerir. SA, belirli bir fonksiyonun genel optimumuna yaklaşmak için olasılıksal bir tekniktir. Kristallerinin boyutunu artırmak ve kusurlarını azaltmak için bir malzemenin ısıtılmasını ve kontrollü soğutulmasını içeren bir teknik olan metalurjideki tavlama işleminden ilham almıştır.

Başlarken
Bu algoritmalardan herhangi birini kullanmak için ilgili dosyayı projenize aktarmanız yeterlidir. Her dosya, uygulanan algoritmanın nasıl kullanılacağına ilişkin ayrıntılı belgeler ve örnekler içerir.

Gerekli bağımlılığın kurulu olduğundan emin olun:

NumPy

NumPy'yi pip kullanarak kurabilirsiniz:

pip kurulumu numpy
