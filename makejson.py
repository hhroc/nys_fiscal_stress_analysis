import json

if __name__ == '__main__':

    """

    The tex file is in the following format (repeated n-times).

    name
    class
    county
    region
    fiscal year end
    type of stress
    fiscal score
    environmental rating
    environmental score
    snapshot date

    Note: for some schools the 'type of stress' field has a value
          of 'Not filed' or 'Inconclusive'.  These need to be
          adressed as the next four fields will be missing after that.

    """

    # there are 10 fields in the doc
    FIELDCOUNT = 10

    # decoded text file
    filename = 'decoded.txt'

    print "Reading in file ..."

    with open(filename,'r') as f:
        contents = f.read()

    print "Pre-Processing file ..."

    # handle not filed and inconclusive cases
    contents = contents.replace('Not filed\n','Not filed\nN/A\nN/A\nN/A\n')
    contents = contents.replace('Inconclusive\n','Inconclusive\nN/A\nN/A\nN/A\n')

    # get each line
    lines = contents.split('\n')

    print "Processing file ..."

    districts = []
    for i in range(0,len(lines)/FIELDCOUNT):
        j = i * FIELDCOUNT
        district = {
            'name': lines[j+0],
            'class': lines[j+1],
            'county': lines[j+2],
            'region': lines[j+3],
            'fiscal_year_end': lines[j+4],
            'type_of_stress': lines[j+5],
            'fiscal_score': lines[j+6],
            'environmental_rating': lines[j+7],
            'environmental_score': lines[j+8],
            'snapshot_date': lines[j+9],
        }
        districts.append(district)

    print "Writing out json file ..."

    with open('districts.json','w') as f:
        f.write(json.dumps(districts))

    print "Writing out csv file ..."

    with open('districts.csv','w') as f:
        headers = 'name,' + \
                  'class,' + \
                  'county,' + \
                  'region,' + \
                  'fiscal year end,' + \
                  'type of stress,' + \
                  'fiscal score,' + \
                  'environmental rating,' + \
                  'environmental score,' + \
                  'snapshot date,\n'
        f.write(headers)

        for district in districts:
            line = '' + \
                district['name'] + ',' + \
                district['class'] + ',' + \
                district['county'] + ',' + \
                district['region'] + ',' + \
                district['fiscal_year_end'] + ',' + \
                district['type_of_stress'] + ',' + \
                district['fiscal_score'] + ',' + \
                district['environmental_rating'] + ',' + \
                district['environmental_score'] + ',' + \
                district['snapshot_date'] + ',\n'
            f.write(line)

    print "Done."


