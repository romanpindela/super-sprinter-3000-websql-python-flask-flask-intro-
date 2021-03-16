HEADERS = ["Id", "Story Title", "User Story", "Acceptance Criteria", "Business Value", "Estimation", "Status"]
STORIES = [{HEADERS[0]: 1, "Story Title": "Some title", "User Story": "After click button is everything okay",
            "Acceptance Criteria": "Login button works", "Business Value": 100, "Estimation": 2,
            "Status": "pending"},
           {HEADERS[0]: 2, "Story Title": "Some title2", "User Story": "After login is logon",
            "Acceptance Criteria": "User can login", "Business Value": 92, "Estimation": 1,
            "Status": "done"},
           {HEADERS[0]: 3, "Story Title": "Some title3", "User Story": "33333333333333333333333",
            "Acceptance Criteria": "works", "Business Value": 87, "Estimation": 10,
            "Status": "in-progress"}
           ]

STATUS = ["new", "pending", "in-progress", "done"]


def get_headers():
    return HEADERS


def get_user_stories():
    return STORIES


def get_statuses():
    return STATUS


def get_user_story(id):
    stories = get_user_stories()
    for story in stories:
        if story[HEADERS[0]] == int(id):
            return story

    return {}


def add_user_story(story):
    STORIES.append(story)


def get_new_id():
    return STORIES[len(STORIES) - 1][HEADERS[0]] + 1


def get_default_story():
    return {HEADERS[0]: None, HEADERS[1]: "Some title", HEADERS[2]: "Some story", HEADERS[3]: "Some criteraia",
            HEADERS[4]: 50, HEADERS[5]: 1, HEADERS[6]: None}


def edit_user_story(edited_story):
    index_to_edit = -1

    for i in range(len(STORIES)):
        if STORIES[i][HEADERS[0]] == edited_story[HEADERS[0]]:
            index_to_edit = i

    if index_to_edit != -1:
        STORIES[index_to_edit] = edited_story
