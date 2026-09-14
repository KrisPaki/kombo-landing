const lightbox = document.querySelector('#lightbox');
const image = document.querySelector('#lightbox-image');
const caption = document.querySelector('#lightbox-caption');
let opener;
for (const link of document.querySelectorAll('[data-lightbox]')) {
  link.addEventListener('click', (event) => {
    if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey || typeof lightbox.showModal !== 'function') return;
    event.preventDefault();
    opener = link;
    const thumbnail = link.querySelector('img');
    image.src = link.href;
    image.alt = thumbnail.alt;
    caption.textContent = `${thumbnail.alt} — fot. Krystian Pakieła`;
    lightbox.showModal();
  });
}
document.querySelector('.lightbox-close').addEventListener('click', () => lightbox.close());
lightbox.addEventListener('click', (event) => { if (event.target === lightbox) lightbox.close(); });
lightbox.addEventListener('close', () => { image.removeAttribute('src'); opener?.focus({ preventScroll: true }); });
