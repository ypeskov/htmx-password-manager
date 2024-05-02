function toggleVisibility() {
  const element = document.getElementById('new-item-select');
  if (element.classList.contains('hidden-selector')) {
    element.classList.remove('hidden-selector');
    element.classList.add('visible-selector');
  } else {
    element.classList.add('hidden-selector');
    element.classList.remove('visible-selector');
  }
}

