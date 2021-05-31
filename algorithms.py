from time import sleep

### Tri Fusion ###

def fusion(T1,T2):
    if T1 == []:
        return T2
    if T2 == []:
        return T1
    if T1[0] < T2[0]:
        return [T1[0]] + [fusion(T1[1:], T2)]
    else:
        return [T2[0]] + [fusion(T2[1:], T1)]

def tri_fusion(Tab):
    if Tab == []:
        return Tab
    else:
        milieu = len(Tab)//2
        return fusion(tri_fusion(Tab[:milieu]), tri_fusion(Tab[milieu:]))

### --- ###

### Tri Rapide ###

def TriRapide(Tab):
    if Tab == []:
        return Tab
    pivot = Tab[0]
    L1 = [i for i in Tab[1:] if i <= pivot]
    L2 = [i for i in Tab[1:] if i > pivot]
    return [TriRapide(L1)] + [pivot] + [TriRapide(L2)]

### --- ###

### Tri par séléction ###

def TriSelection(tab):
    for n in range (len(tab)):
        for v in range (n+1, len(tab)):
            if tab[n] > tab[v]:
                tab[n], tab[v] = tab[v], tab[n]
                
    return tab

    return tab

### --- ###

### Tri par Insertion ###

def TriInsertion(tab):
    for i in range(1, len(tab)):
        valeur = tab[i]
        pos = i
        while pos > 0 and tab[pos-1] > valeur:
            tab[pos] = tab[pos-1]
            pos = pos - 1
        tab[pos] = valeur
    return tab

### --- ###

### Tri à bulle ###

def tri_bulle(Tab):
    for i in range(len(Tab)):
        for n in range(len(Tab)-1-i):
            if Tab[n] > Tab[n+1]:
                Tab[n], Tab[n+1] = Tab[n+1], Tab[n]
    return Tab

### --- ###

### Tri par base ###
import math

def sort(array, radix=10):
    if len(array) == 0:
        return array

    # Determine minimum and maximum values
    minValue = array[0]
    maxValue = array[0]
    for i in range(1, len(array)):
        if array[i] < minValue:
            minValue = array[i]
        elif array[i] > maxValue:
            maxValue = array[i]

  # Perform counting sort on each exponent/digit, starting at the least
  # significant digit
    exponent = 1
    while (maxValue - minValue) / exponent >= 1:
        array = countingSortByDigit(array, radix, exponent, minValue)
        exponent *= radix

    return array

def countingSortByDigit(array, radix, exponent, minValue):
    bucketIndex = -1
    buckets = [0] * radix
    output = [None] * len(array)

    # Count frequencies
    for i in range(0, len(array)):
        bucketIndex = math.floor(((array[i] - minValue) / exponent) % radix)
        buckets[bucketIndex] += 1

    # Compute cumulates
    for i in range(1, radix):
        buckets[i] += buckets[i - 1]

    # Move records
    for i in range(len(array) - 1, -1, -1):
        bucketIndex = math.floor(((array[i] - minValue) / exponent) % radix)
        buckets[bucketIndex] -= 1
        output[buckets[bucketIndex]] = array[i]

    return output

### --- ###
def tamiser(tab, n, i):
    plus_long = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and tab[i] < tab[l]:
          plus_long = l
  
    if r < n and tab[plus_long] < tab[r]:
          plus_long = r

    if plus_long != i:
        tab[i], tab[plus_long] = tab[plus_long], tab[i]
        tamiser(tab, n, plus_long)

def tri_heap(tab):
    n = len(tab)
    for i in range(n//2, -1, -1):
        tamiser(tab, n, i)
  
    for i in range(n-1, 0, -1):
        tab[i], tab[0] = tab[0], tab[i]
        tamiser(tab, i, 0)
  
  
tab = [6, 900, 7, 632, 666]
tri_heap(tab)
n = len(tab)
print("Le tableau trié est")
for i in range(n):
    print("%d " % tab[i], end='')
### --- ###
espacements = [701, 301, 132, 57, 23, 10, 4, 1]
def Shell(tab):
    n = len(tab)  
    for e in espacements:
        for i in range(e, n):
            temp = tab[i]
            j = i
            while j >= e and tab[j - e] > temp:
                tab[j] = tab[j - e]
                j -= e
            tab[j] = temp
    return(tab)
