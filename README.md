## Introduction

This short tutorial will walk you through setting up a conditional main menu background - in simpler terms, a main menu background that changes as you trigger a certain flag or reach a certain point in the game, etc.

### Basic Understanding

This tutorial will involve **Persistent Data** and **Dynamic Displayables** (`ConditionSwitch()`), both of which their usage will be explained in this tutorial. With that said, a basic understanding of variables and conditional statements will greatly improve your understanding of their use. If you have no coding or Ren'Py experience, I recommend the official Ren'Py [Quickstart](https://www.renpy.org/doc/html/quickstart.html) guide, especially the [Supporting Flags using the Default, Python and If Statements](https://www.renpy.org/doc/html/quickstart.html#supporting-flags-using-the-default-python-and-if-statements) section.

Additionally, this tutorial expects you understand Ren'Py basics such as defining displayables. It is recommended to read the [Image Statement](https://www.renpy.org/doc/html/displaying_images.html#image-statement) section of the official Ren'Py documentation.

Whenever I mention to "define" (or `default`, etc) anything, this means that statement belongs **outside of labels**, either at the very top of your script file, or in a separate `.rpy` file entirely.

## Persistent Data

### Persistent Data - Explanation

Ren'Py has a few particuliar way to save data. The most common ways to define variables are `default` and `define`, both of which have their own use (read more at [Python Statements](https://www.renpy.org/doc/html/python.html). The `default` statement is what you would typically use to define a flag variable (in simpler term, a "switch" that toggles or determines if a certain thing was achieved in the game, such as reaching a certain chapter, etc).

The caveat of a normal `default`ed variable however, is that the variable will only be accessible within the scope of a point in the game, or of a save file. As the main menu is not part of that scope, you can't refer to that variable as a flag for a condition to change the main menu background.

In comes **[Persistent Data](https://www.renpy.org/doc/html/persistent.html)**. By prefixing your variable name with `persistent.` you will effectively save that variable to the `persistent` store, which's scope includes all of Ren'Py, including the main menu. Persistent variables, are, well... persistent. Once a persistent variable is set or changed, it is permanently set to the new value even after exiting the game, until it is replaced again or manually deleted.

### Persistent Data - Setting Up

Now that you have a basic idea of what a persistent variable is, let's set the stage for a persistent flag variable. Firstly, keep in mind that a persistent variable may be treated exactly the same way you would a normal `default`ed variable. So first, let's default a persistent variable named `my_flag` - this is only an example, it is strongly recommended you choose a name that is relevant to the case use.

```py
default persistent.my_flag = False
```
Now that you've `default`ed your variable, you may use it to trigger a flag somewhere relevant in your game, such as when reaching a specific chapter in your game.
```py
# [...]
label chapter_2:
    $ persistent.my_flag = True
    "You've reached chapter 2."
    # Etc...
```

### Persistent Data - Clearing Data

Please bear in mind, as noted above, that persistent variables will persist even after starting a new game or exiting the game entirely. As such, it is good to know, and always remember, that persistent data can be cleared via the Ren'Py launcher. You should remember to do so regularly during playtesting if you encounter issues where the flag needs to be reset.

![Clearing persistent data](https://i.imgur.com/jvhMNjd.png)

## Dynamic Displayable

### Dynamic Displayable - Explanation

Now that our flag is ready, we just need to setup the dynamic main menu background. There are a few ways you could go about it, but the simpler, recommended solution is to make use of **[Dynamic Displayables](https://www.renpy.org/doc/html/displayables.html#dynamic-displayables)**, more specifically, [ConditionSwitch()](https://www.renpy.org/doc/html/displayables.html#ConditionSwitch).

`ConditionSwitch()` is a Ren'Py displayable, which means Ren'Py will treat it the same way it would any other displayables, such as normal images. The difference is that such displayables offer far more control over what is being displayed - for example, `ConditionSwitch()` takes multiple displayables (such as an image) alongside conditional statements, and will only display the displayable where the condition or conditions are met.

### Dynamic Displayable - Example

A `ConditionSwitch()` displayable is defined as an image, the same way you would any other displayable - using the `image` statement.
The proper syntax is:
```py
image my_image_name = ConditionSwitch(
    "condition1", "images/background1.png",
    "condition2", "images/background2.png",
    "True", "images/background3.png"
)
```
Each "condition" represents a placeholder for a Python conditional statement. Unlike your typical condition in Python/Ren'Py, the condition must be passed as a string (surrounded in quotes). Conditions are checked in the order they are listed - "condition1" will be checked first, and if it returns `False`, it'll go to "condition2" and so on. The last condition is just "True" so that it always picks this option if all other conditions return `False` - this can be used as what you'd normally call the `else` statement, the "catch-all" statement in case all other conditions fail.

Conditions in `ConditionSwitch()` have slightly different syntax than usual, as you do not need to specify `if`, `elif` or `else`. You can write simple conditions such as `"variable_a >= 10"`, `"variable_b == 'Hello World!'"` etc.

### Dynamic Displayable - Setting Up

In our case, we have one single flag, so we only need to check one condition - if `persistent.my_flag` returns `True` or `False`.
```py
image dynamic_main_menu_bg = ConditionSwitch(
    "persistent.my_flag", "images/chapter_2_bg.png",
    "True", "images/default_main_bg.png"
)
```
In Python, `if boolean_var:` is a shorthand equivalent of `if boolean_var == True:`. This is what is used in this example above.
With this new displayable defined, we can move on to the last part of the process - changing the main menu background to this displayable.

## Main Menu Background

### Main Menu Background - Defining a New Background

This is the final and simplest step of the process. Firstly, open your project's `gui.rpy` file. This can be done through the Ren'Py launcher.

![Opening gui.rpy file from the Ren'Py launcher](https://i.imgur.com/0P0VCNo.png)

Next, locate `gui.main_menu_background` which should be around line 88, but this may change from one Ren'Py version to the other so it is recommended you simply use the "find" function of your text editor to locate this line of code.

![gui.main_menu_background](https://i.imgur.com/8HrRoFr.png)

Now, simply remove `"gui/main_menu.png"` and replace it with your new displayable name, within quotes:
```py
define gui.main_menu_background = "dynamic_main_menu_bg"
```
Save the changes to the file, and you're done! Once you reach the flag (chapter 2 in this case), the main menu background will permanently change to the chapter 2 background.

As mentioned previously, keep in mind that if you ever need to reset this flag during development, you'll have to clear persistent data from the Ren'Py launcher. You may also want to consider setting up a way for the player to manually reset the persistent flags from in-game, if they want to play through the game again from the beginning without seeing persistent changes to the main menu.

## Afterword

This concludes this tutorial - I hope this was helpful to your project. In case you require any assistance, I'm typically in the Ren'Py support server as @jbondguy007, feel free to ping me and I can try to offer assistance if time allows.

Thanks for reading, and happy coding!
