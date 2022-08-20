guest_list = ['luiz', 'tim', 'roberto', 'brandi']
'''for guest in guest_list:
    message = f"\n{guest.title()},\nPlease join me for a dinner party on Saturday at 7:00PM."
    print(message)'''

print(f"\n{guest_list[2].title()} cannot make the dinner part due to work")

guest_list[2] = "jennifer"
for guest in guest_list:
    message = f"\n{guest.title()},\nUPDATE: There has been a change in the time, please join me for a dinner party on Saturday at 8:00PM."
    print(message)
