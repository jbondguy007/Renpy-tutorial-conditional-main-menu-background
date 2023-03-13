# Default the flag variable.
default persistent.my_flag = False

# Define the dynamic displayable and its conditions.
image dynamic_main_menu_bg = ConditionSwitch(
    "persistent.my_flag", "images/chapter2_bg.png",
    "True", "images/default_bg.png"
)

# Set the main menu background to the dynamic displayable defined above.
define gui.main_menu_background = "dynamic_main_menu_bg"

label start:
    "This is chapter one."
    menu:
        "Jump to chapter 2?"
        # This will trigger the flag and change the main menu background.
        "Yes":
            jump chapter_2
        # This will not trigger the flag, and instead return you to the main menu without change.
        "No":
            "You've not reached chapter 2, and therefore have not triggered the flag."
            "Ending script..."
            return

label chapter_2:
    $ persistent.my_flag = True
    "You've reached chapter 2 and triggered the flag."
    "Ending script..."
    return
