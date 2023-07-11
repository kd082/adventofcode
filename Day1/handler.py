# from utils.transform_file import readLines()
import utils.transform_file as data

# Read the data
lines = data.readLines()

# Transform the data
result = data.transformLines(lines)

 
# Get the Max
puzzle1 = data.getMaxCal(result)
puzzle2 = data.getMaxCalTop3(result, 3)

print(f"Calories carried by Top Elf: {puzzle1}")
print(f"Calories carried by Top three Elves: {puzzle2}")

   

