def initialize():
    global WAIT_CODE, START, PROJECT_NAME, PROJECT_DESCRIPTION, PROJECT_POC, PROJECT_VENUE, PROJECT_PURPOSE, \
        PROJECT_INSPIRATION, PROJECT_ROLES, PROJECT_DEADLINE, PROJECT_REQUIREMENTS, PROJECT_TEAM, PROJECT_CONFIRM, \
        REMOVE, ANNOUNCE_QUERY, ANNOUNCE, EDIT, EDIT_CONFIRM, VIEW_PROJECTS, BLOCK_ADD

    WAIT_CODE = range(1)
    START = range(1, 2)
    PROJECT_NAME, PROJECT_DESCRIPTION, PROJECT_POC, PROJECT_VENUE, PROJECT_PURPOSE, PROJECT_INSPIRATION, \
    PROJECT_ROLES, PROJECT_DEADLINE, PROJECT_REQUIREMENTS, PROJECT_TEAM, PROJECT_CONFIRM = range(2, 13)
    REMOVE = range(14, 15)
    ANNOUNCE_QUERY, ANNOUNCE = range(15, 17)
    EDIT, EDIT_CONFIRM = range(17, 19)
    VIEW_PROJECTS = range(19, 20)
    BLOCK_ADD = range(20, 21)