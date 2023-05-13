/*
 * @Date: 2023-03-07 21:23:06
 * @LastEditors: r7000p
 * @LastEditTime: 2023-03-20 20:20:46
 * @FilePath: \web-project\site07\scripts\hello.js
 */

// document.querySelector("h1").addEventListener("click", function(){
//     console.log(Date.now());
// });

// document.querySelector("h1").addEventListener("click", () => {
//     console.log(Date.now());
// });

// document.querySelector("h1").addEventListener("click", function () {
//     alert("别戳我，我怕疼。");
// });

let myImg = document.querySelector("img");
let myName = document.querySelector("span");
myImg.onclick = function() {
    let mySrc = myImg.getAttribute("src")
    if(mySrc === "./src/mob.jpg") {
        myImg.setAttribute("src", "./src/kubo.jpg");
        myName.textContent = "kubo !!!";
        console.log("kubo !!!")
    } else {
        myImg.setAttribute("src", "./src/mob.jpg");
        myName.textContent = "mob";
        console.log("mob")
    }
}

let setUserName_btn = document.querySelector("button");
let curUserName = document.querySelector("h2");
// let curUserName = document.querySelector("h2");

function setUserName() {
    let userName = prompt("你的名字：");
    if(!userName) {
        setUserName();
    }
    else {
        localStorage.setItem("name", userName);
        curUserName.textContent = userName;
    }
}

if(!localStorage.getItem("name")) {
    setUserName();
}
else {
    let storedName = localStorage.getItem("name");
    curUserName.textContent = storedName;    
}

setUserName_btn.onclick = function() {
    setUserName();
}
