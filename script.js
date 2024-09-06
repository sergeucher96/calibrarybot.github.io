// Получаем все элементы с классом "category-block"
const categoryBlocks = document.querySelectorAll('.category-block');
// Получаем все иконки приложений
const appIcons = document.querySelectorAll('.app-icon');
// body
const bodyElement = document.querySelector("body");

categoryBlocks.forEach(block => {
    block.addEventListener('click', (e) => {
        e.preventDefault(); // Предотвращаем переход по ссылке
        const category = block.dataset.category; // Получаем выбранную категорию

        // Перебираем все иконки
        appIcons.forEach(icon => {
            const categories = icon.dataset.categories.split(', '); // Получаем массив категорий иконки
            if (category === 'all' || categories.includes(category)) {
                icon.parentElement.style.display = 'block'; // Показываем иконку
            } else {
                icon.parentElement.style.display = 'none'; // Скрываем иконку
            }
        });
        // плавно скролим вверх
        bodyElement.scroll({
            top: 0,
            behavior: 'smooth'
        });
    });
});
    // Запретить перетаскивание на весь сайт
    document.addEventListener('dragstart', (e) => {
        e.preventDefault(); // Отменить действие по умолчанию
    });