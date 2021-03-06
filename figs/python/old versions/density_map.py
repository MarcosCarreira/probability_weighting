import numpy as np
import time
import matplotlib.pyplot as plt
import scipy.stats as stat

start = time.time()


xx = np.linspace(0.0, 1.0, num=1000)
x = np.linspace(-10, 10, num=5000)
# Gaussians location and scale parameters
s1 = 1
#s2 = np.sqrt(3)
s2 = 2
l1 = 0
l2 = 0
# CDFs
DO = stat.norm.pdf(x, l1, s1)
DM = stat.norm.pdf(x, l2, s2)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(9, 3.5))
fig.tight_layout(pad=3)

#CDF plot
#axes[0].axvline(x=-1, LineStyle='--')
#axes[0].axvline(x=0, LineStyle='--')
#axes[0].axvline(x=1, LineStyle='--')
#axes[0].axhline(y=0.5, LineStyle='--')
axes[0].set_xlim((-4.5, 4.5))
#axes[0].set_ylim((0,.5))
axes[0].plot(x, DO, 'r', lineWidth='2', label=r'$p(x)$')
axes[0].plot(x, DM, 'b', lineWidth='2', label=r'$w(x)$')

#plot arrows
xs=[-2.5,-2,-1.5,-1,-.5,0]
for i in xs:
    axes[0].arrow(i,stat.norm.pdf(i, l1, s1), 0, stat.norm.pdf(i, l2, s2) - stat.norm.pdf(i, l1, s1), head_width=0.16, head_length=0.02, length_includes_head=True, fc='k', ec='k', zorder=10)

#nx = len(x)
#steps = 2
#xs = np.linspace(-4, 4, steps, endpoint=True)
#for i in range(0, steps):
#    if np.abs(xs[i]) > 0.45:
#        axes[0].arrow(xs[i], stat.norm.cdf(xs[i], l1, s1), 0, stat.norm.cdf(xs[i], l2, s2) - stat.norm.cdf(xs[i], l1, s1), head_width=0.15, head_length=0.045, length_includes_head=True, fc='k', ec='k', zorder=10)

axes[0].set_xlabel(r'x')
axes[0].set_ylabel(r'PDFs')
axes[0].set_xticks(np.arange(-4, 5, step=2))
axes[0].set_yticks(np.arange(0, .5, step=0.1))
axes[0].legend(loc='upper left', fontsize='x-small')

#w(p) plot
#axes[1].axvline(x=0.5, LineStyle='--')
axes[1].set_xlim((0,1.05*stat.norm.pdf(0, l1, s1)))
axes[1].set_ylim((0,1.05*stat.norm.pdf(0, l1, s1)))
axes[1].plot(DO, DO, 'r', lineWidth='2', label=r'$p$')
axes[1].plot(DO, DM, 'b', lineWidth='2', label=r'$w$')

# plot arrows
#nx = len(x)
#steps = 9
#xs = np.linspace(0.1, 0.9, steps, endpoint=True)
#for i in range(0, steps):
#    if np.abs(xs[i] - 0.5) > 0.05:
#        axes[1].arrow(xs[i], xs[i], 0, stat.norm.cdf(stat.norm.ppf(xs[i], l1, s1), l2, s2) - stat.norm.cdf(stat.norm.ppf(xs[i], l1, s1), l1, s1), head_width=0.018, head_length=0.045, length_includes_head=True, fc='k', ec='k', zorder=10)

for i in xs:
    axes[1].arrow(stat.norm.pdf(i, l1, s1),stat.norm.pdf(i, l1, s1), 0, stat.norm.pdf(i, l2, s2) - stat.norm.pdf(i, l1, s1), head_width=0.008, head_length=0.02, length_includes_head=True, fc='k', ec='k', zorder=10)

axes[1].set_xlabel(r'PDF $p$')
axes[1].set_ylabel(r'PDFs')
axes[1].set_xticks(np.arange(0, .5, step=0.1))
axes[1].set_yticks(np.arange(0, .5, step=0.1))
axes[1].legend(loc='upper left', fontsize='x-small')

plt.savefig("./../density_map.pdf", bbox_inches='tight')
plt.show()
plt.clf()

end = time.time()
print(end - start)