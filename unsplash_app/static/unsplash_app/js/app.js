CLIENT_ID = "xJt3ueEHF-iFVzywR-czMBWaDH9O_uvsptbC-kPTQD0"


// ! Gallery Cards var
const IMAGES = imagesData;
const explore = document.getElementById("explore");
const img_cards = document.querySelectorAll(".img_card")

// ! Modal cards vars
const card = document.querySelector(".card");
const modal = document.querySelector(".modal");
const overlay = document.querySelector(".overlay");
const author = document.querySelector(".modal_top-left h2");
const download_btn = document.querySelector(".btn-download");
const modal_img = document.querySelector(".modal img")

const photographer = document.getElementById("photographer")

// ! Local Vars
let current_img

// ! Card Selection
img_cards.forEach(card => {
    card.addEventListener("click", ()=>{
        IMAGES.forEach(img => {
            if (img.id === card.id) {
                current_img = img
                console.log(img.urls.regular)
                modal_img.src = img.urls.regular
                photographer.textContent = img.user.name
                modal.classList.remove("hidden");
                overlay.classList.remove("hidden");
                // window.open(img.urls.full, '_blank');
            }
        })
        console.log(card.id)
    })
})

console.log(IMAGES[0])

// ! Modal Functionality
  overlay.addEventListener("click", () => {
    modal.classList.add("hidden");
    overlay.classList.add("hidden");
  });
  
  download_btn.addEventListener("click", () => {
    const dropdown_value = document.querySelector(".dropdown").value;
    console.log(dropdown_value);
    let download_url = current_img.urls[dropdown_value]
    window.open(download_url, '_blank');
  });

