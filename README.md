## Project Title
### BikeShare

### Date created
08 October 2023

### Description
Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

In this project, we use data provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. We compare the system usage between three large cities: Chicago, New York City, and Washington, DC.

### Files used
- bikeshare_2.py: The bikeshare.py file is set up as a script that takes in raw input to create an interactive experience in the terminal that answers questions about the dataset.
- chicago.csv: The dataset set containing Chicago City data
- new_york_city.csv: The dataset set containing New York City data
- washington.csv: The dataset set containing Washington City data

## An Interactive Experience
The experience is interactive because depending on a user's input, the answers to the questions on the previous page will change! There are four questions that will change the answers:

1. Would you like to see data for Chicago, New York, or Washington?
2. Would you like to filter the data by month, day, or not at all?
3. (If they chose month) Which month - January, February, March, April, May, or June?
4. (If they chose day) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?

## The Datasets

Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:
- Start Time (e.g., 2017-01-01 00:07:57)
- End Time (e.g., 2017-01-01 00:20:53)
- Trip Duration (in seconds - e.g., 776)
- Start Station (e.g., Broadway & Barry Ave)
- End Station (e.g., Sedgwick St & North Ave)
- User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:
- Gender
- Birth Year

### Credits
- [GIT CHEAT SHEET](https://education.github.com/git-cheat-sheet-education.pdf)