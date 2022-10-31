date=(input("enter today date:")).lower().strip()
place=(input("enter the place:")).lower().strip()
name=(input("enter your name:")).lower().strip()
class_name=(input("enter your classname:")).lower().strip()
section=(input("enter your section:")).lower().strip()
school_name=(input("enter your schoolname:")).lower().strip()
class_teacher_name=(input("enter your class teacher name:")).lower().strip()
subject=(input("enter the subject:")).lower().strip()
reason=(input("enter the reason for leave:")).lower().strip()
no_of_leave_days=(input("enter no of leave days:")).lower().strip()
date_of_leave=(input("enter the date of leave:")).lower().strip()
permission_letter=f'''
                 
                                     Leave Letter

From                                                                                            Date:{date} 
        {name}
        {class_name} sec {section}
        {school_name}
        {place}

To
        {class_teacher_name}
        {class_name} sec {section}
        {school_name}
        {place}

Respected Sir/Madam  
             sub:{subject}
                      I am {name}. Studying in {class_name} sec {section}. I'm not able attend my class today
due to {reason}.I want a permission to take a leave for {no_of_leave_days} days {date_of_leave} . kindly give permission 
for oneday to take a leave.
                              Thankyou
                                                                         your's faithfully
                                                                             {name}                                                                         
'''
print(permission_letter)

