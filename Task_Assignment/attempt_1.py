# O(nLog(n)) time | O(n) space where n is length of tasks

def taskAssignment(k, tasks):
    sorted_tasks = sorted(tasks)
    paired_list = []

    task_duration_indices = {}
    for i, task in enumerate(tasks):
        if task in task_duration_indices:
            task_duration_indices[task].append(i)
        else:
            task_duration_indices[task] = [i]

    for i in range(k):
        worker_1_sorted_task = sorted_tasks[i]
        indices_worker_1 = task_duration_indices[worker_1_sorted_task]
        worker_1_index = indices_worker_1.pop()

        worker_2_sorted_task = sorted_tasks[len(tasks) - 1 -i]
        indices_worker_2 = task_duration_indices[worker_2_sorted_task]
        worker_2_index = indices_worker_2.pop()

        paired_list.append([worker_1_index, worker_2_index])

    return paired_list
