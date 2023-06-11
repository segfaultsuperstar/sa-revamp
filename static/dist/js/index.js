const slideFormat = function(){
  let slideIndex = 1;
  showSlides(slideIndex);

  // Next/previous controls
  function plusSlides(n) {
    showSlides(slideIndex += n);
  }

  function showSlides(n) {
    let i;
    let slides = document.getElementsByClassName("slide");
    if (n > slides.length) {
      slideIndex = 1;
    }
    if (n < 1) {
      slideIndex = slides.length
    }
    for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
    }
    slides[slideIndex-1].style.display = "block";
  } 

  $('.next').click(function() {
    plusSlides(1);
  });

  $('.prev').click(function() {
    plusSlides(-1);
  });
}
slideFormat()
$(".game-link").on('click', (function() {
  var game = $(this).attr('id');
  var cname = $('title').text().toLowerCase();
    $.ajax({
        type: "GET",
        url: "/select/game",
        data: {'game': game,
              'cname': cname,},
        success: function(db_data) {
          $('#reviews-container').html(db_data['new_data']);
          slideFormat();
        }
    });
  })
);
