const parallax_elements = document.querySelectorAll(".parallax");

let xMouse = 0, yMouse = 0, rotateDegree = 0;

function update(event){
    parallax_elements.forEach((element) => {
        let speedx = element.dataset.speedx;
        let speedy = element.dataset.speedy;
        let speedz = element.dataset.speedz;
        let speedrotate = element.dataset.speedrotate;

        let isInLeft = parseFloat(getComputedStyle(element).left) < window.innerWidth / 2 ? 1 : -1;
        let zValue = (event.clientX - parseFloat(getComputedStyle(element).left)) * isInLeft * 0.1;

        element.style.transform = `translateX(calc(-50% + ${-xMouse * speedx}px)) translateY(calc(-50% + ${yMouse * speedy}px)) rotateY(${rotateDegree * speedrotate}deg) perspective(2300px) translateZ(${zValue * speedz}px)`;
    })
}

update(0)

window.addEventListener("mousemove", (event) => {
    xMouse = event.clientX - window.innerWidth / 2;
    yMouse = event.clientY - window.innerHeight / 2;
    rotateDegree = xMouse / (window.innerWidth / 2) * 20;

    update(event);
})
