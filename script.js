// Smooth scroll
document.querySelectorAll('a[href^=\"#\"]').forEach(anchor => {
    anchor.addEventListener('click', e => {
        e.preventDefault();
        document.querySelector(anchor.getAttribute('href')).scrollIntoView({ behavior: 'smooth' });
    });
});

// Busca dinâmica
function initSearch() {
    const input = document.createElement('input');
    input.placeholder = 'Buscar (coração, fluxo, válvulas...)';
    input.style.cssText = 'width: 100%; padding: 0.8rem; margin-bottom: 1rem; border: 2px solid #d32f2f; border-radius: 25px; font-size: 1rem;';
    input.addEventListener('input', e => {
        const term = e.target.value.toLowerCase();
        document.querySelectorAll('section').forEach(sec => {
            sec.style.display = sec.textContent.toLowerCase().includes(term) ? 'block' : 'none';
        });
    });
    document.querySelector('header').appendChild(input);
}

initSearch();

// Pausar/reproduzir vídeos ao scroll
window.addEventListener('scroll', () => {
    document.querySelectorAll('iframe').forEach(iframe => {
        const rect = iframe.getBoundingClientRect();
        if (rect.top < window.innerHeight && rect.bottom > 0) {
            // Vídeo visível, continua
        }
    });
});
