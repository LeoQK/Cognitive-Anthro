import matplotlib.pyplot as plt
import powerlaw as law

nkill_list = []
f = open('nkill.txt',"r")
for line in f:
    nkill_list.append(int(line.strip('\n')))

nkill_list_largerOne = [k for k in nkill_list if k > 0]
nkill_ccdfL = law.ccdf(nkill_list_largerOne)

plt.yscale("log")
plt.xscale("log")

fit = law.Fit(nkill_list, discrete=True)
fit.power_law.plot_ccdf(color="black")
plt.scatter(nkill_ccdfL[0], nkill_ccdfL[1], facecolors='none', edgecolors='b')
plt.show()

# scale invariance
# cdf verteilungsfunktion
# log-log plot interpretation
# approximately scale invariant
# forward-backward
# ungeschickt "die verteilung folgt einer verteilung die skalen invariant ist"
# xmin in der Funktion
# kern dichte schätzung
