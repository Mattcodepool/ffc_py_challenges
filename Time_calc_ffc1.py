def add_time(start, duration, day = None):

  days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
          "Sunday"]

  numm = start.split(":")
  start_hour = int(numm[0])
  start_ref = numm[1].split()
  start_min = int(start_ref[0])
  start_ampm = start_ref[1]
  dura = duration.split(":")
  dur_hour = int(dura[0])
  dur_min = int(dura[1])
  new_day = ""
  end_hour = (start_hour + dur_hour) % 12
  end_min = (start_min + dur_min) % 60
  swap = (start_hour + dur_hour)//12

  if end_min < 10:
    end_min = "0" + str(end_min)
    
  if (start_min + dur_min) > 60:
    end_hour +=1
    swap = (start_hour + dur_hour + 1)//12
    
  if swap % 2 == 0:
    end_ampm = start_ampm
  else:
    if start_ampm == "AM":
      end_ampm = "PM"
    else:
      end_ampm = "AM"
      if swap == 1:
        new_day = " (next day)"

  if swap == 2 :
    new_day = " (next day)"
  elif swap > 2:
    new_day = " (" + str(swap//2+1) + " days later)"
    
  if end_hour == 0:
    end_hour = "12"
  
  new_time = str(end_hour) + ":" + str(end_min) + " " + str(end_ampm)

  if day:
    weekday = days.index(day.lower().capitalize())
    if new_day == " (next day)":
      weekday += 1
    elif new_day == (" (" + str(swap//2+1) + " days later)"):
      weekday += swap//2+1
    new_time += ", " + days[weekday % 7]

  if new_day:
    new_time += new_day

  return new_time


print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM
 
print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday
 
print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM
 
print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)
 
print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)
 
print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)
