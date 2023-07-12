/*
Template Name: EduGrids - Education & Online Course HTML Template.
Author: GrayGrids
*/

(function () {
    //===== Prealoder

    window.onload = function () {
        window.setTimeout(fadeout, 500);
        var header_navbar = document.querySelector(".navbar-area");
        var sticky_phantom = document.querySelector(".sticky-phantom");
        sticky_phantom.style.height = header_navbar.offsetHeight + "px";
    }

    function fadeout() {
        document.querySelector('.preloader').style.opacity = '0';
        document.querySelector('.preloader').style.display = 'none';
    }

    /*=====================================
    Sticky
    ======================================= */
    window.onscroll = function () {
        var header_navbar = document.querySelector(".navbar-area");
        var sticky_phantom = document.querySelector(".sticky-phantom");
        var sticky = header_navbar.offsetTop;
        var toolbar_area = document.querySelector(".toolbar-area");

        if (window.pageYOffset > sticky + toolbar_area.offsetHeight) {
            //sticky_phantom.style.height = header_navbar.offsetHeight + "px";
            header_navbar.classList.add("sticky");
            //sticky_phantom.style.display = "block";
        } else {
            header_navbar.classList.remove("sticky");
            //sticky_phantom.style.display = "none";
        }




        // show or hide the back-top-top button
        var backToTo = document.querySelector(".scroll-top");
        if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
            backToTo.style.display = "flex";
        } else {
            backToTo.style.display = "none";
        }
    };


    // WOW active
    new WOW().init();



    // for menu scroll
    var pageLink = document.querySelectorAll('.page-scroll-edd');

    pageLink.forEach(elem => {
        elem.addEventListener('click', e => {
            e.preventDefault();
            window.location.href = "https://www.rta.lv"+elem.getAttribute('href');
            document.querySelector(elem.getAttribute('href')).scrollIntoView({
                behavior: 'smooth',
                offsetTop: 1 - 60,
            });
        });
    });


      //===== mobile-menu-btn
	let navbarToggler = document.querySelector(".mobile-menu-btn");
	navbarToggler.addEventListener('click', function () {
		navbarToggler.classList.toggle("active");
	});

    //====== counter up
    var cu = new counterUp({
        start: 0,
        duration: 2000,
        intvalues: true,
        interval: 100,
        append: " ",
    });
    cu.start();

})();
