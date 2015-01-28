##########################
#Computer Project #2
#
# Algorithm
#   prompt for an integer
#   input an integer
#   calculate 
#   display summary
##########################

import math

print("This program will help you plan your garden.\n")

#ask user for input
side_str = input("Please enter the side length for your garden (in feet):")
dist_str = input("Please enter the distance between plants (in inches):")
bed_depth_str = input("Please enter the depth for the flower beds(in feet):")
fill_depth_str = input("Please enter the depth for the fill (in feet):")
print()

#convert str to float
side_float = float(side_str)
dist_float = float(dist_str)
bed_depth_float= float(bed_depth_str)
fill_depth_float = float(fill_depth_str)

#calculations for plant needs
area_semi = (math.pi*(side_float/4)**2/2)
total_area_semi = int(area_semi*4)
area_center = (math.pi*(side_float/4)**2)
total_area_center = int(area_center*4)
total_plants = (total_area_semi*4) + total_area_center

print("Summary of your plant needs:")
print("Each outer semi-circular bed:",total_area_semi,"plants")
print("The center circular bed:",total_area_center,"plants")
print("Total:",total_plants,"plants\n")

#convert to cubic yards, soil need calc
cubic = 3*(1/3**3)
soil_semi_yards = (total_area_semi * cubic/4)
soil_area_yards = (total_area_center * cubic/4)
total_semi_soil = (soil_semi_yards * 4)
total_soil = (total_semi_soil + soil_area_yards)

print("Summary of your soil needs:")
print("Each outer semi-circular bed:",round(soil_semi_yards,1),"cubic yards")
print("The center circular bed:",round(soil_area_yards,1),"cubic yards")
print("Total:",round(total_soil,1),"cubic yards\n")

#fill need calculations
square_area = (side_float * 12)
center_bed = (total_area_center/4)
fill = (square_area - (total_area_semi + center_bed))
total_fill = (fill * fill_depth_float)
total_yards = (total_fill/27)

print("Summary of your fill needs:")
print("Total:",round(total_yards,1),"cubic yards")










