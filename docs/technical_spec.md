# Microgravity Materials Optimization: Technical Specification

## 1. Thermal Solidification Model
In the absence of gravity ($g \approx 0$), buoyancy-driven convection is eliminated. The heat transfer is governed primarily by conduction:

$$\rho c_p \frac{\partial T}{\partial t} = k \nabla^2 T + L \frac{\partial \phi}{\partial t}$$

Where:
- $\rho$: Density
- $c_p$: Specific heat
- $k$: Thermal conductivity
- $L$: Latent heat of fusion
- $\phi$: Phase fraction

### 1.1 Analytical Approximation
For a semi-infinite solid with constant boundary temperature $T_b$, the temperature profile at depth $x$ is:
$$T(x,t) = T_b + (T_i - T_b) \cdot erf\left(\frac{x}{2\sqrt{\alpha t}}\right)$$
Where $\alpha = \frac{k}{\rho c_p}$ is the thermal diffusivity.

## 2. Dendrite Arm Spacing (DAS)
The primary dendrite arm spacing ($\lambda_1$) in microgravity is significantly different from terrestrial values due to the lack of convective thinning at the dendrite tips.

$$\lambda_1 = C \cdot G^{-1/2} \cdot V^{-1/4}$$

In our engine, we use an adjusted constant $C_{space} \approx 1.3 \cdot C_{earth}$ to reflect the larger, more uniform structures observed in ISS experiments (e.g., METCOMP, MICAST).

## 3. Optimization Strategy
The Bayesian Optimizer uses a Gaussian Process (GP) surrogate model to map the high-dimensional parameter space (Cooling Rate, Gradient, Pressure) to a quality metric defined by structural integrity and microstructural uniformity.
