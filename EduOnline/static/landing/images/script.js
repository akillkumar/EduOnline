var swiper = new Swiper(".couse-sliderr", {
    spaceBetween: 20,
    grabCursor:true, 
    loop:true,
    pagination: {
      el: ".swiper-pagination",
      clickable:true,
    },
    breakpoints: {
        640: {
          slidesPerView: 1,
        },
        768: {
          slidesPerView:2, 
        },
        1024: {
          slidesPerView: 3,
        },
    },
  });