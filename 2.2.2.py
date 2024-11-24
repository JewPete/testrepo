import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import scipy.constants as sc

def E_phi(theta,phi):
    eta = (sc.mu_0 / sc.epsilon_0) ** 0.5
    Cm = 1
    Ce = eta
    Lambda = 1
    k = 2 * np.pi / Lambda

    E_phi = 1j * k * eta * Ce * np.cos(phi)
    E_phi = E_phi + (1j * k * Cm * np.cos(phi) * np.cos(theta))
    E_phi = E_phi * np.exp(-1j * k) / (4 * np.pi)

    return (abs(E_phi))

theta_range = np.arange(0, 6.28, 1/100)
# phi_range = np.arange(0, 6.28 ,1/100)
phi_range = np.pi/2*np.ones(100)
theta_mesh, phi_mesh = np.meshgrid(theta_range, phi_range)


E_phi_max = E_phi(0,0)

def E_phi_dB(theta,phi):
    return 20 * np.log10(E_phi(theta,phi) / E_phi_max)


E_phi_dB_values = E_phi_dB(theta_mesh,phi_mesh)

fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
ax = fig.add_subplot(111, projection='polar')
ax.plot(theta_mesh[0], E_phi_dB_values[0])
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)

ax.set_title('Electric Field Radiation Intensity of Huygen"s Source')

plt.show()

# for i in range(0,len(theta_range)):
#     theta = theta_range[i]
#     for i in range(0,len(phi_range)):
#         phi = phi_range[i]
#         y = np.sin(theta)*np.cos(phi)
#         z = np.sin(theta)*np.sin(phi)
#         F_theta_dB[i] = 20 * np.log10(E_theta(theta,phi)/E_theta_max)
#         #ax = plot.subplot(111, projection='polar')
#         ax.plot(phi_range, F_theta_dB, label=f'$\\phi$ = {phi}')
#         ax.set_theta_zero_location('N')
#         ax.set_theta_direction(-1)
#
# ax.legend(loc='center left', bbox_to_anchor=(1.1, 0.5))
#
# surf = ax.plot_surface(F_theta_dB, y, Z, cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)
#
#
# # Customize the z axis.
# ax.set_zlim(-1.01, 1.01)
# ax.zaxis.set_major_locator(LinearLocator(10))
# # A StrMethodFormatter is used automatically
# ax.zaxis.set_major_formatter('{x:.02f}')
#
# # Add a color bar which maps values to colors.
# fig.colorbar(surf, shrink=0.5, aspect=5)
#
# plt.show()