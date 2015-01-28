import math

print("This program will help you plan your garden.")
print("First, we need some information about the dimensions you want.")

print()

#Prompt for input
side_str = input("Please enter the side length for your garden (in feet):")
distance_str = input("Please enter the distance between plants (in inches):")
flower_depth_str=input("Please enter the depth for the flower beds (in feet):")
fill_depth_str = input("Please enter the depth for the fill (in feet):")

print()

#Convert string into float
side_float = float( side_str )
distance_float =float( distance_str )
flower_depth_float = float( flower_depth_str )
fill_depth_float = float( fill_depth_str )

#Calculations for plant needs
triangle_area=(side_float/2)*(side_float/2)*.5)
total_triangle_area = int(triangle_area*4)
circle_area= (math.pi*(side_float/4)**2)
tiny_square_area= (distance_float/12)**2
triangular_plants= int(triangle_area/tiny_square_area)
circle_plants= int(circle_area / tiny_square_area)

print("Summary of your plant needs.")
print("Each outer triangular bed: ",triangular_plants,"plants.")
print("The center circular bed:",circle_plants,"plants.")
print("Total:",circle_plants+(triangular_plants*4),"plants.")

print()

#Calculations for soil needs
soil_triangle= triangle_area  * flower_depth_float /27
soil_circle= circle_area * flower_depth_float /27


print("Summary of your soil needs.")
print("Each outer triangular bed:",round(soil_triangle, 1),"cu. yd.")
print("The center circular bed:",round(soil_circle, 1),"cu. yd.")
print("Total:",round(soil_triangle*4 + soil_circle, 1),"cu.yd.")

print()

#Calculations for fill needs
area_of_square= (side_float * side_float)
garden_area =(total_triangle_area + circle_area)
fill_area= (area_of_square - garden_area)
fill_area_times_depth= (fill_area * fill_depth_float)
fill_area_in_yards = (fill_area_times_depth / 27)

print("Summary of your fill needs.")
print("Total:",round(fill_area_in_yards,1),"cu. yd.")

