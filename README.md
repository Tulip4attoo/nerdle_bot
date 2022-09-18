# Nerdle_bot

A bot to solve https://nerdlegame.com/

# Install & Run
You need python 3 to run it.

+ Clone the repo
`git clone https://github.com/Tulip4attoo/nerdle_bot.git`
+ Run the script
`python core.py`

There are 3 values in result list, that I label:
+ 0 as not in the target operation, default value.
+ 1 as in the position but wrong spot.
+ 2 as correct spot.

Here is an example of today question:
![Bot solve question](2022_09_18_225106.gif)

Of course I could write a web UI to solve it but I got too lazy.
You could also check how it solve an question by using `utils.solve_a_target` function.

# How

I solved it in 5 steps:
+ step 1: (DONE) gen all valid operations
+ step 2: (DONE) create check guess operations function
+ step 3: (DONE) calculate score for each guess
+ step 4: (DONE) create a search bot with score in step 3
+ step 5: (DONE) test and evalute the bot

Step 3 is based on 3Blue1Brown video on Wordle bot.