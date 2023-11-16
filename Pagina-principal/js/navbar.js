window.addEventListener("scroll", () => {
    if ( window.scrollY>900 ){
		document.querySelector("header").classList.add("scrolled");
	}else{
		document.querySelector("header").classList.remove("scrolled");
	}
})