const accordionHeader = document.querySelectorAll(".accordion__top");

console.log(accordionHeader);
accordionHeader.forEach((accordionHeader) => {
  accordionHeader.addEventListener("click", (event) => {
    const accordion = event.target.closest(".accordion");
    const active = accordion.classList.contains("is-active");

    if (active) {
      accordion.classList.remove("is-active");
    } else {
      accordion.classList.add("is-active");
    }
  });
});
