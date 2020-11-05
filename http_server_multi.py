import requests
import matplotlib.pyplot as plt

m = 0 # Used to calculate max time
plt.figure()
sites = ['http://www.gazzetta.it', 'http://www.netflix.com', 'http://www.facebook.com']
averages = []
size = []

ABOUT_MSG = '''
HTTP server time response

Through this simple script, you can analyze any website server time response in milliseconds, finding max, min and average in 10 connection requests.
As a term of comparison, it will be plotted and analyzed even Facebook, Netflix and Gazzetta dello Sport server.
'''

print(ABOUT_MSG)
myUrl = 'http://' + input("Insert website url: ")
sites.append(myUrl)

print()
for url in sites:
    print('Test site:', url,'\n')
    tempi = []

    for _ in range(10): # 10 requests per site
        r = requests.get(url)
        tempi.append(r.elapsed.microseconds/1000)

    plt.plot(tempi, label = url)
    print('Response time - MIN:', min(tempi), '[ms]')
    print('Response time - MAX:', max(tempi), '[ms]')
    print('Response time - AVG:', sum(tempi)/len(tempi), '[ms]\n')
    averages.append(sum(tempi)/len(tempi))
    m = max([m, max(tempi)]) # Re-calculate max

print('Best average:', min(averages), '[ms] from ', sites[averages.index(min(averages))])

plt.title('Response time test')
plt.ylabel('[ms]')
plt.xlabel('ID Measures')
plt.ylim([0, 1.1*m])
plt.legend(loc = 'lower right', fontsize = 8)
plt.grid()
plt.show()
