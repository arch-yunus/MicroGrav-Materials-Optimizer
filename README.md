# MicroGrav-Materials-Optimizer (Mikro-Yerçekimi Malzeme Optimizatörü)

[![Lisans: MIT](https://img.shields.io/badge/Lisans-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![TUA Astrohackathon 2026](https://img.shields.io/badge/Hackathon-TUA_Astrohackathon_2026-blue.svg)](https://tua.gov.tr)
[![Bilimsel Hesaplama](https://img.shields.io/badge/Bilimsel-Optimizasyon-green.svg)](https://scipy.org)
[![Sistem Sınıfı: Aethel](https://img.shields.io/badge/Sistem_Sınıfı-Aethel-gold.svg)](#)

## 🌌 Genel Bakış
**MicroGrav-Materials-Optimizer**, mikro-yerçekimi ortamlarında malzeme üretim süreçlerini otonom olarak yönetmek ve optimize etmek için tasarlanmış, **Aethel-Sınıfı** yüksek sadakatli bir hesaplama ekosistemidir. **TUA Astro Hackathon 2026** kapsamında geliştirilen bu platform, metal alaşımlarından optik kristallere kadar geniş bir yelpazede "sıfır hata" üretim hedeflerini gerçekleştirmek için kuantum sonrası optimizasyon algoritmaları ve fizik tabanlı dijital ikiz simülasyonlarını birleştirir.

### 🔬 Mikro-Yerçekimi Üretim Paradigması
Dünya yörüngesindeki üretim süreçleri, terrestrial (yer tabanlı) kısıtlamalardan arındırılmıştır:
- **Konveksiyonsuz Termal Gradyanlar:** Isı transferi sadece difüzyonla gerçekleşir, bu da atomik düzeyde kontrol sağlar.
- **Sıfır Çökelme:** Yoğunluğu farklı bileşenler (örneğin metal matrisli kompozitler) mükemmel homojenlikte karışır.
- **Makro-Kristal Büyümesi:** Yerçekimi stresi olmadan, Dünya'da mümkün olmayan boyut ve saflıkta kristal yapılar elde edilir.

---

## 🏗 Aethel-Sınıfı Sistem Mimarisi

Sistem, birbirine bağlı dört ana katmandan oluşur:

### 1. Kognitif Optimizasyon Katmanı (COL)
`src/optimizers/` altında bulunan bu katman, Bayes optimizasyonunu çok amaçlı (multi-objective) genetik algoritmalarla harmanlar. Sadece malzeme kalitesini değil, aynı zamanda uzay istasyonunun sınırlı enerji bütçesini de optimize eder.

### 2. Fiziksel Dijital İkiz Katmanı (PDTL)
`src/simulators/` modülü, yüksek çözünürlüklü termal difüzyon ve dendrit büyüme modellerini barındırır. 2D ısı dağılımı analizi ile üretim hücresindeki anlık değişimleri öngörür.

### 3. Malzeme Ontolojisi Kütüphanesi (MOL)
`data/materials.json` üzerinden yönetilen, uzayda üretim için kritik öneme sahip süper alaşım ve egzotik cam (ZBLAN) parametrelerini içeren genişletilebilir veri tabanı.

### 4. ROI ve Stratejik Analiz Modülü (RSAM)
Uzayda üretilen 1 gram malzemenin Dünya ekonomisindeki stratejik değerini ve üretim maliyetini (payload cost vs. market value) analiz eder.

---

## 📈 Matematiksel Derin Bakış

### Termal Kararlılık Denklemi
Mikro-yerçekimi ortamında katılaşma cephesindeki kararlılık, Mullins-Sekerka kriteri ile analiz edilir:
$$V < \frac{G \cdot k}{\Delta T \cdot \rho}$$
Sistemimiz, soğutma hızı ($V$) ve sıcaklık gradyanı ($G$) arasındaki bu kritik dengeyi nanosaniye ölçeğinde optimize ederek dendritik dallanmayı kontrol altında tutar.

---

## 🚀 Temel Özellikler (Gelişmiş)

- **Çok Amaçlı Bayes Optimizasyonu:** Maksimum darbe direnci ve minimum enerji tüketimi için eşzamanlı optimizasyon.
- **2D Termal Haritalama:** Katılaşma sırasında malzeme içindeki ısı dağılımının boyutsal görselleştirilmesi.
- **ZBLAN Modu:** Kristalleşmeyi önlemek için ultra hassas soğutma kontrolü.
- **Hata Isı Haritası (Risk Heatmap):** Üretim prosedüründeki riskli bölgeleri belirleyen formal analiz.

---

## 🛠 Kullanım ve Entegrasyon

### CLI ile İleri Düzey Analiz
```bash
# CMSX-4 Süper alaşımı için 2D görselleştirme ve optimizasyon
python -m src.main --material CMSX-4 --run-sim --visualize --run-opt
```

---

## 🗺 Gelecek Yol Haritası (Roadmap)

- [ ] **2026 Q3:** Otonom Robotik Kol (Cobot) entegre üretim simülasyonu.
- [ ] **2026 Q4:** Lunar (Ay) regolitinden yapısal malzeme üretimi optimizasyonu.
- [ ] **2027 Q1:** Kuantum bilgisayarlar için simüle edilmiş tavlama (simulated annealing) modülü.

---

## 📄 Gelişmiş Dokümantasyon
- [Teknik Şartname](docs/technical_spec.md)
- [Risk Analizi ve Yönetimi](docs/risk_assessment.md)
- [Proje Yönetişimi](docs/governance.md)

---
**TUA Astro Hackathon 2026 - Uzayda Geleceği İnşa Ediyoruz.**
