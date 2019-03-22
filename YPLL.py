import csv
import numpy
import matplotlib.pyplot as plt

independent_cols = ["Population", "< 18", "65 and over", "African American","Female", "Rural", "%Diabetes" , "HIV rate","Physical Inactivity" , "mental health provider rate","median household income", "% high housing costs","% Free lunch", "% child Illiteracy", "% Drive Alone"]
dependent_cols = ["YPLL Rate"]

def read_csv(filename, cols, Unreliable):
    reader = csv.DictReader(open(filename, 'r'))
    rows = {}
    for line in reader:
        if Unreliable and line['Unreliable'] == 'x':
            continue
        if line['County'] == '':
            continue
        rname = '%s__%s' % (line['State'], line['County'])
        try:
            rows[rname] = [float(line[col]) for col in cols]
        except:
            pass
    return rows

def get_arrs():
    ypll = read_csv('ypll.csv', dependent_cols, True)
    measures = read_csv('additional_measures_cleaned.csv', independent_cols, False)

    ypll_arr = []
    measures_arr = []

    for key,value in ypll.items():
        if key in measures:
            ypll_arr.append(value[0])
            measures_arr.append(measures[key])  
    return(numpy.array(ypll_arr), numpy.array(measures_arr))

ypll_arr, measures_arr = get_arrs()

fig = plt.figure(figsize=(6, 8))

subplot = fig.add_subplot(311)
subplot.scatter(measures_arr[:,6], ypll_arr, color='#1f77b4')
subplot.set_title("ypll vs. % of population with diabetes")

subplot = fig.add_subplot(312)
subplot.scatter(measures_arr[:,8], ypll_arr, color='#2072DD')
subplot.set_title('ypll vs. % of population without physical activities')

subplot = fig.add_subplot(313)
subplot.scatter(measures_arr[:,12], ypll_arr,color='#629BE5' )
subplot.set_title('ypll vs. % of population having free lunch')



plt.show()
#plt.savefig('temp/figure1.png', format='png')

exit()


