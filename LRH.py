import itertools, csv, os
from datetime import datetime




def group_separator(line):
    return line=='\n'



def line_counter(file): #file need to be the list of files and \n inside each type of data has been removed.
    global num
    num = []  # after the following 5 lines, the list will contain all numbers to search for the journal, line

    numbering = [str(i) for i in range(1, len(file))]
    for i in numbering:
        s = i + '.'
        num.append(s)


currentYear = datetime.now().year
now = datetime.now()
curtime = now.strftime('%Y-%m-%d_%H:%M:%S')
data = []
new_data = []

file_name = input("Please input the file name: ")
while bool(file_name) ==False:
    file_name = input('File name can not be empty, please enter again: ')


with open("./"+file_name+'.txt', "r") as lf: # open the txt file
    for key, group in itertools.groupby(lf, group_separator): # process context based on empty line(s)
        #print(key,list(group))
        if not key: # if the block of lines are not empty
            for i in [list(group)]: # merge them together into one block of text
                temp_data=''.join(i)
                data.append(temp_data) # append the edited text block into a new list


# remove unwanted \n

for i in data:
    l = ' '.join(i.splitlines())
    new_data.append(l)


data = [] # reset the data list and each word as a component inside the sublist(each line)
for i in new_data: # iterate through the list created
    t = i.split()
    data.append(t)

line_counter(data) # numberings system build for extraction of literature info etc.



# now, how to extract all sorts of info, most important, title, url, abstract, authors and year of publication.
# also think about if possible to add some kind of citation info. Maybe not now. Do this in version 2

output = input('Please enter a name for the output: ')
while bool(output) ==False:
    output = input('File name can not be empty, please enter again: ')




with open('./'+output+'.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    header=['FileCreated_'+curtime, 'Title', 'Authors', 'Year', 'Abstract','doi', 'SearchInGoogleScholar', 'Notes']
    writer.writerow(header)

with open('./'+output+'.csv', 'a', newline='')as csvfile:
    writer = csv.writer(csvfile, dialect='excel')

    for i in range(0,len(num)):

        title = 'NA'
        authors = 'NA'
        ab = 'NA'

        # when find the number, means that start of a new article
        if data[i][0] in num:
            try:
            # title found and saved
                title = new_data[i+1]

            # authors found and saved
                authors = new_data[i+2]

            # abstracts found and saved,
                if len(new_data[i+4])>len(new_data[i+5])>0:
                    ab = new_data[i+4]
                elif len(new_data[i+5])>len(new_data[i+4])>0:
                    ab = new_data[i+5]

            # count

            except IndexError:
                pass
            # converting list to iterator
            Ite = iter(data[i])

            # reset info to avoid error in doi
            doi = 'Information Not Found'
            pub_yr = 'Information Not Found'
            No = data[i][0]

            keywords = '+'.join(data[i + 1])
            link = 'http://scholar.google.co.nz/scholar?hl=en&as_sdt=1%2C5&q={}&btnG='.format(keywords)
            for n in range(200):

                t = next(Ite,'NA')

                # dates
                year = ''
                if t =='NA':
                    break
                elif t == 'doi:':
                    doi = 'doi:'+next(Ite)[:-1]
                    # print('doi: '+doi)
                elif t in [str(y) for y in range(1960,currentYear+1)]:
                    pub_yr = t


            writer.writerow([No, title, authors, pub_yr, ab, doi,link, ''])



# google scholar
# https://scholar.google.co.nz/
