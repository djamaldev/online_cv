function reveal_work() {
    var reveals = document.querySelectorAll("#work");
  
    for (var i = 0; i < reveals.length; i++) {
      var windowHeight = window.innerHeight;
      var elementTop = reveals[i].getBoundingClientRect().top;
      var elementVisible = 150;
  
      if (elementTop < windowHeight - elementVisible) {
        reveals[i].classList.add("active");
      } else {
        reveals[i].classList.remove("active");
      }
    }
  }

  function reveal_info() {
    var reveals = document.querySelectorAll("#info");
  
    for (var i = 0; i < reveals.length; i++) {
      var windowHeight = window.innerHeight;
      var elementTop = reveals[i].getBoundingClientRect().top;
      var elementVisible = 150;
      reveals[i].classList.add("active");
      if (elementTop < windowHeight - elementVisible) {
        reveals[i].classList.add("active");
      } else {
        reveals[i].classList.remove("active");
      }
    }
  }
  function reveal_contact() {
    var reveals = document.querySelectorAll("#contact");
  
    for (var i = 0; i < reveals.length; i++) {
      var windowHeight = window.innerHeight;
      var elementTop = reveals[i].getBoundingClientRect().top;
      var elementVisible = 150;
  
      if (elementTop < windowHeight - elementVisible) {
        reveals[i].classList.add("active");
      } else {
        reveals[i].classList.remove("active");
      }
    }
  }
  
  window.addEventListener("scroll", reveal_work);
  window.addEventListener("scroll", reveal_info);
  window.addEventListener("scroll", reveal_contact);

  $(document).scroll(function(){
    var scroll = $(window).scrollTop();
    var amount = -160+(scroll*0.8);
    if (amount < 10)
    {
      $('#info').css({left:amount+"px"});
    }
  });