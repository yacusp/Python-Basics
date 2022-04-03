seconds = int(input('Enter time in seconds: '))

hours = seconds // 3600
seconds = seconds % 3600
minutes = seconds // 60
seconds = seconds % 60

print(f"Your time is: {hours:02d}:{minutes:02d}:{seconds:02d}.")
