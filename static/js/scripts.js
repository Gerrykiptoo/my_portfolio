document.getElementById('contact-button').addEventListener('click', function() {
    openModal('contact-modal');
});

document.getElementById('hire-button').addEventListener('click', function() {
    openModal('hire-modal');
});

function openModal(modalId) {
    document.getElementById(modalId).style.display = 'block';
}

function closeModal(modalId) {
    document.getElementById(modalId).style.display = 'none';
}
