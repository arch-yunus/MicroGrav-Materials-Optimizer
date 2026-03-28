import argparse
import sys
import matplotlib.pyplot as plt
import os
from src.optimizers.bayesian import ProcessOptimizer
from src.simulators.solidification import MicrogravitySolidificationSim

def main():
    parser = argparse.ArgumentParser(description="MicroGrav Malzeme Optimizatörü - CLI")
    parser.add_argument("--material", type=str, default="Inconel-718", choices=["Inconel-718", "CMSX-4", "ZBLAN"], help="Optimize edilecek malzeme")
    parser.add_argument("--run-opt", action="store_true", help="Optimizasyon döngüsünü çalıştır")
    parser.add_argument("--run-sim", action="store_true", help="Katılaşma simülasyonunu çalıştır")
    parser.add_argument("--visualize", action="store_true", help="Simülasyon sonuçları için grafik oluştur")
    parser.add_argument("--test", action="store_true", help="Motor bütünlüğünü doğrula")

    args = parser.parse_args()

    if args.test:
        print("--- MicroGrav Motor Bütünlük Testi ---")
        try:
            opt = ProcessOptimizer(material=args.material)
            sim = MicrogravitySolidificationSim(material_name=args.material)
            print("Durum: Tüm bileşenler başarıyla başlatıldı.")
        except Exception as e:
            print(f"Durum: Başlatma sırasında hata - {e}")
            sys.exit(1)
        return

    if args.run_opt:
        opt = ProcessOptimizer(material=args.material)
        results = opt.run()
        print(f"\n{args.material} için Optimal Üretim Parametreleri:")
        for k, v in results.items():
            print(f"  {k}: {v:.4f}")

    if args.run_sim:
        sim = MicrogravitySolidificationSim(material_name=args.material)
        time, temp = sim.simulate_cooling()
        print(f"\n{args.material} için simülasyon tamamlandı.")
        print(f"Başlangıç Sıcaklığı: {temp[0]:.2f} K")
        print(f"Final Sıcaklığı: {temp[-1]:.2f} K")
        
        pdas = sim.calculate_pdas(cooling_rate=10.0)
        print(f"Öngörülen PDAS (Sıfır-G): {pdas:.2f} um")

        if args.visualize:
            plt.figure(figsize=(10, 6))
            plt.plot(time, temp, label=f'{args.material} Soğutma Profili', color='cyan')
            plt.axhline(y=300, color='r', linestyle='--', label='Sınır Sıcaklığı')
            plt.title(f"Termal Katılaşma Profili - {args.material} (Mikro-Yerçekimi)")
            plt.xlabel("Zaman (s)")
            plt.ylabel("Sıcaklık (K)")
            plt.grid(True, alpha=0.3)
            plt.legend()
            
            output_path = os.path.join('simulations', f'{args.material}_sogutma.png')
            plt.savefig(output_path)
            print(f"Görselleştirme kaydedildi: {output_path}")

    if not any([args.run_opt, args.run_sim, args.test]):
        parser.print_help()

if __name__ == "__main__":
    main()
