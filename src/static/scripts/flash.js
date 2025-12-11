const FADE_DURATION = 300;

document.querySelectorAll('.flash-card').forEach((card) => {
  const duration = parseInt(card.getAttribute('data-duration'));
  card.style.setProperty('--flash-duration', `${duration}ms`);

  requestAnimationFrame(() => {
    requestAnimationFrame(() => {
      card.classList.add('enter');
    });
  });

  let removed = false;
  const removeCard = () => {
    if (removed) return;
    removed = true;
    card.classList.add('removing');
    setTimeout(() => {
      card?.remove();
    }, FADE_DURATION + 20);
  };

  const endTimer = setTimeout(removeCard, duration);

  const closeBtn = card.querySelector('.flash-close');
  closeBtn.addEventListener('click', () => {
    clearTimeout(endTimer);
    removeCard();
  });
});
