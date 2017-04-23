This text file provides information for running the following programs: 
1) galtonBoard.py
2) convexHull.py



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~galtonBoard.py~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The following software is required for execution of this program, and also for reading output:
1) imageMagick: https://www.imagemagick.org/script/download.php
--> download, and while installing make sure to select "Install legacy utilities (e.g. convert)"
2) gifviewer: https://sourceforge.net/projects/gifviewer/
--> download and install, or use another viewer to view the output gifs



The following modifications must be made in order to successfully create animations on your PC:
@ line 299 make sure that the path for the convert.exe command is 'C:\Program Files\ImageMagick-7.0.5-Q16'
@ line 301-302 check that the paths correspond to appropriate folder locations in our project submission file



To run the program:
1) open galtonBoard.py in, for example, PyCharm (run from the unzipped folder it was submitted in)
2) @ line 25, modify numBalls = ... to the number of balls you wish to drop into the galton board
              (because n_skips = numBalls/100, this works for numBalls=100,1000,10000,50000,100000,1000000)
   
   @ line 27, [optional] modify n_skips = ... to the number of plots which will be skipped in the sequence
              (i.e. if n_skips = 1, none of the plots will be skipped) 

3) run galtonBoard.py
4) galtonBoard_plots contain all plots (for exercises where numBalls=100,1000,10000,50000,100000,1000000)
   galtonBoard_gifs contain all gifs (for exercises where numBalls=100,1000,10000,50000,100000,1000000)
   
   **NOTE: When you run the program, the plots will go into the galtonBoard_plots folder. The gifs will also 
           go into the galtonBoard_plots folder; for convenience, all plots and gifs have already been 
           manually added into the appropriate subfolders.
   **Thus, if you want to view the pre-run plots for 100 balls, go to "galtonBoard_plots/numBalls = 100"
   **If, for example, you want to view the pre-run gif for 100 balls, go to galtonBoard_gifs/numBalls = 100"



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~convexHull.py~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
No additional software is required for execution of this program, or for reading output.



To run the program:
1) open convexHull.py in, for example, PyCharm (run from the unzipped folder it was submitted in)
2) @ line 154, modify selEx = "all" to the desired exercise number (1,2,3,4,5,6)
               (note that "all" selects all exercises).
3) run convexHull.py
4) convexHull_plots contains all plots (for the exercises that have been specified by selEx)
