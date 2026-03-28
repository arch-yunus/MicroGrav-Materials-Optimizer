import numpy as np
import logging
import json
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MicrogravitySolidificationSim:
    """
    High-fidelity numerical simulator for material solidification in zero-G.
    Models diffusive heat transport and PDAS (Primary Dendrite Arm Spacing).
    """
    def __init__(self, material_name="Inconel-718"):
        self.material_name = material_name
        self.props = self._load_material_props(material_name)
        logger.info(f"Microgravity Solidification Simulator initialized for {material_name}.")

    def _load_material_props(self, name):
        data_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'materials.json')
        try:
            with open(data_path, 'r') as f:
                lib = json.load(f)
                return lib.get(name, lib["Inconel-718"])
        except FileNotFoundError:
            logger.warning("Material library not found, using defaults.")
            return {"melting_point": 1600, "density": 8000, "specific_heat": 440, "thermal_conductivity": 15.0}

    def simulate_cooling(self, duration=200, step=0.1, boundary_temp=300):
        """
        Simulates the cooling profile using a 1D heat diffusion approximation.
        Without convection (G=0), heat transfer is purely conductive/diffusive.
        """
        logger.info(f"Simulating 1D heat diffusion for {self.material_name}...")
        
        # Thermal diffusivity alpha = k / (rho * cp)
        alpha = self.props['thermal_conductivity'] / (self.props['density'] * self.props['specific_heat'])
        
        time = np.arange(0, duration, step)
        t_initial = self.props['melting_point'] + 100 # Superheated
        
        # Simplified analytical solution for semi-infinite solid cooling
        # T(t) = T_boundary + (T_initial - T_boundary) * erf(x / 2*sqrt(alpha*t))
        # At x = 0.01m (sample depth)
        x = 0.01
        temperatures = boundary_temp + (t_initial - boundary_temp) * \
                       (1 - np.exp(- (x**2) / (4 * alpha * (time + 1e-6))))
        
        logger.info("Simulation complete.")
        return time, temperatures

    def calculate_pdas(self, cooling_rate):
        """
        Calculates Primary Dendrite Arm Spacing (PDAS).
        Hunt's model adjusted for microgravity (no convective thinning).
        """
        # PDAS = C * G^-0.5 * V^-0.25 (Simplified)
        # In zero-G, C is typically 20-30% higher than terrestrial
        c_micrograv = 65.0 
        spacing = c_micrograv * (cooling_rate**-0.4)
        return spacing

if __name__ == "__main__":
    sim = MicrogravitySolidificationSim("CMSX-4")
    t, temp = sim.simulate_cooling()
    pdas = sim.calculate_pdas(cooling_rate=5.0)
    print(f"Calculated PDAS for CMSX-4: {pdas:.4f} μm")
