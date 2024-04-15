document.addEventListener("DOMContentLoaded", function () {
  // Slide de imagens no banner principal
  let images = ["img/banner1.jpg", "img/banner2.jpg", "img/banner3.jpg"];
  let currentImageIndex = 0;
  let bannerImage = document.getElementById("banner-image");

  function changeBannerImage() {
    bannerImage.src = images[currentImageIndex];
    currentImageIndex = (currentImageIndex + 1) % images.length;
  }

  setInterval(changeBannerImage, 5000); // Altera a imagem a cada 5 segundos

  // Exibição de depoimentos de clientes em um carrossel
  let testimonials = [
    { name: "João Silva", text: "Adorei os chocolates, são deliciosos!" },
    { name: "Maria Santos", text: "Atendimento excelente, recomendo a todos!" },
    {
      name: "Pedro Oliveira",
      text: "Entrega rápida e produtos de alta qualidade.",
    },
  ];
  let currentTestimonialIndex = 0;
  let testimonialContainer = document.getElementById("depoimentos");

  function showNextTestimonial() {
    let testimonial = testimonials[currentTestimonialIndex];
    testimonialContainer.innerHTML = `<p><strong>${testimonial.name}:</strong> ${testimonial.text}</p>`;
    currentTestimonialIndex =
      (currentTestimonialIndex + 1) % testimonials.length;
  }

  setInterval(showNextTestimonial, 7000); // Mostra o próximo depoimento a cada 7 segundos
});
