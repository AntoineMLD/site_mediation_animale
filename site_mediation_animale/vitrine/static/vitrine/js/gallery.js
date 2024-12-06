document.addEventListener('DOMContentLoaded', function () {
    const images = document.querySelectorAll('.gallery img');

    images.forEach(img => {
        img.addEventListener('click', () => {
            alert('Vous avez cliqué sur une image!');
        });
    });
});
