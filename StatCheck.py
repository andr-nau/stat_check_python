# StatCheck
# Just test Python code to play with libraries

import random
import statistics
import numpy
import matplotlib


b=[]

# Get 10'000 random numbers 0-10 
f = open("myfile.txt", "w")
for i in range(0,10000):
    a=random.randint(1,10)
    b.append(int(a))
    f.write(str(a)+" ")

# Check stats
mn = statistics.mean(b)
mnn = numpy.mean(b)
med = statistics.median(b)
medn = numpy.median(b)
qtn = numpy.quantile(b,0.5)

text = "Mean:\n"+"stat:"+str(mn)+"\nnumpy:"+str(mnn)+"\nMediane:\n"+"stat:"+str(med)+"\nnumpy:"+str(medn)+"\nQuantile:"+"\nnumpy:"+str(qtn)
print(text)
f.write(text)

matplotlib.pyplot.hist(b,bins=10,rwidth=0.6)

f.close()
