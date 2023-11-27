# CSE 100 Implementations and Scripts
This is a largely informal project, so I'll use a more casual format in lieu of a more professional README. There are no relevant contribution guidelines or security notices, and I will not be monitoring this repository for issues. Development will likely cease after 2023-12-16, the date of my last final for this academic quarter.

This repository is intended to host implementations of the data structures taught in CSE 100: Advanced Data Structures, as well as any additional helper programs that I may write in order to aid the completion of homework for this class. Reading quizzes and data structures from the lectures are implemented in the `Lectures` folder, while Programming Assignments are implemented in the `PAs` folder. Neither folder is comprehensive, nor are they meant to be.

All code is written in Python. There is no real reason for this, except that I didn't want to bother with a compiled language and it will be an extremely cold day in San Diego before I write serious programs in Ruby. I'll probably rewrite this in Haskell or something just for fun, but that's at least a few months down the line.

## Format
Filenames will consist of the abbreviated names of the relevant lectures or programming assignments. If there are multiple such lectures or programming assignments, the names will be concatenated. For instance, `L24L25` implements up-trees, which are the subject of both Lecture 24 and Lecture 25.

There is no such format for the code written *within* the files. Again, since this repository does not accept external contributions, this lack of consistent format should not be relevant. For the most part, programs will have the following format:
```
import statements

constant definitions

function one

function two


relevant driver code
```

## Usage
These programs are not intended for robust usage and as such do not have a command line interface. As such, adapting a program to run with arbitrary data or parameters will require manual modification of the code. I have made a minor effort to limit these modifications to the constant definitions at the top, so as to make this code as easy to modify as possible, but this is not true everywhere.

Similarly, I plan on eventually making most of these programs more consistent with module code, such that the relevant methods can be imported and ran. This, too, will some time before it is finished.

## "Isn't This Academic Dishonesty?"
Not really. Reading quizzes are graded on a completion basis anyway, so an unmotivated student could just as well submit garbage answers and receive their points. The availability of a repository that "solves" these quizzes is hardly jeopardizing the integrity of this class.

Even if it were, the vast majority of these programs are simply implementing extremely widely used data structures and algorithms, all of which are already implemented elsewhere. This repository offers no more functionality than "red black tree visualization online" on Google would. It is extremely difficult to make a compelling argument that my code, specifically, is going to help a student achieve unfair results in this class.

Of course, I am willing to take this code down if requested to do so by the relevant members of UCSD faculty or administration.

## License
This code is licensed under GPLv3, unless it turns out that I'm not actually GPL compliant and that all of my code is illegally licensed, in which case this code is entirely unlicensed and nobody should use it. I, as usual, make no warranties and accept no liability for any damage incurred from the use of this code. I'm not really sure how you would cause damage, but I don't want anything to do with it.

I would use a beerware license, but I'm frankly scared that my FOSS friends will find out and crucify me.