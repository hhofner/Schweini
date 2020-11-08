'''
This file describes the todo.txt format.

      creation-date, completion-date
__ __ __________ __________ ___________________ _________ _______ ______________ ______________
x  A  2020-05-10 2020-10-11 add cli tooling for @schweini +python due:2020-11-12 do:2020-09-09

key value pair usage and rules:
    do:{date value or pre-defined strings} -> This is used for the "today" report and the "up-next" reports
    which mimic what Things 3 (and others) do, which allows you to "assign" a task for a day and at the same
    time have a "due" value. It also allows you to have tasks to be "assigned" for tomorrow, next week, etc.

    cancel:{true|false} -> This will allow you to cancel tasks rather than delete them or "complete" them even though
    you didn't actually complete it. This is used for tasks that you've decided you no longer want to do, or habits that
    you didn't accomplish on the day, or tasks that have been done by someone else, for example.

special tags:
    +HABIT -> This is to mark a "habit-task", which, if you tag it, will create a recurring task that will auto
    cance; this task if not marked "done" by some specified time:
    TODO: Need to think this one through, will be a bit tricky. Things to consider:
        - somehow define when this gets canceled
'''


