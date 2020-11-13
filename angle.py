time = input('Time: ')
print(time) 

time_value = list(time.split(':'))
print(time_value)
hour = int(time_value[0])
minute = int(time_value[1]) 
print(hour, minute) 

h_deg = 30
m_deg = 6

total_angle_hour = h_deg * hour + (15 * minute) / 30 #accounting for smaller changes impacted by minute, based on 15 degree shift every 30 minutes. 
total_angle_minute = m_deg * minute 
print(total_angle_hour, total_angle_minute)

delta_angle = abs(total_angle_hour - total_angle_minute) 
print(delta_angle) 
