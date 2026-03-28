# Risk Değerlendirmesi ve Hafifletme (Risk Assessment)

## 1. Teknik Riskler
| Risk | Olasılık | Etki | Hafifletme Stratejisi |
| :--- | :--- | :--- | :--- |
| Sensör Veri Sapması | Yüksek | Kritik | Bayesian filtreleme ve otonom kalibrasyon döngüleri. |
| Termal Kararsızlık | Orta | Yüksek | Real-time PID kontrolü ve öngörülü simülasyon. |
| Enerji Kısıtı | Yüksek | Orta | Düşük güç tüketimli optimizasyon modları. |

## 2. Operasyonel Riskler
- **Uzay Radyasyonu:** Donanım seviyesinde hata toleranslı sistemlerin yazılımsal olarak desteklenmesi.
- **İletişim Gecikmesi (Latency):** Uzay istasyonunda yerel (edge) işleme kapasitesinin artırılması.

## 3. Risk Isı Haritası (Risk Heatmap)
Sistemimiz, her üretim döngüsü öncesinde bir "Üretim Güven Puanı" (Manufacturing Confidence Score) hesaplar. 70/100 altındaki skorlarda süreç otomatik olarak durdurulur.
