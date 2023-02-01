/*
 * @Date: 2022-07-03 23:29:20
 * @LastEditors: r7000p
 * @LastEditTime: 2022-07-06 22:47:46
 * @FilePath: \Daily\daily-web\web-project\my-site02\scripts\script.js
 */

let myImg = document.querySelector("img");
myImg.onclick = function() {
    let imgSrc = myImg.getAttribute("src");
    if (imgSrc === "./images/img1.jpg") {
        myImg.setAttribute("src", "./images/img2.jpg");
    } else {
        myImg.setAttribute("src", "./images/img1.jpg");
    }
}

let myButton = document.querySelector("button");
let myHead = document.querySelector("h1");

myButton.onclick = function() {
    setName();
}

function setName() {
    let myName = prompt("来个名字~");
    if (myName) {
        localStorage.setItem("name", myName);
        myHead.textContent = "我的猫猫：" + myName;    
    }
}

if (!localStorage.getItem("name")) {
    setName();
} else {
    let storeName = localStorage.getItem("name");
    myHead.textContent = "我的猫猫：" + storeName;
}
