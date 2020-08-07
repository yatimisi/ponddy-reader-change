import os
import json


def main(before_name, data_name, after_name):
    file_path = os.path.join(before_name)

    fields = [
        'id',
        'description',
        'content_id',
        'record_id',
        'title',
        'type',
        'updated',
        'position',
    ]

    tmp = []
    dataset = []

    with open(file_path) as file:
        tmp = file.readlines()

    for values in tmp:
        data = {}
        for i, value in enumerate(values[:-1].split('\t')):
            data[fields[i]] = json.loads(value) if fields[i] == 'description' else value
        dataset.append(data)

    print('len: ', len(dataset))

    data_path = os.path.join(data_name)

    data_fields = [
        'Pondlet_ID',
        'Content_Id',
        'plan',
        'Simp',
        'un_Simp',
        'Sentences',
    ]

    data_values = []
    tmp = []

    with open(data_path) as file:
        tmp = file.readlines()

    for values in tmp:
        data = {}
        for i, value in enumerate(values[:-1].split('\t')):
            data[data_fields[i]] = value
        data_values.append(data)

    print(*dataset[:3], sep='\n')
    print()
    print(*data_values[:3], sep='\n')

    for value in data_values:
        for data in dataset:
            if data['content_id'] == value['Content_Id']:
                for description in data['description']:
                    if description['word'] == value['Simp']:
                        description['description'] = description['description'] + '<br>' + value['Sentences']
                        # description['word'] = unicode(description['word'], "big5")
                print(value['Content_Id'], value['Simp'], value['Sentences'], data)
                print()

    print(*dataset[:3], sep='\n')

    after_path = os.path.join(after_name)

    with open(after_path, "a") as file:
        for data in dataset:
            output_str = ''
            for i, value in enumerate(data.items()):
                output_str += str(value[1]) + ('\n' if i == len(data) - 1 else '\t')
            file.write(output_str)

    # print(dataset[0]['description'][0]['word'])
    # dictionaries = Dictionary.objects.filter(voice__in=[row['voice'] for row in data if row['voice']])
    # for row in data:
    #     for dictionary in dictionaries:
    #         if dictionary.voice == row['voice']:
    #             row['dictionary'] = dictionary.pk

    # print(*show_fields, sep='\t')

    # for row in data:
    #     if row['show'] is True and all(field in row.keys() for field in show_fields):
    #         for field in show_fields:
    #             print(row[field], end='\t')
    #         print()

if __name__ == '__main__':
    before_name = 'before'
    after_name = 'after'
    data_name = 'data'
    main(before_name, data_name, after_name)
