from Image import open
import matplotlib as mpl
mpl.use('Agg')
import pylab as plt

mpl.rc('text', usetex=True)
plt.figure()
y=[1,2,3,4,5,4,3,2,1,1,1,1,1,1,1,1]
col_labels=['col1','col2','col3']
row_labels=['row1','row2','row3']
table_vals=[11,12,13,21,22,23,31,32,33]
table = r'''\begin{tabular}{ c | c | c | c } & col1 & col2 & col3 \\\hline row1 & 11 & 12 & 13 \\\hline row2 & 21 & 22 & 23 \\\hline row3 & 31 & 32 & 33 \end{tabular}'''
plt.text(9, 3.4, table, size=12)
plt.plot(y)
plt.savefig("./table_demo.ps") 

# convert ps image to png
open("./table_demo.ps").save("./table_demo.png")