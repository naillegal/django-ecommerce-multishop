const wishButton = document.querySelectorAll('.wish-button');

function wishButtonHandler() {
    const productId = this.getAttribute('product-id')
    if (this.classList.contains('wished')) {
        fetch(`http://127.0.0.1:8000/en/api/remove-wish/${productId}`).then(response => {
            if (response.status === 200){
                this.classList.replace('wished', 'nonwished')
                this.innerHTML = '<i class="far fa-heart"></i>'
            }
        })
    } else if (this.classList.contains('nonwished')) {
        fetch(`http://127.0.0.1:8000/en/api/add-wish/${productId}`).then(response => {
            if (response.status === 200){
                this.classList.replace('nonwished', 'wished')
                this.innerHTML = '<i class="fas fa-heart"></i>'
            }
        })
    } 
}

for (let likeButton of wishButton) {
    likeButton.onclick = wishButtonHandler
}






