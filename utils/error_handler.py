def safe_int(prompt):#keeps asking until user gives a valid integer
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")