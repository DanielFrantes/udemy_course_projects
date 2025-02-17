todos = []
user_prompt = "Type todo: "
while True:
    todo = input(user_prompt)
    print(todo.title())
    todos.append(todo)
    print(todos)