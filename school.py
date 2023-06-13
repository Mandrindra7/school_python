import json


def create_file(data, filename):
    res = '\n'.join(json.dumps(obj) for obj in data)
    with open(filename, "w") as file:
        file.write(res)


def get_top_five_state(schools):
    results = {}
    for school in schools:
        state = school['state']
        average_percent = school['percent_african_students']

        if state in results:
            results[state].append(average_percent)
        else:
            results[state] = [average_percent]

    average_percents = []
    for state, average_percent in results.items():
        state_percent = sum(average_percent) / len(average_percent)
        average_percents.append({"state": state, "percent": state_percent})

    sorted_school = sorted(average_percents, key=lambda x: x['percent'], reverse=True)
    create_file(sorted_school[:5], 'top_5_state.txt')
