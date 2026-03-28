# Mikro-Yerçekimi Malzeme Optimizasyonu: Teknik Şartname

## 1. Termal Katılaşma Modeli
Yerçekiminin yokluğunda ($g \approx 0$), kaldırma kuvvetine bağlı konveksiyon ortadan kalkar. Isı transferi temel olarak iletim (kondüksiyon) ile kontrol edilir:

$$\rho c_p \frac{\partial T}{\partial t} = k \nabla^2 T + L \frac{\partial \phi}{\partial t}$$

Burada:
- $\rho$: Yoğunluk
- $c_p$: Özgül ısı
- $k$: Termal iletkenlik
- $L$: Gizli füzyon ısısı
- $\phi$: Faz fraksiyonu

### 1.1 Analitik Yaklaşım
Sabit sınır sıcaklığı $T_b$ olan yarı sonsuz bir katı için, $x$ derinliğindeki sıcaklık profili şu şekildedir:
$$T(x,t) = T_b + (T_i - T_b) \cdot erf\left(\frac{x}{2\sqrt{\alpha t}}\right)$$
Burada $\alpha = \frac{k}{\rho c_p}$ termal difüzivitedir.

## 2. Dendrit Kol Aralığı (DAS)
Mikro-yerçekiminde birincil dendrit kol aralığı ($\lambda_1$), dendrit uçlarındaki konvektif incelme olmaması nedeniyle karasal değerlerden önemli ölçüde farklıdır.

$$\lambda_1 = C \cdot G^{-1/2} \cdot V^{-1/4}$$

Motorumuzda, ISS deneylerinde (örneğin METCOMP, MICAST) gözlemlenen daha büyük ve daha homojen yapıları yansıtmak için ayarlanmış bir sabit $C_{space} \approx 1.3 \cdot C_{earth}$ kullanıyoruz.

## 3. Optimizasyon Stratejisi
Bayes Optimizatörü, yüksek boyutlu parametre uzayını (Soğutma Hızı, Gradyan, Basınç), yapısal bütünlük ve mikroyapısal tekdüzelik tarafından tanımlanan bir kalite metriğine eşlemek için bir Gauss Süreci (GP) vekil modeli kullanır.
