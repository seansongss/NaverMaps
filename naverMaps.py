import json
import csv

with open('naverMaps.json', 'rt', encoding='UTF8') as json_file:
    data = json.load(json_file)
    data = data['my']['bookmarkSync']['bookmarks']
    print(len(data))
    count = 1
    with open('naverMaps.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['이름', '주소', '위도 및 경도'])
        for d in data:
            new_d = d['bookmark']
            writer.writerow([new_d['name'], new_d['address'], str(new_d['py']) + ', ' + str(new_d['px'])])
            print(new_d['name'] + '; ' + new_d['address'] + '; ' + str(new_d['py']) + ', ' + str(new_d['px']))
            count += 1