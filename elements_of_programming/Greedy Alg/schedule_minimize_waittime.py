#given service times for a set of queries, compute a
# schedule for processing the queries that minimizes the total
# waiting time

def minimize_wait_time(tasks):

    tasks_ordered = tasks.sort()
    total_wait_time = 0
    for i, service_time in enumerate(tasks):
        remaining_tasks = len(tasks) - (i + 1)
        total_wait_time += service_time * remaining_tasks
    return total_wait_time


print minimize_wait_time([2,5,1,3])