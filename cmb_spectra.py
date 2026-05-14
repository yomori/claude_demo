import camb
import numpy as np
import matplotlib.pyplot as plt

# Planck 2018 cosmological parameters (TT,TE,EE+lowE+lensing, Table 2)
pars = camb.CAMBparams()
pars.set_cosmology(
    H0=67.36,
    ombh2=0.02237,
    omch2=0.1200,
    omk=0.0,
    tau=0.0544,
)
pars.InitPower.set_params(
    As=2.1e-9,
    ns=0.9649,
    r=0.0,
)
pars.set_for_lmax(3000, lens_potential_accuracy=1)

results = camb.get_results(pars)
powers = results.get_cmb_power_spectra(pars, CMB_unit="muK")

# Dl = l(l+1)/(2pi) * Cl, already in this form from CAMB's totCl output
totCl = powers["total"]
ells = np.arange(totCl.shape[0])

# Columns: TT, EE, BB, TE
TT = totCl[:, 0]
EE = totCl[:, 1]
BB = totCl[:, 2]

fig, ax = plt.subplots(figsize=(9, 6))

mask = ells >= 2
ax.plot(ells[mask], TT[mask], label=r"$D_\ell^{TT}$", color="steelblue")
ax.plot(ells[mask], EE[mask], label=r"$D_\ell^{EE}$", color="tomato")
ax.plot(ells[mask], BB[mask], label=r"$D_\ell^{BB}$", color="seagreen")

ax.set_xlabel(r"Multipole $\ell$", fontsize=13)
ax.set_ylabel(r"$D_\ell \; [\mu\mathrm{K}^2]$", fontsize=13)
ax.set_title("CMB Power Spectra — Planck 2018 Cosmology", fontsize=14)
ax.set_yscale("log")
ax.set_xlim(2, 3000)
ax.legend(fontsize=12)
ax.grid(True, which="both", ls="--", alpha=0.4)

plt.tight_layout()
plt.savefig("cmb_spectra.png", dpi=150)
plt.show()
