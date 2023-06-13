import json


def create_file(data, filename):
    res = '\n'.join(json.dumps(obj) for obj in data)
    with open(filename, "w") as file:
        file.write(res)


def get_top_five_state(schools):
    sorted_school = sorted(schools, key=lambda x: x['percent_african_students'], reverse=True)
    result = sorted_school[:5]
    create_file(result, 'top5state.txt')
