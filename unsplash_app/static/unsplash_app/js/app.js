const IMAGES = imagesData;

const explore = document.getElementById("explore");
const img_cards = document.querySelectorAll(".img_card")

img_cards.forEach(card => {
    card.addEventListener("click", ()=>{
        IMAGES.forEach(img => {
            if (img.id === card.id) {
                console.log(img.urls.full)
                window.open(img.urls.full, '_blank');
            }
        })
        console.log(card.id)
    })
})

console.log(IMAGES[0])