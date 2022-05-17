import time


month_dic = { 
    "01":'January', 
    "02": 'February', 
    "03": 'March', 
    "04": 'April', 
    "05": 'May', 
    "06": 'June', 
    "07": 'July',
    "08": 'August', 
    "09": 'September', 
    "10": 'October', 
    "11": 'November', 
    "12": 'December'
}

day_dic = {
    '01': '1st', '02': '2nd', '03': '3rd', 
    '04': '4th', '05': '5th', '06': '6th', 
    '07': '7th', '08': '8th', '09': '9th', 
    '10': '10th', '11': '11th', '12': '12th', 
    '13': '13th', '14': '14th', '15': '15th', 
    '16': '16th', '17': '17th', '18': '18th', 
    '19': '19th', '20': '20th', '21': '21st', 
    '22': '22nd', '23': '23rd', '24': '24th', 
    '25': '25th', '26': '26th', '27': '27th', 
    '28': '28th', '29': '29th', '30': '30th', 
    '31': '31st'
}

def convert_date(x):
    stripped = x.split("-")

    #grab 1st element from stripped (month)
    #get converted month from month_dic dictionary
    month = stripped[0]
    converted_month = month_dic[month]

    #grab 2nd element from stripped (day)
    #get converted day from day_dic dictionary
    day = stripped[1]
    converted_day = day_dic[day]

    #grab 3rd element from stripped (year)
    year = stripped[2]

    #concatenate month, day, year into variable results
    results = converted_month + " " + converted_day + ", " + year

    return results


while True:

    time.sleep(1)    
    #open file
    convertFile = open('convert.txt', 'r+')  
    convertRead = convertFile.readline()

    if len(convertRead) == 10:
        #convert to format
        new_date = convert_date(convertRead)
        convertFile.close()
        time.sleep(2)

        #write new date format into results.txt
        resultsFile = open('results.txt', 'w')
        resultsFile.write(new_date)
        resultsFile.close()
        time.sleep(2)

        #let project know that it can retrieve
        #correct format date 
        convertFile = open('convert.txt', 'w')
        convertFile.write('DONE')
        convertFile.close()
        time.sleep(2)


if __name__ == "__main__":
    i = "05-06-2022"
    final = convert_date(i)
    print(final)
