Optimizasyon Algoritmaları Kitaplığı
Bu depo, çeşitli optimizasyon algoritmalarının uygulamalarını içerir. Her algoritma kendi Python dosyasında uygulanır. Aşağıda her dosyanın ve içerdiği algoritmanın kısa bir açıklaması bulunmaktadır.

Dosya Açıklamaları

AntColonyOptimizer.py
Bu dosya, Karınca Kolonisi Optimizasyonu (ACO) algoritmasının uygulanmasını içerir. ACO, grafikler aracılığıyla iyi yollar bulmaya indirgenebilecek hesaplama problemlerini çözmeye yönelik olasılıksal bir tekniktir. Karıncaların kolonilerinden besin kaynaklarına giden yolları bulma davranışlarından ilham alıyor.

YapayBeeColony.py
Bu dosya Yapay Arı Kolonisi (ABC) algoritmasını uygular. ABC, bal arısı sürüsünün akıllı yiyecek arama davranışına dayanan bir optimizasyon algoritmasıdır. Sayısal problemleri optimize etmek için kullanılır ve yiyecek arayan bal arılarının doğal davranışlarından ilham alır.

Crossover.py
Bu dosya genetik algoritmalarda kullanılan farklı çaprazlama tekniklerini içerir. Çaprazlama, yeni yavrular oluşturmak için iki ebeveynin genetik bilgilerini birleştiren bir genetik operatördür. Yaygın teknikler arasında tek noktalı, iki noktalı ve tekdüze geçiş bulunur.

EdgeRecombination.py
Bu dosya, Gezgin Satıcı Problemi (TSP) gibi problemler için genetik algoritmalarda kullanılan Kenar Rekombinasyon operatörünü uygular. Bu operatör, yeni yavrular oluşturmak için ana çözümlerde bulunan kenarları korur.

GenetikAlgoritma.py
Bu dosya bir Genetik Algoritmanın (GA) uygulanmasını içerir. GA, doğal seçilim sürecinden ilham alan bir meta-sezgiseldir. Aday çözümlerden oluşan bir popülasyonu en uygun çözüme doğru geliştirmek için seçme, çaprazlama ve mutasyon gibi teknikleri kullanır.

GreyWolfOptimizer.py
Bu dosya Gri Kurt Doktoru (GWO) algoritmasını uygular. GWO, gri kurtların doğadaki sosyal hiyerarşisinden ve avlanma davranışlarından ilham alıyor. Gri kurtların liderlik hiyerarşisini ve avlanma mekanizmasını taklit ederek optimizasyon problemlerini çözmek için kullanılır.

Sırt çantası.py
Bu dosya, çeşitli optimizasyon tekniklerini kullanarak Sırt Çantası Problemine bir çözüm sunar. Sırt Çantası Problemi, amacın bir sırt çantasına yerleştirilen öğelerin toplam değerini, kapasitesini aşmadan maksimuma çıkarmak olduğu kombinatoryal bir optimizasyon problemidir.

SimulatedAnnealing.py
Bu dosya Simüle Tavlama (SA) algoritmasının uygulamasını içerir. SA, belirli bir fonksiyonun genel optimumuna yaklaşmak için olasılıksal bir tekniktir. Kristallerinin boyutunu artırmak ve kusurlarını azaltmak için bir malzemenin ısıtılmasını ve kontrollü soğutulmasını içeren bir teknik olan metalurjideki tavlama işleminden ilham almıştır.

Başlarken
Bu algoritmalardan herhangi birini kullanmak için ilgili dosyayı projenize aktarmanız yeterlidir. Her dosya, uygulanan algoritmanın nasıl kullanılacağına ilişkin ayrıntılı belgeler ve örnekler içerir.

Gerekli bağımlılığın kurulu olduğundan emin olun:

NumPY

NumPy'yi pip kullanarak kurabilirsiniz:

pip kurulumu numpy
