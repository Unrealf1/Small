# YoutubeHole
The idea was to see, where would youtube guide me, if I were to click the first recommended video every time. This idea came to me after watching [this talk](https://www.youtube.com/watch?v=v9EKV2nSU8w). Spoilers - almost every time it's children's content.

### I recommend logging out of your main youtube account to save your sanity.

### How does it work?
Contents of .js script were placed in tapermonkey browser extension, so on every youtube page it will run automatically and if it is a video page, then in a random amount of seconds (5 to 15) it will log current video in localStorage and switch to the next recommended video.

To extract the results you have to type localStorage.getItem("YoutubeHoleExperiment") in your browser console and copy output to a file. Then run .py script with the path to this file as the first argument and path to the output file as the second. Don't forget to erase result, before rerunning by typing localStorage.removeItem("YoutubeHoleExperiment") in your browser console.

### It seems like Google Chrome has a lower limit on how much data is possible to store in one variable of localStorage than Firefox. On Chrome it was possible to store 5KB of data(~45 videos), while Firefox had no problem with more than 80KB, so I would recommend using the latter.
