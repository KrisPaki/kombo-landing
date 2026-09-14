const lightbox = document.querySelector('#lightbox');
const image = document.querySelector('#lightbox-image');
const caption = document.querySelector('#lightbox-caption');
let opener;
document.addEventListener('click', (event) => {
  const link = event.target.closest('[data-lightbox]');
  if (!link || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey || typeof lightbox.showModal !== 'function') return;
  event.preventDefault();
  opener = link.closest('[aria-hidden="true"]') ? document.querySelector('.motion-toggle') : link;
  const thumbnail = link.querySelector('img');
  image.src = link.href;
  image.alt = thumbnail.alt;
  caption.textContent = `${thumbnail.alt} — fot. Krystian Pakieła`;
  lightbox.showModal();
});
document.querySelector('.lightbox-close').addEventListener('click', () => lightbox.close());
lightbox.addEventListener('click', (event) => { if (event.target === lightbox) lightbox.close(); });
lightbox.addEventListener('close', () => { image.removeAttribute('src'); opener?.focus({ preventScroll: true }); });

// Keep the photo preview discoverable while offering explicit motion controls.
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
const teaser = document.querySelector('.gallery-teaser');
const preview = document.querySelector('.preview-window');
const previewGroup = document.querySelector('.preview-group');
const motionToggle = document.querySelector('.motion-toggle');
const gallery = document.querySelector('.full-gallery');
let photosPaused = reducedMotion.matches;
const duplicate = previewGroup.cloneNode(true);
duplicate.setAttribute('aria-hidden', 'true');
duplicate.querySelectorAll('a').forEach(link => link.tabIndex = -1);
previewGroup.parentNode.append(duplicate);
function updatePhotoMotion() {
  teaser.classList.toggle('is-paused', photosPaused || reducedMotion.matches);
  motionToggle.setAttribute('aria-pressed', String(photosPaused || reducedMotion.matches));
  motionToggle.textContent = reducedMotion.matches ? 'Przesuń zdjęcia palcem lub gładzikiem' : photosPaused ? 'Wznów ruch zdjęć' : 'Wstrzymaj ruch zdjęć';
  motionToggle.disabled = reducedMotion.matches;
}
motionToggle.addEventListener('click', () => { photosPaused = !photosPaused; updatePhotoMotion(); });
new IntersectionObserver(([entry]) => {
  preview.dataset.moving = String(entry.isIntersecting && !document.hidden);
}, { threshold: 0.1 }).observe(preview);
gallery.addEventListener('toggle', () => {
  gallery.querySelector('.gallery-action').textContent = gallery.open ? 'Zwiń galerię' : 'Rozwiń całą galerię';
});
updatePhotoMotion();

// Autoplay only visible videos. Native controls retain pause, sound and fullscreen.
const videos = [...document.querySelectorAll('.portfolio-video')];
const visibleVideos = new Set();
const manuallyPaused = new WeakSet();
const explicitPlay = new WeakSet();
function synchronizeVideos() {
  for (const video of videos) {
    const shouldPlay = visibleVideos.has(video) && !document.hidden && !lightbox.open && !manuallyPaused.has(video) && (!reducedMotion.matches || explicitPlay.has(video));
    if (shouldPlay) video.play().catch(() => {});
    else video.pause();
  }
}
for (const video of videos) {
  video.muted = true;
  video.addEventListener('pause', () => {
    if (visibleVideos.has(video) && !document.hidden && !lightbox.open && !reducedMotion.matches && !video.ended) manuallyPaused.add(video);
  });
  video.addEventListener('play', () => { manuallyPaused.delete(video); explicitPlay.add(video); });
  video.addEventListener('volumechange', () => {
    if (!video.muted) for (const other of videos) if (other !== video) other.muted = true;
  });
}
const videoObserver = new IntersectionObserver(entries => {
  for (const entry of entries) {
    if (entry.isIntersecting && entry.intersectionRatio >= 0.12) visibleVideos.add(entry.target);
    else visibleVideos.delete(entry.target);
  }
  synchronizeVideos();
}, { threshold: [0, 0.12] });
videos.forEach(video => videoObserver.observe(video));
document.addEventListener('visibilitychange', () => {
  if (document.hidden) preview.dataset.moving = 'false';
  else preview.dataset.moving = 'true';
  synchronizeVideos();
});
new MutationObserver(synchronizeVideos).observe(lightbox, { attributes: true, attributeFilter: ['open'] });
reducedMotion.addEventListener('change', () => {
  photosPaused = reducedMotion.matches;
  if (reducedMotion.matches) videos.forEach(video => explicitPlay.delete(video));
  updatePhotoMotion();
  synchronizeVideos();
});
