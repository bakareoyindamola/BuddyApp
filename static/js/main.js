const openModalButtons = document.querySelectorAll('[data-modal-target]');
const overlay = document.getElementById('overlay');
const modalOverlay = document.getElementById('modaloverlay');

if(overlay) {
    overlay.addEventListener('click', () => {
        const modals = document.querySelectorAll('.success-registration');
        modals.forEach(modal => {
            closeModal(modal);
        })
    })
}

openModalButtons.forEach( button => {
    button.addEventListener('click', () => {
        const modal = document.querySelector(button.dataset.modalTarget);
        openModal(modal)
    })
});


function openModal(modal) {
    if (modal == null) return
    modal.classList.add('active')
    modalOverlay.classList.add('active')
}

modalOverlay.addEventListener('click', () => {
    const modals = document.querySelectorAll('.notify-me.active');
    modals.forEach(modal => {
        closeNotifyModal(modal);
    })
})

function closeModal(modal) {
    if (modal == null) return
    modal.classList.add('inactive')
    overlay.classList.add('inactive')
}

function closeNotifyModal(modal) {
    if (modal == null) return
    modal.classList.remove('active')
    modalOverlay.classList.remove('active')
}

const email1 = document.querySelector('#email1');
const email2 = document.querySelector('#email2');
const button1 = document.getElementById("submitBtn1");
const button2 = document.getElementById("submitBtn2");


function disableButton(emailName, button) {
    emailName.addEventListener('keyup', () => {
        const emailValue = emailName.value;
        if(emailValue.length == 0) {
            button.disabled = true; 
        }else {
            button.disabled = false; 
        }
    })
}

disableButton(email1, button1);
disableButton(email2, button2);





