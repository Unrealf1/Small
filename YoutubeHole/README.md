# YoutubeHole
The idea was to see, where would youtube guide me, if I were to click the first recommended video every time. The idea came to me after watching [this talk](https://www.youtube.com/watch?v=v9EKV2nSU8w).

# How it works?
Contents of .js script were placed in tapermonkey browser extension, so on every youtube page it will run automatically and if it is a video page, then in random amount of sedonds (5 to 15) it will log current video in localStorage and switch to the next recommended video.

To extract the results you have to type localStorage.getItem("YoutubeHoleExperiment") in your browser concole and copy output to a file. Then run .py script with path to this file as the first argument and path to the output file as the second. Don't forget to erase result, before rerunning by typing localStorage.setItem("YoutubeHoleExperiment", "") or localStorage.removeItem("YoutubeHoleExperiment") in your browser console.
