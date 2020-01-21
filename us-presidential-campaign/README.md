# Analyzing U.S. presidential campaign contributions dataset
___
## First step
Download the dataset at http://ocw.mit.edu/ans7870/RES/RES.6-009/iap12/datasets/P00000001-ALL.zip
The file contains information about the candidate, the donor's city, state, zip code, employer and occupation information,
as well as the amount donated. In addition it contains the date of the donation.

Open terminal, unzip the file and rename it to something meaningful.

```$ unzip P00000001-ALL.zip```

```$ mv P00000001-ALL.txt donations.txt```

## View the names of each fields
``` $ head -n3 donations.txt ```
```cmte_id,cand_id,cand_nm,contbr_nm,contbr_city,contbr_st,contbr_zip,contbr_employer,contbr_occupation,contb_receipt_amt,contb_receipt_dt,receipt_desc,memo_cd,memo_text,form_tp,file_num```

## Sampling data
The dataset is relatively large, processing the whole dataset takes a lot of time. It should be sampled and try things out on a smaller dataset before doing the full dataset analysis.  The following is a script that samples
the donations.txt. The following script prints 1 out of 1000 donations:

```
import sys
with file(sys.argv[1], 'r') as f:
 i = 0
 for line in f:
 if i % 1000 == 0:
 print line[:-1]
 i += 1
 
 ```
 To create a new file, use  the > standard output redirector
 
 ```$ python sampling.py donations.txt > donations_sampled.tx```

## Plotting the data
We want to compare Obama's total donations with McCain's ones over a period of time in 2008 U.S. presidential campaign.
We will compute daily total donations of each candidate and use **matplotlib** to create a chart.

```
import matplotlib.pyplot as plt
import csv,sys,datetime
from collections import defaultdict
reader = csv.DictReader(open(sys.argv[1], 'r'))

obamadonations = defaultdict(lambda:0)
mccaindonations = defaultdict(lambda:0)

for row in reader:
    name = row['cand_nm']
    datestr = row['contb_receipt_dt']
    amount  = float(row['contb_receipt_amt'])
    if amount < 0:
	    line = '\t'.join(row.values())
    date = datetime.datetime.strptime(datestr, '%d-%b-%y')

    if 'Obama' in name:
	    obamadonations[date] += amount
    elif 'McCain' in name:
	    mccaindonations[date] += amount


sorted_by_date = sorted(obamadonations.items(), key=lambda (key,val): key)
sorted_by_date2 = sorted(mccaindonations.items(), key=lambda (key,val): key)

xs,ys = zip(*sorted_by_date)
xs2,ys2 = zip(*sorted_by_date2)

plt.plot(xs, ys, label='Obama''s donations')
plt.plot(xs2, ys2,label='McCain''s donations')

plt.legend(loc='upper center', ncol = 4)
plt.show()
```
A few notes about the code
1. reader = csv.DictReader(open(sys.argv[1], 'r')) takes input file name as its argument
2. We need to sort the data in obamadonations by the date (the key). sorted(l, key=f) returns a sorted copy of
l and calls f to extract the key to use for comparison.
3. zip(*pairs) then unzips the list of pairs into two lists.

![image](https://user-images.githubusercontent.com/40592382/54732892-e63fe400-4bc8-11e9-900a-bd5cf1f6ae4e.png)

Visited wikipedia and just found some key interesting facts

It can be seen that Obama's donations outnumbered McCain's, especially the period of time around the end of 2008. A further detailed look shows that there are two spike in the plot, in August 2008 and October 2008.
In August that year, Democratic National Convention took place and the Democratic Party nominated Barack Obama as their presidential candidate.
In October, Obama and McCain had their second and third presidential debate. In additons, Obama's 30-minute presidential campaign advertising was broadcast in prime-time over several networks


