# Python-Programs
Problem Statement-
You are given a text file as input.

Each line contains 2 words separated by a space. Both the words will have the same number of letters and are lowercase. You are required to find linear and circular distances between them.

Linear is when the alphabet in arranged in a list understood. abc....xyz Circular is when we assume after ...xyz we again have abc.... So in some cases, going in a circle might be shorter.

Examples:

cake make

c -> m = 10 linear (defghijkl), 10 circular(defghijkl)
a -> a = 0, 0
k -> k = 0, 0
e -> e = 0, 0
Total = 10 linear, 10 circular 
pod lot

p -> l = 4 linear (onm), 4 circular (onm)
o -> o = 0
d -> t = 16 linear (efghijklmnopqrs), 10 circular (uvwxyzabc) because it is shorter to go in a circle here
Total = 20 linear, 14 circular
For a file with following words:

cake make
pod lot
abc def
xyz abc
rail liar
Correct output (linear, circular) would be:

10 10
20 14
9 9
69 9
28 28
