import argparse
import sys
import matplotlib.pyplot as plt
import os
from src.optimizers.bayesian import ProcessOptimizer
from src.simulators.solidification import MicrogravitySolidificationSim

def main():
    parser = argparse.ArgumentParser(description="MicroGrav Materials Optimizer - CLI")
    parser.add_argument("--material", type=str, default="Inconel-718", choices=["Inconel-718", "CMSX-4", "ZBLAN"], help="Material to optimize")
    parser.add_argument("--run-opt", action="store_true", help="Run optimization cycle")
    parser.add_argument("--run-sim", action="store_true", help="Run solidification simulation")
    parser.add_argument("--visualize", action="store_true", help="Generate plots for simulation results")
    parser.add_argument("--test", action="store_true", help="Verify engine integrity")

    args = parser.parse_args()

    if args.test:
        print("--- MicroGrav Engine Integrity Test ---")
        try:
            opt = ProcessOptimizer(material=args.material)
            sim = MicrogravitySolidificationSim(material_name=args.material)
            print("Status: All components initialized successfully.")
        except Exception as e:
            print(f"Status: Error during initialization - {e}")
            sys.exit(1)
        return

    if args.run_opt:
        opt = ProcessOptimizer(material=args.material)
        results = opt.run()
        print(f"\nOptimal Manufacturing Parameters for {args.material}:")
        for k, v in results.items():
            print(f"  {k}: {v:.4f}")

    if args.run_sim:
        sim = MicrogravitySolidificationSim(material_name=args.material)
        time, temp = sim.simulate_cooling()
        print(f"\nSimulation complete for {args.material}.")
        print(f"Initial Temp: {temp[0]:.2f} K")
        print(f"Final Temp: {temp[-1]:.2f} K")
        
        pdas = sim.calculate_pdas(cooling_rate=10.0)
        print(f"Predicted PDAS (Zero-G): {pdas:.2f} μm")

        if args.visualize:
            plt.figure(figsize=(10, 6))
            plt.plot(time, temp, label=f'{args.material} Cooling Profile', color='cyan')
            plt.axhline(y=300, color='r', linestyle='--', label='Boundary Temp')
            plt.title(f"Thermal Solidification Profile - {args.material} (Microgravity)")
            plt.xlabel("Time (s)")
            plt.ylabel("Temperature (K)")
            plt.grid(True, alpha=0.3)
            plt.legend()
            
            output_path = os.path.join('simulations', f'{args.material}_cooling.png')
            plt.savefig(output_path)
            print(f"Visualization saved to {output_path}")

    if not any([args.run_opt, args.run_sim, args.test]):
        parser.print_help()

if __name__ == "__main__":
    main()
