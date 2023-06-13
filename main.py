import requests
from school import create_file, get_top_five_state

api_id = 'bd44b861'
app_key = 'c7953b281e5a719890f354b64f9758eb'

states = ['AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA',
          'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK',
          'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
school_per_state = []

uri = "https://api.schooldigger.com/v2.0/schools"


def get_all_schools():
    result = {}
    params = {'page': 1, 'perPage': 20, 'appId': api_id, 'appKey': app_key}
    for state in states:
        params['st'] = state
        response = requests.get(uri, params=params)
        if response.status_code == 200:
            result[state] = response.json().get('schoolList', [])
        else:
            print(f"Failed to retrieve schools for state {state}. Error: {response.text}")

    return result


def format_school():
    school_objs = get_all_schools()
    percent_african_students = 0.0
    for state, school_list in school_objs.items():

        for school in school_list:
            school_id = school['schoolid']
            school_name = school['schoolName']
            number_details = len(school['schoolYearlyDetails'])
            for percent in school['schoolYearlyDetails']:
                if percent['percentofAfricanAmericanStudents'] is not None:
                    percent_african_students += percent['percentofAfricanAmericanStudents']
            if number_details > 0:
                percent_african_students /= number_details

            obj = {'school_id': school_id, 'school_name': school_name, 'state': state,
                   'percent_african_students': percent_african_students}
            school_per_state.append(obj)


format_school()

create_file(school_per_state, 'school_list.txt')
get_top_five_state(school_per_state)
