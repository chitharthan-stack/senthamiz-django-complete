// script.js

document.addEventListener('DOMContentLoaded', function() {
    let featuredImg = document.getElementById('featured-image');
    let smallImgs = document.getElementsByClassName('small-Img');

    for (let i = 0; i < smallImgs.length; i++) {
        smallImgs[i].addEventListener('click', () => {
            featuredImg.src = smallImgs[i].src;
            for (let j = 0; j < smallImgs.length; j++) {
                if (i === j) {
                    smallImgs[j].classList.add('sm-card');
                } else {
                    smallImgs[j].classList.remove('sm-card');
                }
            }
        });
    }

    let cards = document.querySelectorAll('.card');
let mouseHover = false;
let mousePosition = { x: 0, y: 0 };
let cardSize = { width: 0, height: 0 };
let SCALE_X = 4;
let SCALE_Y = 8;

cards.forEach(card => {
    card.addEventListener('blur', () => {
        mouseHover = false;
    });

    card.addEventListener('focus', () => {
        mouseHover = true;
    });

    card.addEventListener('mousemove', (e) => {
        if (!mouseHover) return;
        let rect = card.getBoundingClientRect();
        let x = e.clientX - rect.left;
        let y = e.clientY - rect.top;
        mousePosition = { x, y };
        cardSize = {
            width: card.offsetWidth || 0,
            height: card.offsetHeight || 0,
        };
        card.style.transform = `perspective(1000px) rotateX(${
            (mousePosition.y / cardSize.height) * -(SCALE_Y * 2) + SCALE_Y
            }deg) rotateY(${
            (mousePosition.x / cardSize.width) * (SCALE_X * 2) - SCALE_X
            }deg) translateZ(10px)`;
    });

    card.addEventListener('mouseout', () => {
        mouseHover = false;
        card.style.transform = 'perspective(600px) rotateX(0deg) rotateY(0deg) translateZ(0px)';
    });

    card.addEventListener('mouseover', () => {
        mouseHover = true;
    });
});
});
function showNav(){
    document.getElementsByClassName("navigation")[0].classList.toggle("active");
  }

  const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container-login");

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});

// Optional JavaScript for more control over smooth scrolling
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});