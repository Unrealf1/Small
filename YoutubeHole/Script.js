// ==UserScript==
// @name         YouTubeHole
// @namespace    http://tampermonkey.net/
// @version      0.2
// @description  Redirectiong to the next recommended video every 5-15 seconds and logging title and url
// @author       Unrealf1
// @match        https://www.youtube.com/*
// @grant        none
// ==/UserScript==

const key = "YoutubeHoleExperiment"

function goNext() {
    if (!window.location.href.includes("watch")) {
        console.log("Not on a page with video");
        return;
    }

    const title = document.title;
    const current = window.location.href;
    var next = document.getElementById("thumbnail").href;
    if (!next) {
        const b = document.getElementsByClassName("yt-simple-endpoint inline-block style-scope ytd-thumbnail")
        for (var i = 0; i < b.length; i++) {
            if (b[i].href && !(b[i].href.includes("playlist"))) {
                next = b[i].href;
                break;
            }
        }
    }
    if (!next) {
        console.log("no links found")
        return;
    }
    console.log(title)
    console.log(next)
    const prev = localStorage.getItem(key)
    localStorage.setItem(key, prev + " |$| " + title + "(" + current + ")")

    window.location.href = next;
}

(function() {
    if (!localStorage.getItem(key)) {
        localStorage.setItem(key, "");
    }
    const sleep_for = 5000 + Math.random() * 10000;
    setTimeout(goNext, sleep_for)
})();
