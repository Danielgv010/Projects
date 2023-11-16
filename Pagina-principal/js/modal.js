let modal = document.getElementById("modal");
let bannerContent = document.getElementsByClassName("banner-content")[0];
let close = document.getElementById("close");
let open = document.getElementById("open");

open.addEventListener("click", function() { 
    document.body.classList.add("modal-open");
    modal.style.display = "flex";
    bannerContent.style.display = "none";
});

close.addEventListener("click", function() {  
    document.body.classList.remove("modal-open");
    modal.style.display = "none";
    bannerContent.style.display = "block";
});

window.addEventListener("click", function (event) { 
    if (event.target == modal) {
        document.body.classList.remove("modal-open");
        modal.style.display = "none";
        bannerContent.style.display = "block";
    }
});