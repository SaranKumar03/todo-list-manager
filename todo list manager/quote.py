import PySimpleGUI as sg

def add_task(task, tasks_list):
    tasks_list.append(task)
    return tasks_list

def remove_task(selected_task_index, tasks_list):
    if selected_task_index:
        del tasks_list[selected_task_index[0]]
    return tasks_list

def clear_tasks(tasks_list):
    tasks_list.clear()
    return tasks_list

layout = [
    [sg.Text("Todo List Manager", font=("Helvetica", 20))],
    [sg.InputText(key="-TASK-", size=(40, 1)), sg.Button("Add")],
    [sg.Listbox(values=[], size=(40, 10), key="-TASKS-", enable_events=True)],
    [sg.Button("Remove"), sg.Button("Clear"), sg.Button("Exit")]
]

def main():
    tasks = []

    window = sg.Window("Todo List Manager", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Exit":
            break

        if event == "Add" and values["-TASK-"]:
            task = values["-TASK-"]
            tasks = add_task(task, tasks)
            window["-TASKS-"].update(values=tasks)

        if event == "Remove" and values["-TASKS-"]:
            selected_task_index = values["-TASKS-"]
            tasks = remove_task(selected_task_index, tasks)
            window["-TASKS-"].update(values=tasks)

        if event == "Clear":
            tasks = clear_tasks(tasks)
            window["-TASKS-"].update(values=tasks)

    window.close()

if __name__ == "__main__":
    main()

