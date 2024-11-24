import numpy as np
import matplotlib.pyplot as plot

def F_co(theta,phi):

    qe = 3.2
    qh = 2.16

    var = (np.cos(theta)**qe) * (np.sin(phi)**2)
    var1 = (np.cos(theta)**qh) * (np.cos(phi)**2)
    F_co = var + var1

    return F_co

def F_cr(theta,phi):

    qe = 3.2
    qh = 2.16

    var = (np.cos(theta)**qe) * np.cos(phi) * np.sin(phi)
    var1 = (np.cos(theta)**qh) * np.cos(phi) * np.sin(phi)
    F_cr = var - var1

    return F_cr


theta_range = np.arange(0,np.pi/2,1/100)
phi_range = [0, np.pi/2, np.pi/4]


Fco_dB = np.zeros(len(theta_range))
Fcr_dB = np.zeros(len(theta_range))
Fco_0_dB = np.zeros(len(phi_range))
F_normalized = np.zeros(len(theta_range))
F_normalized1 = np.zeros(len(theta_range))

for phi in phi_range:
    Fco_0_dB = 20 * np.log10(abs(F_co(0, phi)))
    for i in range(0 , len(theta_range)):
        theta = theta_range[i]
        Fco_dB[i] = 20 * np.log10(F_co(theta, phi))
        Fcr_dB[i] = 20 * np.log10(abs(F_cr(theta, phi)))
        F_normalized[i] = Fco_dB[i] - Fco_0_dB
        F_normalized1[i] = Fcr_dB[i] - Fco_0_dB

    ax1 = plot.subplot(211, projection='polar')
    ax1.plot(theta_range, F_normalized, label=f'$\\phi$ = {phi}')
    ax1.set_theta_zero_location('N')
    ax1.set_theta_direction(-1)
    ax2 = plot.subplot(212, projection='polar')
    ax2.plot(theta_range, F_normalized1, label=f'$\\phi$ = {phi}')
    ax2.set_theta_zero_location('N')
    ax2.set_theta_direction(-1)

plot.subplots_adjust(hspace = 0.3)
ax1.legend(loc='center left', bbox_to_anchor=(1.4, -0.1))
ax1.set_title(f'Normalized form of Fco($\\theta$,$\\phi$)/|Fco(0,$\\phi$)| in (dB)')
ax2.set_title(f'Normalized form of |Fcr($\\theta$,$\\phi$)|/|Fco(0,$\\phi$)| in (dB)')

# Show plot
plot.show()




# r_range = [0.7* Lambda, 0.8 * Lambda, 0.9 * Lambda, 2 * Lambda, 3 * Lambda, 4 * Lambda, 5 * Lambda, 10 * Lambda, 20 * Lambda, 50 * Lambda]
# for r in r_range:
#     for i in range(0 , len(theta_range)):
#         theta = theta_range[i]
#         E_theta_r_dB[i] = Etheta(r,theta,phi[i])
#     E_theta_norm = Etheta(r,np.pi/2,phi)*np.ones(len(theta_range))
#
#     E_normalized_dB = E_theta_r_dB - E_theta_norm
#     theta_full = np.concatenate((-np.flip(theta_range), theta_range))
#     Etheta_full = np.concatenate((np.flip(E_normalized_dB), E_normalized_dB))
#     ax = plot.subplot(111, projection='polar')
#     ax.plot(theta_full, Etheta_full, label=f'r = {r/h}h')
#     ax.set_theta_zero_location('N')
#     ax.set_theta_direction(-1)
#
#
# ax.legend(loc='center left', bbox_to_anchor=(1.1, 0.5))
# ax.set_title(f'Normalized Electric Field (dB) for h = {h/Lambda}$\\lambda$ versus $\\theta$')
#
# # Show plot
# plot.show()