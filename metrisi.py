

from collections import Counter
data=[]
#DATA_FILL______________________________________________________

def fill_data_table():

    for m in range(int(input("Αριθμός μετρήσεων για εισαγωγή....."))):
        data.append(float(input("Εισάγετε μέτρηση  {0}...".format(m))))

    return data

#MODE__________________________________________________

def calculate_mode(data_set):

    a=Counter(data_set).most_common()[0][1]
    return a

#MEDIAN__________________________________________________

def calculate_median(data_set):
    N = len(data_set)
    data_set.sort()
    if N % 2 == 0:
        median = ((data_set[int((N/2))]+data_set[int((N/2)-1)])/2)
    else:
        median = data_set[int((N/2)-0.5)]

    return median



#RANGE_____________________________________________________

def find_range(data_set):
    lowest = min(data_set)
    highest = max(data_set)
    range = highest-lowest
    return lowest, highest, range

#FREQUENCY_TABLE--------------------------------------------
def frequency_table(data_set):
    table = Counter(data_set)
    print('Number\tFrequency')
    for n in table.most_common():
        print('{0}\t{1}'.format(n[0], n[1]))

#MEAN________________________________________________________
def calculate_mean(data_set):
    s = sum(data_set)
    N = len(data_set)
    mean = s/N
    return mean

#VARIANCE----------------------------------------------------
def find_differences(data_set):

    mean = calculate_mean(data_set)
    diff = []
    for num in data_set:
        diff.append(num-mean)
    return diff

def calculate_variance(data_set):
    diff = find_differences(data_set)
    squared_diff = []
    for d in diff:
        squared_diff.append(d**2)

    sum_squared_diff = sum(squared_diff)
    variance = sum_squared_diff/len(data_set)
    return variance

#STANDARD DEVIATION----------------------------------------------------
def calculate_standard_deviation(data_set):
    standard_deviation=(calculate_variance(data_set))**0.5
    return standard_deviation

#OUTPUT PARAMETERS ----------------------------------------------------

def output():
    print()
    print()
    print("-----------------------REPORT--------------------------")

    print ( "Τα δεδομένα σας είναι  {0}".format(data))
    print()
    print('Η διακύμανση είναι   {0:.2f}'.format(calculate_variance(data)))
    print()
    print('Η τυπική απόκλιση είναι  {0:.2f}'.format(calculate_standard_deviation(data)))
    print()
    print('Ο μέσος είναι {0:.2f}'.format(calculate_mean(data)))
    print()
    print('Ο διάμεσος είναι  {0:.2f}'.format(calculate_median(data)))
    print()

    print('H μέτρηση είναι   {0:.2f}'.format(calculate_mean(data)))
    print('Το σφάλμα είναι +/-  {0:.2f}'.format(calculate_standard_deviation(data)))

fill_data_table()
output()

# Write your code here :-)
