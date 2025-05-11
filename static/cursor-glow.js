document.addEventListener('DOMContentLoaded', () => {
    const glowDot = document.createElement('div');
    glowDot.style.position = 'fixed';
    glowDot.style.width = '20px';
    glowDot.style.height = '20px';
    glowDot.style.borderRadius = '50%';
    glowDot.style.background = 'rgba(163, 217, 202, 0.8)';
    glowDot.style.boxShadow = '0 0 15px 5px rgba(163, 217, 202, 0.8)';
    glowDot.style.pointerEvents = 'none';
    glowDot.style.zIndex = '10000';
    glowDot.style.transition = 'transform 0.1s ease-out';
    glowDot.style.transform = 'translate(-50%, -50%)';
    document.body.appendChild(glowDot);

    document.addEventListener('mousemove', (e) => {
        glowDot.style.left = e.clientX + 'px';
        glowDot.style.top = e.clientY + 'px';
    });
});
